import os
from pathlib import Path
import requests
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request, send_from_directory, stream_with_context

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
app = Flask(__name__, static_folder=None)
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse"

@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")

@app.get("/<path:name>")
def static(name):
    path = (ROOT / name).resolve()
    if name.startswith(".") or name in {"server.py", ".env"} or ROOT not in path.parents or not path.is_file():
        return jsonify(error="Not found"), 404
    return send_from_directory(ROOT, name)

@app.get("/api/status")
def status():
    p = {"gemini": bool(os.getenv("GEMINI_API_KEY")), "groq": bool(os.getenv("GROQ_API_KEY"))}
    return jsonify(providers=p, any_configured=any(p.values()))

def call(provider, model, messages):
    if provider == "groq":
        return requests.post(GROQ_URL, headers={"Authorization":"Bearer "+os.environ["GROQ_API_KEY"],"Content-Type":"application/json"}, json={"model":model,"messages":messages,"stream":True}, stream=True, timeout=(15,180))
    system = next((m["content"] for m in messages if m["role"]=="system"), "")
    transcript = "\n\n".join(("Assistant" if m["role"]=="assistant" else "User")+":\n"+m["content"] for m in messages if m["role"]!="system")
    return requests.post(GEMINI_URL, headers={"x-goog-api-key":os.environ["GEMINI_API_KEY"],"Content-Type":"application/json"}, json={"model":os.getenv("GEMINI_MODEL","gemini-3.8-flash"),"input":system+"\n\n"+transcript,"stream":True}, stream=True, timeout=(15,180))

@app.post("/api/chat")
def chat():
    data=request.get_json(silent=True) or {}
    preferred=data.get("provider","gemini")
    messages=data.get("messages")
    if preferred not in ("gemini","groq") or not isinstance(messages,list) or not messages or len(messages)>20:
        return jsonify(error="Invalid provider or conversation."),400
    clean=[]
    for m in messages:
        if not isinstance(m,dict) or m.get("role") not in ("system","user","assistant") or not isinstance(m.get("content"),str) or len(m["content"])>20000:
            return jsonify(error="Invalid message format or message too long."),400
        clean.append({"role":m["role"],"content":m["content"]})
    order=[preferred,"gemini" if preferred=="groq" else "groq"]
    choices=[]
    for p in order:
        if p=="groq" and os.getenv("GROQ_API_KEY"):
            choices += [(p,os.getenv("GROQ_MODEL","openai/gpt-oss-120b")),(p,"openai/gpt-oss-20b")]
        if p=="gemini" and os.getenv("GEMINI_API_KEY"):
            choices.append((p,os.getenv("GEMINI_MODEL","gemini-3.8-flash")))
    if not choices:
        return jsonify(error="No API keys configured. Add GEMINI_API_KEY and/or GROQ_API_KEY to the host laptop .env file."),503
    errors=[]
    for provider,model in choices:
        upstream=None
        try:
            upstream=call(provider,model,clean)
            if upstream.status_code>=400:
                try:
                    detail=upstream.json().get("error",{}).get("message",upstream.text[:400])
                except Exception:
                    detail=upstream.text[:400]
                errors.append(provider+"/"+model+": "+detail)
                upstream.close()
                continue
            def stream(resp=upstream):
                try:
                    for chunk in resp.iter_content(1):
                        if chunk: yield chunk
                finally: resp.close()
            return Response(stream_with_context(stream()),content_type=upstream.headers.get("Content-Type","text/event-stream"),headers={"Cache-Control":"no-cache, no-transform","X-AI-Provider":provider,"X-Accel-Buffering":"no"})
        except requests.RequestException as e:
            if upstream is not None: upstream.close()
            errors.append(str(e))
    return jsonify(error="All configured providers failed: "+" | ".join(errors[-4:])),502

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.getenv("PORT","8000")),threaded=True)

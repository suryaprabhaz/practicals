# Practicals AI

A responsive coding assistant with a Python LAN backend, server-side Gemini/Groq API keys, streaming responses, local chat history, and offline programming references.

## Run on your laptop and access it from another device on the same Wi-Fi

**For this version, run Flask with `python server.py`, not `python -m http.server`.** The Flask app serves both the frontend and AI API on port 8000.

### 1. Get the latest repository

```bash
git clone https://github.com/suryaprabhaz/practicals.git
cd practicals
```

If you already cloned it, run `git pull`.

### 2. Install dependencies (Windows)

```cmd
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

Open `.env` in Notepad and add your keys on the host laptop:

- `GEMINI_API_KEY` — Google AI Studio API key
- `GROQ_API_KEY` — Groq Console API key

Configure either one or both. The real `.env` is ignored by Git and must never be committed. The repository contains only the empty `.env.example` template.

### 3. Start the backend and frontend together

```cmd
python server.py
```

Or double-click `run.bat` on Windows.

The server listens on `0.0.0.0:8000`. Keep this terminal open.

### 4. Open Practicals AI from the other laptop

On the host laptop, run `ipconfig` and find **IPv4 Address** under the active **Wireless LAN adapter Wi-Fi**.

For example, if the host laptop IP is `192.168.1.20`, open this on the second laptop:

```text
http://192.168.1.20:8000
```

Replace the example IP with the host laptop's actual IPv4 address. Both laptops must be on the same reachable Wi-Fi network. Guest Wi-Fi or router client isolation may block connections between devices.

### 5. Keep it running

- Keep the host laptop powered on, awake, and connected to Wi-Fi.
- Keep `python server.py` running; closing the terminal stops the site and API.
- Allow Python through Windows Defender Firewall on **Private networks** when prompted. If needed, add an inbound TCP rule for port 8000 restricted to the Private profile.
- Do not port-forward port 8000 or expose this development server to the public internet.
- Both laptops use the API keys configured on the host laptop. The browser never receives the keys.
- Chat history and provider selection are stored separately in each browser.
- The host laptop needs internet access for Gemini/Groq requests.

## Provider selection and fallback

Use the provider selector in the app to choose Gemini or Groq. The backend tries the selected provider first and then the other configured provider if the upstream request fails before streaming begins. Groq also tries the configured model followed by `openai/gpt-oss-20b`.

Optional model overrides can be set in the host laptop's local `.env`:

- `GEMINI_MODEL` (default: `gemini-3.8-flash`)
- `GROQ_MODEL` (default: `openai/gpt-oss-120b`)

Check backend configuration at `http://HOST-IP:8000/api/status`. It reports whether provider keys are configured, never their values.

## Troubleshooting

- **Page does not open:** verify same Wi-Fi, use the host laptop's current IPv4 from `ipconfig`, keep the server terminal open, and allow Python through the Private firewall profile.
- **AI says no keys configured:** verify the spelling in `.env`, save it, and restart `python server.py`.
- **IP address changed:** run `ipconfig` again; your router may assign a new local IP.
- **Port 8000 is occupied:** set `PORT=8001` in `.env` and open `http://HOST-IP:8001`.

## Security

This is intended for a trusted private LAN only. Anyone who can reach the app on that LAN may be able to submit AI requests using the host's configured API keys and incur usage charges. Do not use it on public/shared Wi-Fi. For internet-facing use, add authentication, rate limiting, HTTPS, and a production WSGI server.

## GitHub Pages

GitHub Pages can publish the static frontend but cannot run Flask or the Python API. The LAN workflow above requires running `python server.py` on the host laptop.

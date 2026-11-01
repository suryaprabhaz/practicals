# Practicals AI

**Live site:** https://suryaprabhaz.github.io/practicals/

A responsive, monochrome coding assistant with Gemini and Groq streaming and a built-in offline programming reference library.

## Features

- Provider switcher for Google Gemini and Groq
- Streaming responses from both providers with separate API keys and model settings
- Concise coding-first answers and reduced conversation context for faster requests
- Stop-safe streaming UI and visible errors
- Local chat history and settings per browser/device
- Offline reference answers for common DSA, Python, Java, C, SQL, networking and CS topics
- Responsive desktop and mobile UI
- GitHub Pages auto-deployment on pushes to `main`

## Run on your Wi-Fi / LAN (including without internet)

Run this on the computer that will host the site:

```bash
python -m http.server 8000 --bind 0.0.0.0
```

Find that computer's local IPv4 address:

- Windows: run `ipconfig` and look for **IPv4 Address** under the active Wi-Fi adapter.
- Linux: run `hostname -I`.
- macOS: run `ipconfig getifaddr en0` (Wi-Fi; interface may differ).

On another phone, tablet or computer connected to the **same Wi-Fi network**, open:

```text
http://HOST-COMPUTER-IP:8000
```

For example, if the host computer's IP is `192.168.1.20`, open `http://192.168.1.20:8000`.

Important:

- Keep the Python server running and the host computer awake. The other device is loading the site from that computer.
- Allow Python through the host computer's firewall on **Private networks** if prompted. Do not expose port 8000 to public networks/the internet.
- The offline reference library, interface and local chat history work without internet once the page is served on your LAN.
- Gemini and Groq are cloud-hosted. AI-generated answers still require internet access and a key for the selected provider.
- Each device/browser has its own local storage. Enter the relevant Gemini or Groq key separately on each device if you want online AI there.
- On plain HTTP LAN addresses, browsers generally do not allow service workers because the origin is not secure. The site still works while the Python server is reachable; don't expect offline access after the host server is stopped.

## API provider setup

1. Open **API settings** and choose **Google Gemini** or **Groq**.
2. For Gemini, create a key in [Google AI Studio](https://aistudio.google.com/app/apikey). The default model is `gemini-3.8-flash`.
3. For Groq, create a key in [Groq Console](https://console.groq.com/keys). The default model is `llama-3.3-70b-versatile`; you can change the model ID in settings if your account supports another model.
4. Paste the selected provider's key and save. The keys are stored separately, so switching providers does not overwrite the other key.

Gemini uses the Interactions streaming API. Groq uses its OpenAI-compatible streaming Chat Completions endpoint. Keys are stored in that browser's localStorage and sent directly to the selected provider. They are not committed to this repository. This BYOK browser setup is for personal use, not a secure shared-key deployment. Anyone with access to that browser profile can use the stored keys, and browser network requests expose them. Never embed a shared API key in a public static website.

## Offline AI limitation

This repository does **not** contain a local generative AI model. Offline mode searches its built-in programming notes and returns matching reference material; it cannot answer arbitrary new questions like Gemini. Running a real model offline requires downloading and hosting a compatible model (for example, a quantized WebLLM model), sufficient device RAM/storage, and additional setup.

## Deployment

GitHub Actions deploys the repository root to GitHub Pages on every push to `main`.

- Repository: https://github.com/suryaprabhaz/practicals
- Workflow: https://github.com/suryaprabhaz/practicals/actions/workflows/pages.yml
- Live site: https://suryaprabhaz.github.io/practicals/

## Local preview

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Privacy

Chats and the optional API key are stored in the current browser profile only. They are not synchronized between devices. The selected provider (Gemini or Groq) receives your prompts and recent conversation context when you use online AI.

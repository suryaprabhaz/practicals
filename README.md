# Practicals AI

**Live site:** https://suryaprabhaz.github.io/practicals/

A responsive, monochrome coding assistant with Gemini streaming and a built-in offline programming reference library.

## Features

- Gemini Flash streaming through the Gemini API
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
- The Gemini API is cloud-hosted. AI-generated answers still require internet access and a Gemini API key.
- Each device/browser has its own local storage. Enter the Gemini key separately on each device if you want online AI there.
- On plain HTTP LAN addresses, browsers generally do not allow service workers because the origin is not secure. The site still works while the Python server is reachable; don't expect offline access after the host server is stopped.

## Gemini setup

1. Open **API settings**.
2. Create a key in [Google AI Studio](https://aistudio.google.com/app/apikey).
3. Paste it into the browser and save.
4. Online AI requests use Gemini 3.8 Flash through the streaming `generateContent` endpoint.

The key is stored in that browser's localStorage and sent directly to Google. It is not committed to this repository. This BYOK browser setup is for personal use, not a secure shared-key deployment. Anyone with access to that browser profile can use the stored key, and browser network requests expose it. Never embed a shared API key in a public static website.

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

Chats and the optional API key are stored in the current browser profile only. They are not synchronized between devices. Gemini receives your prompts and conversation context when you use online AI.

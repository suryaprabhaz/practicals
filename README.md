# Practicals AI

**Live website:** [https://suryaprabhaz.github.io/practicals/](https://suryaprabhaz.github.io/practicals/)

A minimal, monochrome coding assistant with a calm, Claude-inspired interface.

## Features

- Gemini 3.8 Flash by default, using Google's Interactions API
- Streaming responses for coding questions, debugging and explanations
- Bring your own Gemini API key (BYOK)
- Local chat history stored in the current browser
- Responsive desktop and mobile interface
- Offline app shell and a small built-in programming reference library
- Automatic GitHub Pages deployment on pushes to `main`

## Online AI and offline mode

Gemini is a cloud API and requires an internet connection. The app shell and built-in programming notes can be used offline, but this project does **not** run a generative AI model locally. Full offline inference would require bundling a browser-compatible local model, which is a separate and substantially larger setup.

## Configure Gemini

1. Open the [live website](https://suryaprabhaz.github.io/practicals/).
2. Open **API settings**.
3. Create a fresh API key in [Google AI Studio](https://aistudio.google.com/app/apikey).
4. Paste the key into the website and select **Gemini 3.8 Flash**.
5. Save the settings and start a conversation.

The key is stored in that browser's localStorage and sent directly from the browser to Google through the Gemini Interactions API. It is not committed to this repository. This client-side BYOK setup is intended for personal use, not for distributing a shared API key: anyone with access to that browser profile can use the stored key, and browser network requests expose it.

**Never publish an API key in source code or reuse a key pasted into a chat. Revoke exposed keys and rotate them.**

## Deployment

GitHub Actions deploys the repository root to GitHub Pages whenever code is pushed to `main`.

- **Live URL:** https://suryaprabhaz.github.io/practicals/
- **Repository:** https://github.com/suryaprabhaz/practicals
- **Deployment workflow:** [GitHub Actions](https://github.com/suryaprabhaz/practicals/actions/workflows/pages.yml)
- **Pages source:** GitHub Actions

Pages websites are publicly accessible even when their source repository is private. Availability for private repositories depends on the GitHub plan.

## Local preview

Run from the repository root:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Data and privacy

Chats and the optional API key are stored locally in the current browser profile. They are not synchronized between devices. The API key is sent to Google's Gemini API when you request a response.

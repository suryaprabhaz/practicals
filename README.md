# Practicals AI

A lightweight coding assistant with:
- Gemini streaming responses (bring your own API key)
- Local chat history using browser localStorage
- Mobile-friendly interface
- Offline shell caching and a small built-in programming reference library
- GitHub Pages deployment through GitHub Actions

## Important: online AI vs offline mode

Gemini is a cloud API and requires an internet connection. The app shell and built-in programming notes are cached for offline use, but an actual generative AI model does not run offline in this project. Full offline inference would require bundling/downloading a browser-compatible local model (for example WebLLM), which is a separate, substantially larger setup.

## Configure Gemini

1. Open the deployed website.
2. Click **API settings**.
3. Create a fresh key in Google AI Studio and paste it into the browser.
4. Select the available Gemini model and save.

The key is stored in that browser's localStorage and sent directly from the browser to Google. It is never committed to this repository. This is a personal bring-your-own-key design, not suitable for distributing a shared API key. Anyone with access to that browser profile can use its stored key, and the key is visible in browser network requests.

**Do not reuse a key pasted into chat or committed to source control. Revoke exposed keys and rotate them.**

## Deploy

The workflow in `.github/workflows/pages.yml` deploys the repository root to GitHub Pages on every push to `main`. The repository Pages source should be set to **GitHub Actions**.

For a private repository, GitHub Pages availability depends on your GitHub plan. In repository Settings → Pages, select **GitHub Actions** as the build and deployment source if required. Pages websites are publicly accessible even when the source repository is private.

Expected project site URL:
`https://suryaprabhaz.github.io/practicals/`

## Local preview

From this directory, run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Data

Chats and the optional API key are stored locally in the current browser profile. They are not synchronized between devices.

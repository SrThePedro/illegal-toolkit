# IllegalKit 🛠️

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Styling: Rich](https://img.shields.io/badge/styling-rich-green.svg)](https://github.com/Textualize/rich)

**IllegalKit** is a sleek, lightning-fast, and ad-free terminal-based toolkit designed to replace bloated, ad-ridden web utilities. Built with a hacker-aesthetic CLI, it gives you full control over your media downloads directly from your terminal.

---

## ✨ Features
- **🎬 High-Quality Video/Audio Downloader:** Powered by `yt-dlp`, supporting up to 1080p, 2K, and 4K video downloads.
- **🎵 Seamless Audio Extraction:** Convert videos directly into high-quality MP3s (192kbps).
- **📊 Custom Progress Bars:** Beautiful `rich` progress bars showing live percentage, download speeds, and file sizes.
- **🕹️ Interactive CLI:** Keyboard-driven selection menus using `questionary`.

---

## ⚠️ Prerequisites (Important)
To merge high-quality video/audio streams or extract MP3s properly, **FFmpeg** must be installed on your system.

- **Arch Linux / CachyOS:** `sudo pacman -S ffmpeg`
- **Debian / Ubuntu:** `sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** `winget install ffmpeg`

---

## 🚀 Installation & Setup

### Method 1: Direct Install (Recommended)
Install IllegalKit globally directly from GitHub. This allows you to run the tool from anywhere in your terminal.

```bash
pip install git+https://github.com/SrThePedro/illegal-toolkit
```

### Method 2: Local Install (For Developers)
If you want to modify the code or contribute to the project:

```bash
git clone https://github.com/SrThePedro/illegal-toolkit
cd illegalkit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

---

## ⚡ Usage

Once installed, you don't need to navigate to specific folders. Simply type the magic word anywhere in your terminal:

\`\`\`bash
illegalkit
\`\`\`

Use your arrow keys to navigate the interactive menu, hit **Enter** to select a tool, and enjoy the ad-free terminal experience!
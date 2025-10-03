# CleanPaste

CleanPaste is a small Python tool that automatically **removes hidden formatting** (zero-width spaces, non-breaking spaces, etc.) from text you copy into your clipboard.  
It helps when pasting between apps (e.g., from a browser into Word, or from Docs into code) where weird formatting usually sneaks in.

---

## Features
- Cleans copied text in real time (removes invisible/extra characters).
- Works cross-platform (with a few caveats — see below).
- Simple hotkeys:
  - **F12** → Toggle cleaning ON/OFF
  - **F11** → Quit program
- Status messages printed in the terminal (`ON ✅` / `OFF ❌`).

---

## Installation

Clone this repository and install the dependencies:

```bash
git clone https://github.com/yourusername/CleanPaste.git
cd CleanPaste
pip install -r requirements.txt
```

## ⚙️ Platform Support

- **macOS**: Works, but you must grant Accessibility permissions for hotkeys (System Settings → Privacy & Security → Accessibility).
- **Windows**: Works out of the box.
- **Linux**: Works, but requires `xclip` or `xsel` installed for clipboard access.



import time
import pyperclip  
from pynput import keyboard

def clean_text(text: str) -> str:
    """Remove extra whitespace and invisible characters."""
    cleaned = text.replace('\u200b', '').replace('\xa0', ' ')
    cleaned = " ".join(cleaned.split())
    return cleaned

class CleanPaste:
    def __init__(self):
        self.cleaning_enabled = True
        self.last_text = None
        self.running = True
        print("📝 CleanPaste running...")
        print("   ▶ Press F12 to toggle ON/OFF")
        print("   ▶ Press F11 to quit\n")
        self.print_state()

    def toggle(self):
        self.cleaning_enabled = not self.cleaning_enabled
        self.print_state()

    def print_state(self):
        state = "ON ✅" if self.cleaning_enabled else "OFF ❌"
        print(f"--> Cleaning is {state}")

    def stop(self):
        self.running = False
        print("👋 CleanPaste stopped.")

    def clipboard_loop(self):
        while self.running:
            try:
                if self.cleaning_enabled:
                    text = pyperclip.paste()
                    if text != self.last_text:
                        cleaned = clean_text(text)
                        if cleaned != text:
                            pyperclip.copy(cleaned)
                            print(f"[Cleaned] {cleaned[:50]}{'...' if len(cleaned) > 50 else ''}")
                        self.last_text = cleaned
            except Exception as e:
                print("Error:", e)
            time.sleep(0.2)

def main():
    app = CleanPaste()

    # Hotkeys
    hotkeys = keyboard.GlobalHotKeys({
        '<f12>': app.toggle,     # toggle ON/OFF
        '<f11>': app.stop        # quit program
    })

    hotkeys.start()
    app.clipboard_loop()

if __name__ == "__main__":
    main()

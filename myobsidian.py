import ctypes
import webbrowser
import sys
from pynput.keyboard import Key, Controller

def show_message(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

def press_hotkey():
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.shift):
            keyboard.press('b')
            keyboard.release('b')

def main():
    if len(sys.argv) > 1:
        full_url = sys.argv[1]  # 获取传入的URL
        try:
            obsidian_link = full_url.replace('myobsidian://', 'obsidian://')

            if obsidian_link:
                webbrowser.open(obsidian_link)
                press_hotkey()  # 使用热键打开Obsidian
            else:
                show_message("Error", "Obsidian link not found in URL.")
        except Exception as e:
            show_message("Error", f"Error processing URL: {e}")
    else:
        show_message("Error", "No URL received.")


if __name__ == "__main__":
    main()

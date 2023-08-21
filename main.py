from key_displayer import KeyDisplayer
from pynput import keyboard

def main():
    kd = KeyDisplayer()
    listener = keyboard.Listener(on_press = kd.show_key, on_release=kd.hide_key)
    listener.start()
    kd.start()

if __name__ == '__main__':
    main()
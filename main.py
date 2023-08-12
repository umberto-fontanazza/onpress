from pynput import keyboard
import time

def on_press(key):
    print('Hello!')

listener = keyboard.Listener(on_press = on_press)
listener.start()
time.sleep(100)
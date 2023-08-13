from pynput import keyboard
import tkinter as tk
from PIL import Image, ImageTk

def on_press(key):
    print('Hello!')

def main():
    # listener = keyboard.Listener(on_press = on_press)
    # listener.start()

    letter_image = Image.open('letter_a.png')
    photo = ImageTk.PhotoImage(letter_image)


    window = tk.Tk()
    window.geometry('450x100')
    window.geometry('-100+100') # move window to the top right side
    window.mainloop()

if __name__ == '__main__':
    main()
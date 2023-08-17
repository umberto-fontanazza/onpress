from image_manager import ImageManager
import tkinter as tk
from tkinter import ttk

class KeyDisplayer:
    __instance = None
    __window = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__initialize_tk()
        return cls.__instance

    @classmethod
    def __initialize_tk(cls):
        cls.__window = tk.Tk()
        window = cls.__window
        # window.title('Main window')
        window.rowconfigure(0, weight=1)
        window.geometry('800x200')
        window.geometry('-100+100') # move window to the top right side
        cls.__init_tk_style()
        on_press = lambda key: cls.displayChar(key.char)
        window.bind('<KeyPress>', on_press)
        window.mainloop()

    @classmethod
    def __init_tk_style(cls):
        s = ttk.Style(cls.__window)
        s.theme_use('classic') # https://stackoverflow.com/questions/23750141/tkinter-ttk-widgets-ignoring-background-color
        s.configure('TFrame', background='green')
        s.configure('red.TFrame', background='red')

    @staticmethod
    def __create_image_frame(parent, image : tk.PhotoImage, background = 'green') -> ttk.Frame:
        frame = ttk.Frame(parent, style='red.TFrame' if background == 'red' else None)
        canvas = tk.Canvas(frame, background='purple')
        canvas.grid(row=0, column=0, sticky='nswe')
        canvas.create_image((0,0), image=image, anchor='nw')
        return frame

    @classmethod
    def displayChar(cls, char: str, background='green'):
        shown_keys_count: int = len(cls.__window.winfo_children())
        cls.__window.columnconfigure(shown_keys_count, weight=1)
        image : tk.PhotoImage = ImageManager.open_key_image(char)
        frame = cls.__create_image_frame(cls.__window, image, background)
        frame.grid(row=0, column=shown_keys_count, sticky='nswe')
from image_manager import ImageManager
import tkinter as tk
from tkinter import ttk
from pynput import keyboard
from threading import Timer
from typing import Union

class KeyDisplayer:
    __instance = None
    __window = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialize_tk()
        return cls.__instance

    def __initialize_tk(self):
        self.__window = tk.Tk()
        window = self.__window
        window.rowconfigure(0, weight=1)
        window.geometry('50x50-100+100') # move window to the top right side
        self.__init_tk_style()
        listener = keyboard.Listener(on_press=self.displayChar)
        listener.start()
        window.mainloop()

    @classmethod
    def __init_tk_style(cls):
        s = ttk.Style(cls.__window)
        s.theme_use('classic') # https://stackoverflow.com/questions/23750141/tkinter-ttk-widgets-ignoring-background-color
        s.configure('TFrame', background='green')

    @staticmethod
    def __create_image_frame(parent, image : tk.PhotoImage) -> ttk.Frame:
        frame = ttk.Frame(parent)
        canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0)
        canvas.grid(row=0, column=0, sticky='nswe')
        canvas.create_image((0,0), image=image, anchor='nw')
        return frame

    @classmethod
    def displayChar(cls, key: Union[keyboard.Key, keyboard.KeyCode, None]):
        if type(key) == keyboard.KeyCode:
            char: str = key.char
        elif type(key) == keyboard.Key:
            return
        else:
            return
        shown_keys_count: int = len(cls.__window.winfo_children())
        cls.__window.columnconfigure(shown_keys_count, weight=1)
        image : tk.PhotoImage = ImageManager.open_key_image(char)
        frame = cls.__create_image_frame(cls.__window, image)
        frame.grid(row=0, column=shown_keys_count, sticky='nswe')
        Timer(3.0, lambda: cls.remove_frame(frame)).start()

    @staticmethod
    def remove_frame(frame: ttk.Frame):
        frame.grid_forget()
        frame.destroy()
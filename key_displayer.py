from image_manager import ImageManager, ImageAlreadyOpened
import tkinter as tk
from tkinter import ttk
from pynput import keyboard
from threading import Timer
from typing import Union

class KeyDisplayer:
    __instance = None
    __initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__initialized: return
        self.__shown_keys = 0
        self.__init_tk_window()
        self.__initialized = True

    def __init_tk_window(self):
        self.__window = tk.Tk()
        window = self.__window
        window.overrideredirect(True) # remove OS controls
        window.rowconfigure(0, weight=1)
        window.geometry('0x50-100+100')
        window.attributes('-alpha', 0)
        self.__init_tk_style()
        listener = keyboard.Listener(on_press=self.show_char)
        listener.start()
        window.mainloop()

    def __init_tk_style(self):
        self._style = ttk.Style(self.__window)
        self._style.theme_use('classic') # https://stackoverflow.com/questions/23750141/tkinter-ttk-widgets-ignoring-background-color
        self._style.configure('TFrame', background='green')

    def __create_image_frame(self, parent, image : tk.PhotoImage) -> ttk.Frame:
        frame = ttk.Frame(parent)
        canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0)
        canvas.grid(row=0, column=0, sticky='nswe')
        canvas.create_image((0,0), image=image, anchor='nw')
        return frame

    def show_char(self, key: Union[keyboard.Key, keyboard.KeyCode, None]):
        try:
            image : tk.PhotoImage = ImageManager.open_key_image(key)
        except ImageAlreadyOpened as already_opened:
            print(already_opened)
            return
        except FileNotFoundError as fnf:
            print(fnf)
            return
        self.__update_window_width(50)
        self.__window.columnconfigure(self.__shown_keys, weight=1)
        frame = self.__create_image_frame(self.__window, image)
        frame.grid(row=0, column=self.__shown_keys, sticky='nswe')
        Timer(2.0, lambda: self.hide_char(frame, key)).start()
        self.__shown_keys += 1
        if self.__shown_keys == 1:
            self.__window.attributes('-alpha', 1) # show window

    def hide_char(self, frame: ttk.Frame, key: Union[keyboard.Key, keyboard.KeyCode, None]):
        frame.grid_forget()
        frame.destroy()
        self.__update_window_width(-50)
        ImageManager.close_image(key)
        self.__shown_keys -= 1
        if self.__shown_keys == 0:
            self.__window.attributes('-alpha', 0) # hide window

    def __update_window_width(self, increment: int):
        window = self.__window
        old_width: int = window.winfo_width()
        new_width = old_width + increment
        new_width = new_width if new_width >= 0 else 0
        window.geometry(f'{new_width}x50')
from image_manager import ImageManager, ImageAlreadyOpened
import tkinter as tk
from tkinter import ttk
from pynput import keyboard
from threading import Timer
from typing import Union
from PIL import ImageTk

class KeyDisplayer:
    __instance = None
    __initialized: bool = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, height: int = 50):
        if self.__initialized: return
        self.__window = window = tk.Tk()
        self.__height = height # TODO: replace with setter when ready
        self.__labels: dict[Union[keyboard.Key, keyboard.KeyCode], ttk.Label] = {}
        window.overrideredirect(True)
        window.geometry(f'0x{self.height}-100+100')
        window.wm_attributes('-transparent', True)
        window.configure(bg='systemTransparent')
        self.__initialized = True

    def start(self):
        self.__window.mainloop()

    @property
    def width(self) -> int:
        return self.__window.winfo_width()

    @width.setter
    def width(self, width: int):
        if width < 0:
            raise ValueError('Negative width')
        self.__window.geometry(f'{width}x{self.height}')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError('Negative KeyDisplayer.height')
        raise NotImplemented('Height cannot be set at the moment...')
        # TODO: to be implemented, this must resize all children of the window

    def show_key(self, key: Union[keyboard.Key, keyboard.KeyCode, None]):
        try:
            photo_image: ImageTk.PhotoImage = ImageManager.open_key_image(key)
        except (ImageAlreadyOpened, ValueError, FileNotFoundError) as exception:
            print(exception)
            return
        image_width = photo_image.width()
        image_label = ttk.Label(self.__window, image = photo_image, borderwidth=0)
        self.__labels[key] = image_label
        # TODO: test with the order of the following instructions
        self.width += image_width
        image_label.pack(side = tk.LEFT)
        self.__window.update() # TODO: check if necessary

    def hide_key(self, key: Union[keyboard.Key, keyboard.KeyCode, None], delay_seconds : float = 0):
        def hide_key_immediately():
            label : ttk.Label = self.__labels[key]
            label_width = label.winfo_width()
            label.destroy()
            del self.__labels[key]
            ImageManager.close_image(key)
            self.width -= label_width

        if delay_seconds:
            Timer(delay_seconds, hide_key_immediately).start()
        else:
            hide_key_immediately()
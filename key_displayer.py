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

    """
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
            image : ImageTk.PhotoImage = ImageManager.open_key_image(key)
        except ImageAlreadyOpened as already_opened:
            print(already_opened)
            return
        except FileNotFoundError as fnf:
            print(fnf)
            return
        except ValueError as ve:
            print(ve)
            return
        self.__update_window_width(image.width())
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
        image_width : int = ImageManager.get_opened_image(key).width()
        self.__update_window_width(-image_width)
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
    """
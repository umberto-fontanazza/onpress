from PIL import Image, ImageTk
from pynput import keyboard
from typing import Union
from pathlib import Path
from filenames_manager import FilenamesManager

filenames_manager = FilenamesManager()

class ImageManager:
    __buffer: dict[str, ImageTk.PhotoImage] = {}

    @staticmethod
    def open_key_image(key: Union[keyboard.Key, keyboard.KeyCode, None]) -> ImageTk.PhotoImage:
        path = ""
        if isinstance(key, keyboard.KeyCode):
            filename: str = filenames_manager.get_key_filename(key)
            path = str(Path.cwd() / 'assets' / 'keys' / filename)
        elif isinstance(key, keyboard.Key):
            filename: str = filenames_manager.get_special_key_filename(key)
            path = str(Path.cwd() / 'assets' / 'special_keys' / filename)
        return ImageManager.__open_image(path)

    @classmethod
    def closeImage(cls, key: Union[keyboard.Key, keyboard.KeyCode, None]):
        path = cls.__key_image_path(key)
        del cls.__buffer[path]

    @classmethod
    def __open_image(cls, path: str):
        if path in cls.__buffer:
            raise ImageAlreadyOpened(f'The image is already in the ImageManager buffer, path: {path}')
        image = Image.open(path)
        image.convert('RGBA') # used to keep transparency
        resized = image.resize((50,50))
        photo_image = ImageTk.PhotoImage(resized)
        cls.__buffer[path] = photo_image
        return photo_image

class ImageAlreadyOpened(Exception):
    pass
from PIL import Image, ImageTk
from pynput import keyboard
from typing import Union
from pathlib import Path
import json
from filenames_manager import FilenamesManager

filenames_manager = FilenamesManager()

class ImageManager:
    __buffer: dict[str, ImageTk.PhotoImage] = {}
    __filenames_map = None

    @staticmethod
    def open_key_image(key: Union[keyboard.Key, keyboard.KeyCode, None]) -> ImageTk.PhotoImage:
        path = ""
        if isinstance(key, keyboard.KeyCode):
            path = ImageManager.__key_image_path(key)
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

    @staticmethod
    def __key_image_path(key: keyboard.KeyCode) -> str:
        path: str = ''
        if key.char is None: raise ValueError('key.char is None')
        char: str = key.char
        filenames_map: dict[str, str] = ImageManager.get_filenames_map()
        filenames_map_keys = filenames_map["keys"]
        filename: str = filenames_map_keys[char]
        path = str(Path.cwd() / 'assets' / 'keys' / filename)
        return path

    @staticmethod
    def get_filenames_map() -> dict[str, dict[str, str]]:
        if ImageManager.__filenames_map is None:
            with open('./assets/filename_mappings.json', 'r', encoding='utf-8') as json_file:
                ImageManager.__filenames_map = json.load(json_file)
        return ImageManager.__filenames_map

class ImageAlreadyOpened(Exception):
    pass
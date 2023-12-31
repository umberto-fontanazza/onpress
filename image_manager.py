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
        if key is None:
            raise ValueError('Key is None')
        filename: str = filenames_manager.get_key_filename(key)
        subfolder = 'special_keys' if isinstance(key, keyboard.Key) else 'keys'
        path = Path.cwd() / 'assets' / subfolder / filename
        return ImageManager.__open_image(path)

    @classmethod
    def close_image(cls, key: Union[keyboard.Key, keyboard.KeyCode, None]):
        if key is None:
            raise ValueError('Key is None')
        filename: str = filenames_manager.get_key_filename(key)
        del cls.__buffer[filename]

    @classmethod
    def __open_image(cls, path: Path, heigt: int = 50) -> ImageTk.PhotoImage:
        if path.name in cls.__buffer:
            raise ImageAlreadyOpened(f'The image is already in the ImageManager buffer, filename: {path.name}')
        image = Image.open(path)
        image.convert('RGBA') # used to keep transparency
        image_aspect_ratio = image.width / image.height
        width = int(image_aspect_ratio * heigt)
        resized = image.resize((width,heigt))
        photo_image = ImageTk.PhotoImage(resized)
        cls.__buffer[path.name] = photo_image
        return photo_image

class ImageAlreadyOpened(Exception):
    pass
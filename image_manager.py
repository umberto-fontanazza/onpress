from PIL import Image, ImageTk
from pynput import keyboard
from typing import Union

class ImageManager:
    __buffer: dict[str, ImageTk.PhotoImage] = {}

    @staticmethod
    def open_key_image(key: Union[keyboard.Key, keyboard.KeyCode, None]) -> ImageTk.PhotoImage:
        if isinstance(key, keyboard.KeyCode):
            path = ImageManager.__key_image_path(key)
        elif isinstance(key, keyboard.Key):
            path = ImageManager.__key_special_image_path(key)
        else:
            path = ''
        return ImageManager.__open_image(path)

    @classmethod
    def __open_image(cls, path: str):
        try:
            image = Image.open(path)
        except Exception as e:
            print(e)
            print(f"Couldn't open image from path: {path}")
        image.resize((50,50))
        photo_image = ImageTk.PhotoImage(image)
        cls.__buffer[path] = photo_image
        return photo_image

    @staticmethod
    def __key_image_path(key: keyboard.KeyCode) -> str:
        path = ''
        char: str = key.char
        if char == 'a': path = 'letter_a.png'
        if char == 'b': path = 'letter_b.png'
        return path

    @staticmethod
    def __key_special_image_path(key: keyboard.Key) -> str:
        path = ''
        return path
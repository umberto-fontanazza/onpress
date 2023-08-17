from PIL import Image, ImageTk
from pynput import keyboard
from typing import Union

class ImageManager:
    __buffer = {}

    @staticmethod
    def open_key_image(key: Union[keyboard.Key, keyboard.KeyCode, None]) -> ImageTk.PhotoImage:
        # TODO: generalize for any keyboard key
        if type(key) == keyboard.KeyCode:
            char: str = key.char if key.char is not None else ''
        elif type(key) == keyboard.Key:
            return
        else:
            return
        path = './assets/letter_a.png' if char == 'a' else None
        path = './assets/letter_b.png' if char == 'b' else path
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

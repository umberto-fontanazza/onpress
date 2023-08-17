from PIL import Image, ImageTk

class ImageManager:
    __buffer = {}

    @classmethod
    def open_key_image(cls, char: str) -> ImageTk.PhotoImage:
        # TODO: generalize for any keyboard key
        path = './assets/letter_a.png' if char == 'a' else None
        path = './assets/letter_b.png' if char == 'b' else path
        if not path: raise(ValueError(f"Couldn't find a path for letter {char}"))
        image = Image.open(path)
        photo_image = ImageTk.PhotoImage(image)
        cls.__buffer[path] = photo_image
        return photo_image
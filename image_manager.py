from PIL import Image, ImageTk
from pynput import keyboard
from typing import Union
from pathlib import Path
import json

class ImageManager:
    __buffer: dict[str, ImageTk.PhotoImage] = {}
    __filenames_map = None

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
        image = Image.open(path)
        image.convert('RGBA') # used to keep transparency
        image.resize((50,50))
        photo_image = ImageTk.PhotoImage(image)
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
    def __key_special_image_path(key: keyboard.Key) -> str:
        path: str = ''
        filenames_map: dict[str, str] = ImageManager.get_filenames_map()
        filenames_map_special = filenames_map["special_keys"]
        if key is keyboard.Key.alt:
            filename = filenames_map_special["alt/option"]
        elif key is keyboard.Key.alt_l:
            filename = filenames_map_special["alt/option"]
        elif key is keyboard.Key.alt_r:
            filename = filenames_map_special["alt/option"]
        elif key is keyboard.Key.alt_gr:
            filename = filenames_map_special["alt/option"]
        elif key is keyboard.Key.backspace:
            filename = filenames_map_special["backspace"]
        elif key is keyboard.Key.caps_lock:
            filename = filenames_map_special["caps_lock"]
        elif key is keyboard.Key.cmd:
            filename = filenames_map_special["cmd"]
        elif key is keyboard.Key.cmd_l:
            filename = filenames_map_special["cmd"]
        elif key is keyboard.Key.cmd_r:
            filename = filenames_map_special["cmd"]
        elif key is keyboard.Key.ctrl:
            filename = filenames_map_special["ctrl"]
        elif key is keyboard.Key.ctrl_l:
            filename = filenames_map_special["ctrl"]
        elif key is keyboard.Key.ctrl_r:
            filename = filenames_map_special["ctrl"]
        elif key is keyboard.Key.delete:
            filename = filenames_map_special["delete"]
        elif key is keyboard.Key.down:
            filename = filenames_map_special["down"]
        elif key is keyboard.Key.end:
            filename = filenames_map_special["end"]
        elif key is keyboard.Key.enter:
            filename = filenames_map_special["enter"]
        elif key is keyboard.Key.esc:
            filename = filenames_map_special["esc"]
        elif key is keyboard.Key.f1:
            filename = filenames_map_special["f1"]
        elif key is keyboard.Key.f2:
            filename = filenames_map_special["f2"]
        elif key is keyboard.Key.f3:
            filename = filenames_map_special["f3"]
        elif key is keyboard.Key.f4:
            filename = filenames_map_special["f4"]
        elif key is keyboard.Key.f5:
            filename = filenames_map_special["f5"]
        elif key is keyboard.Key.f6:
            filename = filenames_map_special["f6"]
        elif key is keyboard.Key.f7:
            filename = filenames_map_special["f7"]
        elif key is keyboard.Key.f8:
            filename = filenames_map_special["f8"]
        elif key is keyboard.Key.f9:
            filename = filenames_map_special["f9"]
        elif key is keyboard.Key.f10:
            filename = filenames_map_special["f10"]
        elif key is keyboard.Key.f11:
            filename = filenames_map_special["f11"]
        elif key is keyboard.Key.f12:
            filename = filenames_map_special["f12"]
        elif key is keyboard.Key.f13:
            filename = filenames_map_special["f13"]
        elif key is keyboard.Key.f14:
            filename = filenames_map_special["f14"]
        elif key is keyboard.Key.f15:
            filename = filenames_map_special["f15"]
        elif key is keyboard.Key.f16:
            filename = filenames_map_special["f16"]
        elif key is keyboard.Key.f17:
            filename = filenames_map_special["f17"]
        elif key is keyboard.Key.f18:
            filename = filenames_map_special["f18"]
        elif key is keyboard.Key.f19:
            filename = filenames_map_special["f19"]
        elif key is keyboard.Key.f20:
            filename = filenames_map_special["f20"]
        elif key is keyboard.Key.home:
            filename = filenames_map_special["home"]
        elif key is keyboard.Key.left:
            filename = filenames_map_special["left"]
        elif key is keyboard.Key.page_down:
            filename = filenames_map_special["page_down"]
        elif key is keyboard.Key.page_up:
            filename = filenames_map_special["page_up"]
        elif key is keyboard.Key.right:
            filename = filenames_map_special["right"]
        elif key is keyboard.Key.shift:
            filename = filenames_map_special["shift"]
        elif key is keyboard.Key.shift_l:
            filename = filenames_map_special["shift"]
        elif key is keyboard.Key.shift_r:
            filename = filenames_map_special["shift"]
        elif key is keyboard.Key.space:
            filename = filenames_map_special["space"]
        elif key is keyboard.Key.tab:
            filename = filenames_map_special["tab"]
        elif key is keyboard.Key.up:
            filename = filenames_map_special["up"]
        elif key is keyboard.Key.media_play_pause:
            filename = filenames_map_special["media_paly_pause"]
        elif key is keyboard.Key.media_volume_mute:
            filename = filenames_map_special["media_volume_mute"]
        elif key is keyboard.Key.media_volume_down:
            filename = filenames_map_special["media_volume_down"]
        elif key is keyboard.Key.media_volume_up:
            filename = filenames_map_special["media_volume_up"]
        elif key is keyboard.Key.media_previous:
            filename = filenames_map_special["media_previous"]
        elif key is keyboard.Key.media_next:
            filename = filenames_map_special["media_next"]
        elif key is keyboard.Key.insert:
            filename = filenames_map_special["insert"]
        elif key is keyboard.Key.menu:
            filename = filenames_map_special["menu"]
        elif key is keyboard.Key.num_lock:
            filename = filenames_map_special["num_lock"]
        elif key is keyboard.Key.pause:
            filename = filenames_map_special["pause"]
        elif key is keyboard.Key.print_screen:
            filename = filenames_map_special["print_screen"]
        elif key is keyboard.Key.scroll_lock:
            filename = filenames_map_special["scroll_lock"]
        else:
            filename = ''
        path = str(Path.cwd() / 'assets' / 'special_keys' / filename)
        return path

    @staticmethod
    def get_filenames_map() -> dict[str, dict[str, str]]:
        if ImageManager.__filenames_map is None:
            with open('./assets/filename_mappings.json', 'r', encoding='utf-8') as json_file:
                ImageManager.__filenames_map = json.load(json_file)
        return ImageManager.__filenames_map
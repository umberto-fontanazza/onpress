from typing import Union
from pynput import keyboard

class FilenamesManager:
    __instance  = None
    __initialized = False
    __special_keys_filenames: dict[keyboard.Key, str] = {
        keyboard.Key.alt: "",
        keyboard.Key.alt_l: "",
        keyboard.Key.alt_r: "",
        keyboard.Key.alt_gr: "",
        keyboard.Key.backspace: "computer_key_Backspace_T.png",
        keyboard.Key.caps_lock: "computer_key_Caps_Lock_T.png",
        keyboard.Key.cmd: "",
        keyboard.Key.cmd_l: "",
        keyboard.Key.cmd_r: "",
        keyboard.Key.ctrl: "computer_key_Ctrl_T.png",
        keyboard.Key.ctrl_l: "computer_key_Ctrl_T.png",
        keyboard.Key.ctrl_r: "computer_key_Ctrl_T.png",
        keyboard.Key.delete: "computer_key_Delete_T.png",
        keyboard.Key.down: "computer_key_Arrow_Down_T.png",
        keyboard.Key.end: "computer_key_End_T.png",
        keyboard.Key.enter: "computer_key_Enter_T.png",
        keyboard.Key.esc: "computer_key_Esc_T.png",
        keyboard.Key.f1: "computer_key_F1_T.png",
        keyboard.Key.f2: "computer_key_F2_T.png",
        keyboard.Key.f3: "computer_key_F3_T.png",
        keyboard.Key.f4: "computer_key_F4_T.png",
        keyboard.Key.f5: "computer_key_F5_T.png",
        keyboard.Key.f6: "computer_key_F6_T.png",
        keyboard.Key.f7: "computer_key_F7_T.png",
        keyboard.Key.f8: "computer_key_F8_T.png",
        keyboard.Key.f9: "computer_key_F9_T.png",
        keyboard.Key.f10: "computer_key_F10_T.png",
        keyboard.Key.f11: "computer_key_F11_T.png",
        keyboard.Key.f12: "computer_key_F12_T.png",
        keyboard.Key.f13: "",
        keyboard.Key.f14: "",
        keyboard.Key.f15: "",
        keyboard.Key.f16: "",
        keyboard.Key.f17: "",
        keyboard.Key.f18: "",
        keyboard.Key.f19: "",
        keyboard.Key.f20: "",
        keyboard.Key.home: "computer_key_Home_T.png",
        keyboard.Key.left: "computer_key_Arrow_Left_T.png",
        keyboard.Key.page_down: "computer_key_Page_Down_T.png",
        keyboard.Key.page_up: "computer_key_Page_Up_T.png",
        keyboard.Key.right: "computer_key_Arrow_Right_T.png",
        keyboard.Key.shift: "computer_key_Shift_T.png",
        keyboard.Key.shift_l: "computer_key_Shift_T.png",
        keyboard.Key.shift_r: "computer_key_Shift_T.png",
        keyboard.Key.space: "computer_key_Space_bar_T.png",
        keyboard.Key.tab: "computer_key_Tab_T.png",
        keyboard.Key.up: "computer_key_Arrow_Up_T.png",
        keyboard.Key.media_play_pause: "",
        keyboard.Key.media_volume_mute: "",
        keyboard.Key.media_volume_down: "",
        keyboard.Key.media_volume_up: "",
        keyboard.Key.media_previous: "",
        keyboard.Key.media_next: "",
        # Checking keyboard.Key definitions the following keys may not
        # be defined on all platforms: insert, menu, num_lock, pause, print_screen, scroll_lock
    }

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__check_possibly_undefined_keys()
        self.__initialized = True

    def __check_possibly_undefined_keys(self):
        key_filename_pairs = {
            "insert": "computer_key_Insert_T.png",
            "menu": "",
            "num_lock": "computer_key_Num_Lock_T.png",
            "pause": "computer_key_Pause_Break_T.png",
            "print_screen": "computer_key_Print_Screen_T.png",
            "scroll_lock": "computer_key_Scroll_Lock_T.png"
        }

        for key_name in key_filename_pairs:
            filename = key_filename_pairs[key_name]
            if not hasattr(keyboard.Key, key_name):
                print(f"This platform doesn't support key: {key_name}")
                continue
            key : keyboard.Key = keyboard.Key[key_name]
            self.__special_keys_filenames[key] = filename

    def get_key_filename(self, key: Union[keyboard.KeyCode, keyboard.Key]) -> str:
        if isinstance(key, keyboard.KeyCode):
            if key.char is None: raise ValueError('key.char is None')
            letter = key.char
            return f'computer_key_{letter.upper()}_T.png'
        elif isinstance(key, keyboard.Key):
            return self.__special_keys_filenames[key]
        else:
            raise TypeError('Key must be either a keyboard.KeyCode or a keyboard.Key')
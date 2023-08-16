import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from key_displayer import KeyDisplayer

def add_column(window: tk.Tk, weight: int = 1):
    global key_image_tk
    columns_count: int = window.grid_size()[0]
    new_frame = ttk.Frame(window, style='green.TFrame')
    new_frame.grid(row=0, column=columns_count, sticky='nswe')
    window.columnconfigure(columns_count, weight=weight)
    # adding the image
    key_image = Image.open('letter_a.png').resize((50,50))
    key_image_tk = ImageTk.PhotoImage(key_image)
    canvas = tk.Canvas(new_frame, background='black')
    canvas.grid(row=0, column=0, sticky='nsew')
    canvas.create_image((0,0),image=key_image_tk, anchor='nw')

def main():
    kd = KeyDisplayer()

if __name__ == '__main__':
    main()
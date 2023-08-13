import tkinter as tk
from tkinter import ttk

def add_column(window: tk.Tk, weight: int = 1):
    columns_count: int = window.grid_size()[0]
    new_frame = ttk.Frame(window, style='green.TFrame')
    new_frame.grid(row=0, column=columns_count, sticky='nswe')
    window.columnconfigure(columns_count, weight=weight)

def main():
    window = tk.Tk()
    window.title('Main window')
    window.rowconfigure(0, weight=1)
    window.columnconfigure((0,1), weight=1)
    window.geometry('450x100')
    window.geometry('-100+100') # move window to the top right side

    s = ttk.Style(window)
    s.theme_use('classic') # https://stackoverflow.com/questions/23750141/tkinter-ttk-widgets-ignoring-background-color
    s.configure('TFrame', background='red')
    s.configure('blue.TFrame', background='blue')
    s.configure('green.TFrame', background='green')
    s.configure('TLabel', background='blue')

    frame = ttk.Frame(window)
    frame.grid(row=0, sticky='nswe')

    blue_frame = ttk.Frame(window, style='blue.TFrame')
    blue_frame.grid(row=0, column=1, sticky='nswe')

    label = ttk.Label(window, text='Label')
    label.grid(row=0)


    # this is just for testing
    root = tk.Tk()
    root.title = 'Callback test'

    button_callback = lambda : add_column(window = window)
    button = ttk.Button(root, text='Press me', command=button_callback)
    button.grid()

    window.mainloop()

if __name__ == '__main__':
    main()
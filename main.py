import tkinter as tk

from authentication import render_register
from helpers import clear_screen
import os


def render_main_screen(screen: tk.Tk):
    tk.Button(screen, text='Login', background='green', foreground='white', command=lambda: print('Clicked')).grid(row=0, column=0)
    tk.Button(
        screen, text='Register', foreground='black', background='yellow',
        command=lambda: render_register(screen, on_success=render_main_screen)
    ).grid(row=0, column=1)


if __name__ == '__main__':
    window = tk.Tk()
    window.title = 'My App'
    window.geometry('600x600')

    render_main_screen(window)

    window.mainloop()
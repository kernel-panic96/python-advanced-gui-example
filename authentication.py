import os
import tkinter as tk

from helpers import clear_screen


def register(**user):
    # TODO: handle already existing usernames
    with open(os.path.join('db', 'user_store.txt'), 'a') as f:
        f.write(f'{user["username"]} - {user["password"]}\n')


def render_register(screen: tk.Tk, on_success):
    clear_screen(screen)
    inputs = [
        ('username', tk.Entry(screen)),
        ('password', tk.Entry(screen)),
        ('first_name', tk.Entry(screen)),
        ('last_name', tk.Entry(screen)),
    ]

    for idx, (label, input_widget) in enumerate(inputs):
        input_widget.grid(row=idx, column=0)


    def on_click():
        error = register(**{user_attribute: widget.get() for (user_attribute, widget) in inputs})

        if not error:
            clear_screen(screen)
            on_success(screen)
        else:
            tk.Label(screen, text=error, background='red', foreground='white').grid(row=5, column=0)

    tk.Button(
        screen,
        text='Submit',
        command=on_click
    ).grid(row=len(inputs), column=1)
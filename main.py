import tkinter as tk

def clear_screen(screen: tk.Tk):
    for element in screen.grid_slaves():
        element.destroy()

if __name__ == '__main__':
    window = tk.Tk()
    window.title = 'My App'
    window.geometry('600x600')

    tk.Button(window, text='Login', background='green', foreground='white', command=lambda: print('Clicked')).grid(row=0, column=0)
    tk.Button(window, text='Register', foreground='black', background='yellow', command=lambda: print('Clicked')).grid(row=0, column=1)

    tk.Button(window, text='Clear screen', command=lambda: clear_screen(window)).grid(row=1, column=1)

    window.mainloop()



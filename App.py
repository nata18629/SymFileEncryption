import tkinter as tk

from View import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Symmetric File Encryption")
        view = View(self)
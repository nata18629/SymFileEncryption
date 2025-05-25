import tkinter as tk

from Controller import Controller
from Model import Model
from View import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Symmetric File Encryption")
        view = View(self)
        model = Model()
        controller = Controller(model, view)
        view.set_controller(controller)
        view.add_interface()
        view.grid(row=0, column=0, padx=20, pady=20)
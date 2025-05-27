import tkinter as tk

from Controller import Controller
from EncryptionView import EncryptionView
from Model import Model
from MainView import MainView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x450")
        self.title("Symmetric File Encryption")

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)

        view = MainView(self)
        encryption_view = EncryptionView(self)
        model = Model()
        controller = Controller(model, view, encryption_view)
        view.set_controller(controller)
        encryption_view.set_controller(controller)
        controller.change_to_main_view()

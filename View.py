import tkinter as tk
from tkinter import ttk

padding_y = 20

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.encrypt_button = ttk.Button(self, text="ENCRYPT", width=25)
        self.encrypt_button.pack(pady=padding_y)
        self.decrypt_button = ttk.Button(self, text="DECRYPT", width=25)
        self.decrypt_button.pack(pady=padding_y)


    def choose_file_clicked(self):
        pass

    def encrypt_clicked(self):
        pass

    def decrypt_clicked(self):
        pass
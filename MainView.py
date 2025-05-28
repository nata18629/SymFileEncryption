from tkinter import ttk
from Constants import *

class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="20 20 20 20")
        self.controller = None
        self.columnconfigure(0, weight=1)

    def main_view(self):
        ttk.Label(self, text="Symmetric File Encryption App", font=("Helvetica", 18, "bold")).grid(row=0, column=0, pady=padding_y, sticky='n')
        ttk.Button(self, text="🔐 Encryption", width=button_width, command=self.encryption_chosen).grid(row=2, column=0, pady=padding_y, padx=padding_x, sticky="ew")
        ttk.Button(self, text="🔓 Decryption", width=button_width, command=self.decryption_chosen).grid(row=3, column=0, pady=padding_y, padx=padding_x, sticky="ew")

    def set_controller(self, controller):
        self.controller = controller

    def encryption_chosen(self):
        self.controller.change_to_encryption('ENC')

    def decryption_chosen(self):
        self.controller.change_to_encryption('DEC')

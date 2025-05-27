from tkinter import ttk
from Constants import *


class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        #self.grid(row=0, column=0, padx=20, pady=20)

    def main_view(self):
        ttk.Button(self, text="ENCRYPTION", width=button_width, command=self.encryption_chosen).pack(pady=padding_y, fill='x')
        ttk.Button(self, text="DECRYPTION", width=button_width, command=self.decryption_chosen).pack(pady=padding_y, fill='x')

    def set_controller(self, controller):
        self.controller = controller

    def encryption_chosen(self):
        self.controller.change_to_encryption('ENC')

    def decryption_chosen(self):
        self.controller.change_to_encryption('DEC')
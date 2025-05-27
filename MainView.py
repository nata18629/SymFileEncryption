from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

padding_x = 20
padding_y = 20

class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        #self.grid(row=0, column=0, padx=20, pady=20)

    def main_view(self):
        ttk.Button(self, text="ENCRYPTION", width=25, command=self.encryption_chosen).pack(pady=padding_y)
        ttk.Button(self, text="DECRYPTION", width=25, command=self.decryption_chosen).pack(pady=padding_y)

    def set_controller(self, controller):
        self.controller = controller

    def encryption_chosen(self):
        self.controller.change_to_encryption('ENC')

    def decryption_chosen(self):
        self.controller.change_to_encryption('DEC')
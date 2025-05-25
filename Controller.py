import tkinter as tk

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.encryption_option = tk.StringVar(value='ENC')
        self.encryption_mode = tk.StringVar(value='ECB')

    def save_file(self, file):
        self.model.file = file

    def run_model(self):
        if self.model.file is None:
            self.view.error_file_message()
            return
        self.model.encryption_option = self.encryption_option.get()
        self.model.encryption_mode = self.encryption_mode.get()
        self.model.encrypt_file()
import tkinter as tk

class Controller:
    def __init__(self, model, view, encryption_view):
        self.model = model
        self.main_view = view
        self.encryption_view = encryption_view
        self.encryption_option = tk.StringVar(value='ENC')
        self.encryption_mode = tk.StringVar(value='ECB')

    def save_file(self, file):
        self.model.file = file

    def save_key(self, file):
        pass


    def change_to_encryption(self, mode):
        self.delete_frame(self.main_view)
        self.encryption_view.grid(row=0, column=0, padx=20, pady=20)
        if mode == 'ENC':
            self.encryption_view.encryption_view()
        else:
            self.encryption_view.decryption_view()

    def change_to_main_view(self):
        self.delete_frame(self.encryption_view)
        self.main_view.grid(row=0, column=0, padx=20, pady=20)
        self.main_view.main_view()


    def run_model(self):
        if self.model.file is None:
            self.main_view.error_file_message()
            return
        self.model.encryption_option = self.encryption_option.get()
        self.model.encryption_mode = self.encryption_mode.get()
        self.model.encrypt_file()

    def delete_frame(self, frame):
        widgets = frame.winfo_children()
        for item in widgets:
            item.pack_forget()
        frame.grid_forget()
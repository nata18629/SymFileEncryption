from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from Constants import *


class EncryptionView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        #self.grid(row=0, column=0, padx=20, pady=20)

    def set_controller(self, controller):
        self.controller = controller

    def encryption_view(self):
        ttk.Label(self, text="🔐 ENCRYPT A FILE", font=("Helvetica", 16, "bold")).pack(pady=padding_y)
        frame = ttk.Frame(self)
        ttk.Button(frame, text="GENERATE KEY", width=button_width, command=self.generate_key_clicked).pack(pady=padding_y, side='right')
        ttk.Button(frame, text="CHOOSE KEY", width=button_width, command=self.choose_key_clicked).pack(pady=padding_y, side='right')
        frame.pack()
        self.add_interface()


    def decryption_view(self):
        ttk.Label(self, text="🔓 DECRYPT A FILE", font=("Helvetica", 16, "bold")).pack(pady=padding_y)
        ttk.Button(self, text="CHOOSE KEY", width=button_width, command=self.choose_key_clicked).pack(pady=padding_y)
        self.add_interface()

    def add_interface(self):
        ttk.Button(self, text="CHOOSE FILE", width=button_width, command=self.choose_file_clicked).pack(pady=padding_y)
        ttk.Label(self, text="Encryption Mode:").pack(pady=padding_y)
        ttk.Combobox(self, textvariable=self.controller.encryption_mode, values=["ECB", "CBC", "CTR"]).pack(pady=10)
        ttk.Button(self, text="PROCEED", width=button_width, command=self.proceed_clicked).pack(pady=padding_y, side='right')
        ttk.Button(self, text="GO BACK", width=button_width, command=self.go_back).pack(pady=padding_y, side='right')
    def choose_file_clicked(self):
        self.controller.save_file(askopenfilename())

    def choose_key_clicked(self):
        self.controller.save_key(askopenfilename())

    def generate_key_clicked(self):
        self.controller.save_generated_key()

    def proceed_clicked(self):
        self.controller.run_model()

    def error_file_message(self):
        showinfo(title='ERROR', message="Please choose a correct file")

    def error_key_message(self):
        showinfo(title='ERROR', message="Please choose a correct key")

    def error_message(self, message):
        showinfo(title='ERROR', message=message)
    def go_back(self):
        self.controller.change_to_main_view()

    def success_message(self):
        showinfo(title='SUCCESS', message="Your file has been saved")

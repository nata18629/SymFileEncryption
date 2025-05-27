from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

padding_x = 20
padding_y = 20
button_width = 25

class EncryptionView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        #self.grid(row=0, column=0, padx=20, pady=20)

    def set_controller(self, controller):
        self.controller = controller

    def encryption_view(self):
        ttk.Label(self, text="ENCRYPT A FILE").pack(pady=padding_y)
        ttk.Button(self, text="GENERATE KEY", width=button_width, command=self.choose_key_clicked).pack(pady=padding_y)
        self.add_interface()


    def decryption_view(self):
        ttk.Label(self, text="DECRYPT A FILE").pack(pady=padding_y)
        self.add_interface()

    def add_interface(self):
        ttk.Button(self, text="CHOOSE KEY", width=button_width, command=self.choose_key_clicked).pack(pady=padding_y)
        ttk.Button(self, text="CHOOSE FILE", width=button_width, command=self.choose_file_clicked).pack(pady=padding_y)
        ttk.Combobox(self, textvariable=self.controller.encryption_mode, values=["ECB", "CBC", "CTR"]).pack(pady=10)
        ttk.Button(self, text="PROCEED", width=button_width, command=self.choose_key_clicked).pack(pady=padding_y)
        ttk.Button(self, text="GO BACK", width=button_width, command=self.go_back).pack(pady=padding_y)
    def choose_file_clicked(self):
        self.controller.save_file(askopenfilename())

    def choose_key_clicked(self):
        self.controller.save_key(askopenfilename())

    def generate_key_clicked(self):
        self.controller.save_key()

    def proceed_clicked(self):
        self.controller.run_model()

    def error_file_message(self):
        showinfo(title='ERROR', message="Please choose a correct file")

    def go_back(self):
        self.controller.change_to_main_view()

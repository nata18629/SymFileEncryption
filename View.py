from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

padding_x = 20
padding_y = 20

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)

    def add_interface(self):
        choose_file_button = ttk.Button(self, text="CHOOSE FILE", width=25, command=self.choose_file_clicked)
        choose_file_button.pack(pady=padding_y)

        if_encryption = ttk.Radiobutton(self.frame1, text="ENCRYPTION", value='ENC', variable=self.controller.encryption_option)
        if_encryption.grid(padx=padding_x, pady=padding_y, column=0, row=0)
        if_decryption = ttk.Radiobutton(self.frame1, text="DECRYPTION", value='DEC', variable=self.controller.encryption_option)
        if_decryption.grid(padx=padding_x, pady=padding_y, column=1, row=0)
        self.frame1.pack()

        modes = (('ECB', 'ECB'), ('CBC', 'CBC'), ('CTR', 'CTR'))
        i = 0
        for mode in modes:
            mode_choice = ttk.Radiobutton(self.frame2, text=mode[0], value=mode[1], variable=self.controller.encryption_mode)
            mode_choice.grid(padx=padding_x, pady=padding_y, column=i, row=0)
            i += 1
        self.frame2.pack()

        proceed_button = ttk.Button(self, text="PROCEED", width=25, command=self.proceed_clicked)
        proceed_button.pack(pady=padding_y)

    def set_controller(self, controller):
        self.controller = controller

    def choose_file_clicked(self):
        self.controller.save_file(askopenfilename())

    def proceed_clicked(self):
        self.controller.run_model()

    def error_file_message(self):
        showinfo(title='ERROR', message="Please choose a correct file")
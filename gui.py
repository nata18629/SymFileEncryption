from tkinter import *
from tkinter import ttk


padding_y = 20

root = Tk()
root.geometry("400x400")
root.title("Symmetric File Encryption")
encrypt_button = Button(root, text="ENCRYPT", width=25)
encrypt_button.pack(pady=padding_y)
decrypt_button = Button(root, text="DECRYPT", width=25)
decrypt_button.pack(pady=padding_y)


root.mainloop()
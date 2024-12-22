import tkinter as tk



# class CustomButton(tk.Button):
#     def __init__(self, master, text, command):
#         super().__init__(master, text=text, command=command)
#         self.pack(pady=10)

def CustomButton(master, text, command):
    button = tk.Button(master, text=text, command=command)
    button.pack(pady=10)
    return button
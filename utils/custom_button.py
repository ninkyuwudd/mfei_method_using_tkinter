
from tkinter import ttk



# class CustomButton(tk.Button):
#     def __init__(self, master, text, command):
#         super().__init__(master, text=text, command=command)
#         self.grid(pady=10)

def CustomButton(master, text, command, color = "primary"):
    button = ttk.Button(master, text=text, command=command,width=20,bootstyle=color)
    button.grid(pady=10)
    # button.config(state=tk.DISABLED)
    return button
import tkinter as tk



# class CustomButton(tk.Button):
#     def __init__(self, master, text, command):
#         super().__init__(master, text=text, command=command)
#         self.grid(pady=10)

def CustomButton(master, text, command):
    button = tk.Button(master, text=text, command=command,width=20)
    button.grid(pady=10)
    # button.config(state=tk.DISABLED)
    return button
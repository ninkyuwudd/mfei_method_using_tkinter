import tkinter as tk
from execute import executeProccess
from input_ouput_handle import *

def main():
    root = tk.Tk()
    root.title("Basic Tkinter App")
    
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=20)

    create_directory_button(root, "Choose Directory")
    buttonRemove = remove_folder(root, "uploads")
    executeProccess(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
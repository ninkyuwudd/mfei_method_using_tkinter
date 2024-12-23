from tkinter import *
from execute import executeProccess
from input_ouput_handle import *

def main():
    root = Tk()
    root.title("Gait Recognition")
    root.geometry("400x400")
    root.iconbitmap("assets/icon_walk.ico")

    pann_container = PanedWindow(root,orient="horizontal")
    pann_container.pack(fill=BOTH, expand=1)

 
    pann_container_left = PanedWindow(pann_container,bd=2,orient="vertical")
    pann_container.add(pann_container_left)
    pann_container_right = PanedWindow(pann_container,orient="vertical")
    pann_container.add(pann_container_right)
   
    
    label_frame01 = LabelFrame(pann_container_left)
    pann_container_left.add(label_frame01)

    label = Label(label_frame01, text="Unggah kumpulan frame siluet gaya berjalan anda", font=("Helvetica", 10))
    label.pack(pady=10)


    create_directory_button(label_frame01, "Choose Directory")
    remove_folder(label_frame01, "uploads")
    executeProccess(label_frame01)

    label = Label(pann_container_right, text="DISPLAY", font=("Helvetica", 10))
    label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
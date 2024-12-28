from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from execute import executeProccess
from input_ouput_handle import *


def main():
    root = Tk()
    root.configure(bg="#1e1e1f")
    root.title("Gait Recognition")
    root.geometry("800x550")
    root.iconbitmap("assets/icon_walk.ico")

    pann_container = PanedWindow(root, orient="horizontal", bg="#1e1e1f")
    pann_container.grid(sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

 
    pann_container_left = PanedWindow(pann_container,orient="vertical",bg="#1e1e1f")
    pann_container.add(pann_container_left)
    pann_container_right = PanedWindow(pann_container,orient="vertical",bg="#1e1e1f")
    pann_container.add(pann_container_right)

   
   
    style = ttk.Style()
    style.configure('Custom.TLabelframe', background='#2e2e2e')
    label_frame01 = ttk.LabelFrame(pann_container_left, text="Navigation Panel", bootstyle="dark", style='Custom.TLabelframe',padding=20)
    pann_container_left.add(label_frame01)



    # id untuk menghapus widget
    canvas_id = tk.StringVar()
    label_id = tk.StringVar()
    mfei_res_id = tk.StringVar()
    gr_animated_id = tk.StringVar()
    frame_input_file_idx = 0


    # Upload sequence data dari folder kita dan menampilkan animasi gaya berjalan
    create_directory_button(label_frame01, pann_container_right,canvas_id,mfei_res_id,"Choose Directory",frame_input_file_idx,gr_animated_id,label_id)

    # menghapus data folder yang sudah di upload
    remove_folder(label_frame01,pann_container_right,canvas_id, "uploads", mfei_res_id,gr_animated_id,label_id)

    # Memproses data yang sudah di upload
    executeProccess(label_frame01,pann_container_right,mfei_res_id,label_id,gr_animated_id)

   
    
    root.mainloop()

if __name__ == "__main__":
    main()
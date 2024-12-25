
from tkinter import Label, PanedWindow
from tkinter.ttk import Labelframe
from PIL import Image, ImageTk

def show_image_on_tkinter(root,mfei_res_id, image_array):


    # pann_container_right_bottom = PanedWindow(root,bd=2,bg="#1e1e1f",height=200,width=200)
    # root.add(pann_container_right_bottom)


    # lbl_frame = Labelframe(root, text="Hasil",style='Custom.TLabelframe')
    # root.add(lbl_frame) 
    # Konversi NumPy array ke format Image
    image = Image.fromarray(image_array)

    # Konversi Image ke PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Tampilkan gambar di tkinter menggunakan Label
    label = Label(root, image=photo)
    label.image = photo  # Simpan referensi agar gambar tidak hilang
    # root.add(label)
    label.grid(row=2,column=1,padx=10,pady=10)
    mfei_res_id.set(label)
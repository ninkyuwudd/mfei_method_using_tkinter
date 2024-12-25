import os
from tkinter import Canvas, PanedWindow
from tkinter import ttk
from tkinter.ttk import Labelframe
from PIL import Image, ImageTk
import cv2
import tkinter as tk



def play_video_from_frames(frame_folder, canvas, root, delay=33):
    """Play video from frame sequence stored in a folder."""
    # Get all frame filenames and sort numerically
    frame_files = sorted(os.listdir(frame_folder), key=lambda x: int(x.split('.')[0]))
    frame_index = 0
    
    def update_frame():
        nonlocal frame_index
        
        # Loop through frames
        if frame_index < len(frame_files):
            frame_path = os.path.join(frame_folder, frame_files[frame_index])
            frame = cv2.imread(frame_path)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert to ImageTk format for Tkinter display
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Display the frame on the canvas
            canvas.image = imgtk  # Keep reference to avoid garbage collection
            canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            
            frame_index += 1
        else:
            frame_index = 0  # Restart the video loop
        
        root.after(delay, update_frame)  # Schedule the next frame
            
    update_frame()


def display_video(root, canvas_id,frame_folder):

    label = ttk.Label(root, text="Gait Input", font=("Helvetica", 10))
    label.grid(row=0,columnspan=2,sticky="ew") 


    first_frame = cv2.imread(os.path.join(frame_folder, sorted(os.listdir(frame_folder))[0]))
    height, width, _ = first_frame.shape


    # pann_container_right_top = PanedWindow(root,bd=2,bg="#1e1e1f")
    # root.add(pann_container_right_top)

    # style = ttk.Style()
    # style.configure('Custom.TLabelframe', background='#2e2e2e',)
    # ori_frame = Labelframe(root, text="Original Gait",style='Custom.TLabelframe')
    # root.add(ori_frame)
    # Canvas for video display
    canvas = Canvas(root, width=width - 20, height=height - 20, bg='black')
    # root.add(canvas)
    canvas.grid(columnspan=2)
    canvas_id.set(str(canvas))
    print(str(canvas))

    # Play video
    play_video_from_frames(frame_folder, canvas, root)




def display_ndarray_frames_in_sequence(root, canvas, frames, delay=100):
    """
    Menampilkan urutan frame pada canvas sebagai animasi.
    
    Args:
        root: Tkinter root window.
        canvas: Tkinter Canvas widget.
        frames: List of numpy.ndarray (grayscale images).
        delay: Waktu delay antar frame dalam milidetik (default 100 ms).
    """
    def update_frame(idx):
        if idx < len(frames):
            # Konversi frame numpy.ndarray ke format Tkinter (ImageTk)
            frame = frames[idx]
            img = ImageTk.PhotoImage(Image.fromarray(frame).convert("L"))
            
            # Perbarui canvas dengan gambar baru
            canvas.image = img  # Simpan referensi ke gambar
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            
            # Jadwalkan frame berikutnya
            root.after(delay, update_frame, idx + 1)

    # Mulai menampilkan frame dari indeks pertama
    update_frame(0)

def show_ndarray_animation(aligned_frames,root):

    
    # Asumsi semua frame memiliki ukuran yang sama
    frame_height, frame_width = aligned_frames[0].shape
    
    # Membuat canvas dengan ukuran sesuai frame
    canvas = tk.Canvas(root, width=frame_width, height=frame_height)
    # root.add(canvas)
    canvas.grid(row=2,column=0,padx=10,pady=10)
    
    # Menampilkan animasi
    display_ndarray_frames_in_sequence(root, canvas, aligned_frames, delay=100)
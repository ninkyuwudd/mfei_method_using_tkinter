import tkinter as tk
from tkinter import filedialog
import os
import cv2
import shutil
from display_gait import display_video
from utils.custom_button import CustomButton


def load_images_from_folder(folder_path):
    images = []
    if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def check_and_remove_widget(parent, widget_name):
    """Cek apakah widget tertentu ada, dan hapus jika ditemukan."""
    for widget in parent.winfo_children():
        if str(widget) == widget_name:  # Periksa nama widget
            widget.destroy()
            print(f"Widget {widget_name} telah dihapus.")
            return
    print(f"Widget {widget_name} tidak ditemukan.")

def remove_and_clear_display_gait(root,widget_id):
    if os.path.exists("uploads"):
            for filename in os.listdir("uploads"):
                file_path = os.path.join("uploads", filename)
                os.remove(file_path)
            os.rmdir("uploads")

            check_and_remove_widget(root, widget_id)



def create_directory_button(root,second_root, canvas_id,text):
    def choose_directory():
        print(canvas_id.get())
        remove_and_clear_display_gait(second_root,canvas_id.get())

        directory = filedialog.askdirectory()
        if directory:
            # print("Directory:", directory)
            uploads_dir = os.path.join(os.getcwd(), "uploads")
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            for img in image_files:
                img_src = os.path.join(directory, img)
                new_img_path = os.path.join(uploads_dir, img)
                # print("Copying", img_src, "to", new_img_path)
                shutil.copy(img_src, new_img_path)
        
        def count_files_in_directory(directory):
            return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

        def count_subdirectories_in_directory(directory):
            return len([name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))])

        directory_path = "uploads"
        num_files = count_files_in_directory(directory_path)
        num_subdirectories = count_subdirectories_in_directory(directory_path)

        # print(f"Number of files in '{directory_path}': {num_files}")
        # print(f"Number of subdirectories in '{directory_path}': {num_subdirectories}")

        if(num_files > 0):
            print("Displaying video...")
            display_video(second_root, canvas_id,"uploads")
    
    return CustomButton(root, text, choose_directory)


def remove_folder(root,folder_path):
    def remove():
        # Hapus folder dan isinya
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
        os.rmdir(folder_path)

    return CustomButton(root, "Remove data", remove)


def create_video_from_frames(frame_folder, output_video_path, fps=20):
    # Dapatkan daftar file frame dan urutkan
    frames = [f for f in os.listdir(frame_folder) if f.endswith('.png') or f.endswith('.jpg')]
    frames.sort()

    # Baca frame pertama untuk mendapatkan ukuran video
    first_frame_path = os.path.join(frame_folder, frames[0])
    first_frame = cv2.imread(first_frame_path)
    height, width, layers = first_frame.shape

    # Tentukan codec dan buat VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec untuk format .mp4
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Tulis setiap frame ke video
    for frame_name in frames:
        frame_path = os.path.join(frame_folder, frame_name)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)

    # Selesai menulis video
    video_writer.release()
    print(f"Video saved to {output_video_path}")


def extract_frames_from_video(video_path, output_folder):
    # Buat folder output jika belum ada

    os.makedirs(output_folder, exist_ok=True)

    # Buka video
    video_capture = cv2.VideoCapture(video_path)

    # Periksa apakah video berhasil dibuka
    if not video_capture.isOpened():
        message = f"Error: Tidak dapat membuka video {video_path}"
        return message

    frame_count = 0
    while True:
        # Baca frame dari video
        ret, frame = video_capture.read()

        # Jika tidak ada frame lagi, keluar dari loop
        if not ret:
            break

        # Simpan frame sebagai gambar
        frame_filename = os.path.join(output_folder, f"{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Selesai memproses video
    video_capture.release()
    return f"Extracted {frame_count} frames to {output_folder}"


def check_input_video(request,app):
    if request.method == "POST":
        if "videoInput" not in request.files:
            return 'Is empty file'

        dataVideo = request.files['videoInput']

        if dataVideo.filename == "":
            return 'You not select any video'
        
        if dataVideo:

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], dataVideo.filename)
            dataVideo.save(file_path)
            result = extract_frames_from_video(file_path, "output_frame")
            return f'File  {file_path} and {result}'
        

        
frame_folder = 'E:/kuliah/skripsi/datavideo/casia/fn/fn02/0200' 
# create_video_from_frames(frame_folder, "output_video.mp4")
video_gait = "E:/kuliah/skripsi/code/mfei_method_using_tkinter/output_video.mp4"
# result = extract_frames_from_video(video_gait, "output_frame")
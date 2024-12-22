import tkinter as tk
from tkinter import filedialog
import os
import cv2
import shutil
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


def create_directory_button(root, text):
    def choose_directory():
        directory = filedialog.askdirectory()
        if directory:
            print("Directory:", directory)
            uploads_dir = os.path.join(os.getcwd(), "uploads")
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            for img in image_files:
                img_src = os.path.join(directory, img)
                new_img_path = os.path.join(uploads_dir, img)
                # print("Copying", img_src, "to", new_img_path)
                shutil.copy(img_src, new_img_path)
    
    return CustomButton(root, text, choose_directory)


def remove_folder(root,folder_path):
    def remove():
        # Hapus folder dan isinya
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
        os.rmdir(folder_path)

    return CustomButton(root, "Remove data", remove)
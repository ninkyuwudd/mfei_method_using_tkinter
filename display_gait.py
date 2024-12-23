import os
from tkinter import Canvas
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
    first_frame = cv2.imread(os.path.join(frame_folder, sorted(os.listdir(frame_folder))[0]))
    height, width, _ = first_frame.shape

    # Canvas for video display
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    canvas_id.set(str(canvas))
    print(str(canvas))

    # Play video
    play_video_from_frames(frame_folder, canvas, root)
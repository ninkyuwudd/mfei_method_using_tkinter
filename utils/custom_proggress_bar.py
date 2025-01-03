



import time
from tkinter import HORIZONTAL
from tkinter import ttk
from tkinter.ttk import Progressbar
import threading

from utils.custom_label import custom_label





def custom_progress_bar(root,text,label_id):
    lbl_frame_result = ttk.Labelframe(root,text="Recognition Result")
    lbl_frame_result.grid(row=0,column=1,padx=10,pady=10)
    label_id.set(lbl_frame_result)
    percent_label = ttk.Label(lbl_frame_result, text=f"{0}%", font=("Helvetica", 15))
    percent_label.grid(row=0,column=0,pady=10)
    proggress_bar = ttk.Progressbar(lbl_frame_result, orient=HORIZONTAL, length=150, mode='determinate',bootstyle = "success")
    proggress_bar.grid(row=0,column=1,pady=10)

    def update_progress():
        for i in range(90):
            proggress_bar['value'] = i
            percent_label['text'] = f"{i+5}%"
            lbl_frame_result.update_idletasks()
            time.sleep(0.001)
        
        time.sleep(1)
        proggress_bar.grid_forget()
        percent_label.grid_forget()
        custom_label(lbl_frame_result, text,label_id)
        
    

    threading.Thread(target=update_progress).start()
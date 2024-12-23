



import time
from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar
import threading

from utils.custom_label import custom_label





def custom_progress_bar(root,text,label_id):
    proggress_bar = Progressbar(root, orient=HORIZONTAL, length=150, mode='determinate')
    proggress_bar.pack(pady=10)

    def update_progress():
        for i in range(90):
            proggress_bar['value'] = i
            root.update_idletasks()
            time.sleep(0.001)
        
        time.sleep(1)
        proggress_bar.pack_forget()
        custom_label(root, text,label_id)
        
    

    threading.Thread(target=update_progress).start()
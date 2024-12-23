

from input_ouput_handle import load_images_from_folder, remove_folder

import pandas as pd

from method.method_hog import compute_hog
from method.method_mfei import execute_mfei
from method.method_pre_processing import normalize_silhouettes
from method.method_svc import clasification_data
from utils.custom_button import CustomButton
import numpy as np  
import os


def executeProccess(root):
    def runProggram():
 
        load_images = load_images_from_folder("uploads")
        normalize= normalize_silhouettes(load_images)
        mfei = execute_mfei(normalize) 
        hog = compute_hog(mfei)    
        faltten_hog = np.array(hog).flatten()
        if len(faltten_hog) > 0:
            df = pd.DataFrame([faltten_hog], columns=[f'feature_{i}' for i in range(len(faltten_hog))])
       
            
            # Menyimpan DataFrame ke file CSV
            df.to_csv("input_testing_data.csv", index=False)
            print(f"Hasil disimpan ke: input_testing_data.csv")
        else:
            print(f"Tidak ada data yang diproses")
        result = clasification_data()
        print(result)
        print("Data has been executed")
        # for filename in os.listdir("uploads"):
        #     file_path = os.path.join("uploads", filename)
        #     os.remove(file_path)
        # os.rmdir("uploads")
        # remove_folder(root,"uploads")
        
    return CustomButton(root, "Execute Data", runProggram)
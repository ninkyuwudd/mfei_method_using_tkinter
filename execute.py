

from input_ouput_handle import load_images_from_folder, remove_folder
from pre_processing import normalize_silhouettes
from utils.custom_button import CustomButton


def executeProccess(root):
    def runProggram():
        load_images = load_images_from_folder("uploads")
        normalize= normalize_silhouettes(load_images)
        print("Data has been executed")
        remove = remove_folder(root,"uploads")
        
    return CustomButton(root, "Execute Data", runProggram)
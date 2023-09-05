import os
from rembg import remove
from PIL import Image
folder_path = "images/test"
folder_save = "images/test-png"
num_files = len(os.listdir(folder_path))

'''
if not os.path.exists(folder_path):
    print(f"Pasta {folder_path} não existe.")
'''
for i in range(num_files):
    image_input = Image.open(f"{folder_path}/{i}.jpg")
    image_output = remove(image_input)
    image_output.save(f"{folder_save}/{i}.png")

print("Processo concluido")
import os
import 
import numpy as np

folder_path = "images/test"
folder_save = "images/test-png"
folder_gray = "images/test-gray"
num_files = len(os.listdir(folder_path))
#images = []

for i in range(num_files):
    image = cv2.imread(f'{folder_path}/{i}.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (128, 64))
    #images.append(resized_image)
    resized_image = np.array(resized_image)/255.00
    cv2.imwrite(f'{folder_gray}/{i}.jpg', resized_image*255)

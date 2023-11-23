import Augument as am

import glob
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
# import random
import math
import os

def load_images(path):
    image_list=[]
    images= glob.glob(path)
    image_names=[]
    n=len(images)
    print("images : loaded : ",n)
    for index in range(0,n):
        image= cv2.cvtColor(cv2.imread(images[index]),cv2.COLOR_BGR2RGB)
        image_list.append(cv2.resize(image,(1280,720)))

        image_n=images[index]
        image_names.append(image_n.split('/')[-1])

    return image_list,image_names

output_directory = "/home/vikas/Downloads/DL_PROJECT/new"
if not os.path.exists(output_directory):
  os.makedirs(output_directory)


import random
import os

def apply_random_filters(images, filter_functions, num_filters_to_apply=1):
    filtered_images = []
    for image in images:
        filtered_image_copy = image.copy()  # Create a copy of the original image

        for _ in range(num_filters_to_apply):
            c=np.random.choice(['T','F'], p=[0.8,0.2])
            # print(c)
            if c=='T':
              random_filter_function = random.choice(filter_functions)  # Choose a random filter function
              random_filter_function = am.add_autumn
              # print(random_filter_function)
              filtered_image = random_filter_function(filtered_image_copy)  # Apply the chosen filter function
              filtered_images.append(filtered_image)
            else:
              filtered_images.append(filtered_image_copy)

    return filtered_images


filter_functions = [am.brighten,am.darken,am.add_shadow,am.add_snow,am.add_rain, am.add_fog, am.add_sun_flare, am.add_speed, am.add_autumn]

path=('/home/vikas/Videos/t/*.jpg')
# path=('valid/images/0d056ff0-c51e-48af-b9a8-9a01613480b3_jpg.rf.cbb724bd95fe3ac95e6a029542cd3cae.jpg')
images,names= load_images(path)
print(len(images),len(names))

num_filters_to_apply = 1
filtered_images = apply_random_filters(images, filter_functions, num_filters_to_apply)
# The filtered_images list will contain the results after applying random filters to each input image

from PIL import Image
for i, image in enumerate(filtered_images):
    # Construct the output file path for each image (e.g., output_folder/image_0.png, output_folder/image_1.png, ...)
    output_file_path = os.path.join(output_directory, f'{names[i]}')

    # Save the image to the specified file path
    # cv2.imwrite(output_file_path, image)
    pil_image = Image.fromarray(image)

    # Save the PIL image to the specified file path
    pil_image.save(output_file_path)
    print("saved",i)
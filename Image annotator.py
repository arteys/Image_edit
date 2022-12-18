import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image
import tkinter as tk
import tkinter.filedialog as fd
import matplotlib
import skimage.io
import skimage.util




location_image_1 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 1.png"
location_image_2 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 2.png"
location_image_3 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 2.png"

root = tk.Tk()
# paths = fd.askopenfilenames(parent=root, title='Open images')
paths = ['C:/Users/Modern/Desktop/Python/Image test/Test 1.png', 'C:/Users/Modern/Desktop/Python/Image test/Test 2.png', 'C:/Users/Modern/Desktop/Python/Image test/Test 3.png']



image_first = Image.open(paths[0])
x,y,z = np.shape(image_first)

empty_line = np.zeros([x,20,3])
color_line = np.full_like(empty_line, [255,255,255]).astype(np.uint8)

# image_montage_np = np.empty([x,y,z])
# image_montage_np = []

# for p in paths:
#     image_np = Image.open(p)
#     # image_montage_np.append(image_np)
#     # image_montage_np.append(color_line)
#     image_montage_np = np.append(image_montage_np,image_np)


montage = np.empty([x,1,z]).astype(np.uint8)


imgs = [skimage.io.imread(i) for i in paths]

for p in paths:
    img = cv2.imread(p)
    montage = np.concatenate([montage,color_line,img],axis = 1)
    
print(np.shape(montage))


cv2.imshow('image',montage)
cv2.waitKey(0)


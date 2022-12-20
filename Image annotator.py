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

empty_line = np.zeros([x,10,3])
color_line = np.full_like(empty_line, [255,255,255]).astype(np.uint8)


montage = np.empty([x,1,z]).astype(np.uint8)

labels = ["A","B","C"]
font = cv2.FONT_HERSHEY_PLAIN 
org = ( round(x*0.05), round(y*0.95))
fontScale = 5
color = (255, 255, 255)
thickness = 5

print(org)
i = 0
for p in paths:
    img = cv2.imread(p)
    image = cv2.putText(img, labels[i], org, font, fontScale, color, thickness, cv2.LINE_AA)
    montage = np.concatenate([montage,color_line,img],axis = 1)
    i = i+1


    

cv2.imshow('image',montage)
cv2.waitKey(0)


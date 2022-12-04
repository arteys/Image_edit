import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image




location_image_1 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 1.png"
location_image_2 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 2.png"

# img_1 = cv2.imread(location_image_1)
# img_2 = cv2.imread(location_image_2)

# list_im = [location_image_1,location_image_2]
# imgs    = [Image.open(i) for i in list_im ]

empty_line = np.zeros([512,20,3])
color_line = np.full_like(empty_line, [255,255,255]).astype(np.uint8)

list_im = [location_image_1,location_image_2]
imgs = [Image.open(i) for i in list_im ]
imgs_np = [np.array(i) for i in imgs]


# min_shape = sorted([(np.sum(i.size), i.size ) for i in imgs])[0][1]
# imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])

imgs_np_comb = np.concatenate([imgs_np[0],color_line,imgs_np[1],color_line], axis = 1)

# print(np.shape(imgs_np_comb))
# print(np.dtype(empty_line))
# print(imgs_np)

imgs_comb = Image.fromarray(imgs_np_comb,'RGB')
imgs_comb.show()  


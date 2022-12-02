import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image




location_image_1 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 1.png"
location_image_2 = "C:\\Users\\Modern\\Desktop\\Python\\Image test\\Test 2.png"

img_1 = cv2.imread(location_image_1)
img_2 = cv2.imread(location_image_2)

list_im = [location_image_1,location_image_2]
imgs    = [Image.open(i) for i in list_im ]

black_line = np.zeros([512,20,3])

min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
# imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])

# imgs_comb = np.hstack([[imgs[0]],[black_line],[imgs[1]]])

# imgs_comb = Image.fromarray(imgs_comb)
# imgs_comb.show()


# d_y,d_x,d_z = img_1.shape
# print(d_x,d_y,d_z)




# print(np.shape(image_w_border))

# chans = cv2.split(image_w_border)
# print(chans)

# chans = cv2.split(image_w_border)
# colors = 'b', 'g', 'r'

# plt.figure()
# plt.title('Flattened color histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')

# for (chan, color) in zip(chans, colors):
#     hist = cv2.calcHist([chan], [0], None, [256], [0, 255])
#     plt.plot(hist, color=color)
#     plt.xlim([0, 256])
#     plt.ylim([0, 5000])

# plt.show()
# cv2.waitKey(0)

# vis_2 = np.concatenate((vis,img_2), axis=1)

# imS = cv2.resize(vis_2, (512+20+512, 512))

# cv2.imshow('image', image_w_border)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

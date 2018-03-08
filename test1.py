import numpy as np
import cv2
from matplotlib import pyplot as plt

id_image1 = 'nuclei1.png'
img = cv2.imread(id_image1, 0)

assert isinstance(img, object)
ave = np.sum(img)/img.size
ret, bin_img = cv2.threshold(img, ave, 255, cv2.THRESH_BINARY)
# cv2.imshow(bin_img)
print (ret)

plt.imshow(bin_img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


import numpy as np
#from scipy import misc
import matplotlib.pyplot as plt
import cv2


# #photo_data=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
# photo_data=cv2.imread('img.jpg')
# print(type(photo_data))
# print(photo_data.shape)

# #HOW TO SHOW IMAGE 
# # plt.figure(figsize=(15,15))
# # plt.imshow(photo_data)
# # plt.show()

# #(3725, 4797, 3)
# # print(photo_data)

# # print("******************")
# # tmp=photo_data[:2,:2]
# # print(tmp.shape)
# # print(tmp)

# # print("******************")
# # tmp=photo_data[:1,:1]
# # print(tmp.shape)
# # print(tmp)


# # print(photo_data.max(),photo_data.min())
# # print(photo_data.mean())
# # print(photo_data[150,250])
# # print(photo_data[150,250,0])
# # print(photo_data[150,250,1])
# # print(photo_data[150,250,2])


# # #CHANGE COLOURS IN A RANGE
# # photo_data[200:800,:,1]=255
# # photo_data[200:800,:,0]=255
# # photo_data[200:800,:,2]=255
# # plt.figure(figsize=(10,10))
# # plt.imshow(photo_data)
# # plt.show()


# #photo_data=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
# photo_data=cv2.imread('img.jpg')
# # print(photo_data.shape)
# # lowValueFilter=photo_data<50
# # print(lowValueFilter[2])
# # print(lowValueFilter.shape)



# import random

# plt.figure(figsize=(10,10))
# plt.imshow(photo_data)
# plt.show()

# photo_data[lowValueFilter]=255
# plt.figure(figsize=(10,10))
# plt.imshow(photo_data)
# plt.show()
photo_data=cv2.imread('img.jpg')
# print(photo_data.shape)
# print(len(photo_data))
rowRange=np.arange(len(photo_data))
coldRange=rowRange

photo_data[rowRange,coldRange]=255

# Displaying the image
# cv2.imshow('image', photo_data)

plt.figure(figsize=(15,15))
plt.imshow(photo_data)
plt.show()

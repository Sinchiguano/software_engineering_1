#SCIPY LIBRARY TO WORK WITH IMAGES

from matplotlib.pyplot import imread

'''
The method imread in scipy.misc requires the forked package of PIL named Pillow. If you are having 
problem installing the right version of PIL try using imread in other packages:
'''

#read a jpeg image into numpy array

img=imread('tmp.jpeg')
print(img.shape, img.dtype)




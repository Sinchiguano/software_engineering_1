import cv2

img=cv2.imread('tmp.jpeg',1)
cv2.imshow('Image',img)
cv2.waitKey()
cv2.destroyAllWindows() #enter to destroy all windows

#SAVE IMAGE
cv2.imwrite()



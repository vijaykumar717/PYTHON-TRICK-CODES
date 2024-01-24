import os
import cv2
image=(os.listdir('code/jpg'))
for i in image:
    read=cv2.imread('code/jpg/'+i)
    cv2.imwrite('code/py/'+i,read)
    print(read.shape)
##    cv2.imwrite('code/py.jpeg',read)

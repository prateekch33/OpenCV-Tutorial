import cv2 as cv
print(cv.__version__)
#Chapter 1
img=cv.imread("Resources/1608463046534.jpg")
imgFinal = cv.resize(img, (0, 0), fx = 0.4, fy = 0.3)
cv.imshow("Output",imgFinal)
cv.waitKey(0)
#Chapter 2
import numpy as np
img=cv.imread("Resources/1608463046534.jpg") #Image reading
kernel=np.ones((5,5),np.uint8) #Kernels for Dilation and Erosion
imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #Image in GrayScale
imgBlur=cv.GaussianBlur(imgGray,(7,7),0) #Blur Image
imgCanny=cv.Canny(img,100,100) #Caany Image means only borders/outline is shown
imgDilation=cv.dilate(imgCanny,kernel,iterations=1) #Dilation Image means more thick corner
imgEroded=cv.erode(imgDilation,kernel,iterations=1) #Erosion Image means less corners/intensity of corners eroded

#resizing according to screen size for better view
imgFinal1 = cv.resize(imgGray, (0, 0), fx = 0.4, fy = 0.3) 
imgFinal2 = cv.resize(imgBlur, (0, 0), fx = 0.4, fy = 0.3)
imgFinal3 = cv.resize(imgCanny, (0, 0), fx = 0.4, fy = 0.3)
imgFinal4 = cv.resize(imgDilation, (0, 0), fx = 0.4, fy = 0.3)
imgFinal5 = cv.resize(imgEroded, (0, 0), fx = 0.4, fy = 0.3)

#Display of Image
cv.imshow("Gray Image",imgFinal1)
cv.imshow("Blur Image",imgFinal2)
cv.imshow("Canny Image",imgFinal3)
cv.imshow("Dilation Image",imgFinal4)
cv.imshow("Eroded Image",imgFinal5)

#For Delay of the Display
cv.waitKey(0) # 0 stands for Infinite Delay
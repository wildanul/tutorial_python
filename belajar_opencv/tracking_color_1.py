import cv2
import numpy as np


def nothing(x):
    pass

cap = cv2.VideoCapture(0)

# Create a black image, a window
img = np.zeros((150,600,3), np.uint8)
img2 = np.zeros((150,600,3), np.uint8)

cv2.namedWindow('LOWER')
cv2.namedWindow('UPPER')

# create trackbars for color change
cv2.createTrackbar('LR','LOWER',-10,335,nothing)
cv2.createTrackbar('LG','LOWER',-10,255,nothing)
cv2.createTrackbar('LB','LOWER',-10,255,nothing)

cv2.createTrackbar('UR','UPPER',-10,255,nothing)
cv2.createTrackbar('UG','UPPER',-10,255,nothing)
cv2.createTrackbar('UB','UPPER',-10,255,nothing)

# create switch for ON/OFF functionality
switchL = '0:OFF 1:ON'
cv2.createTrackbar(switchL, 'LOWER',0,1,nothing)

# create switch for ON/OFF functionality
switchU = '0:OFF 1:ON'
cv2.createTrackbar(switchU, 'UPPER',0,1,nothing)

while(1):
    # Take each frame
    _, frame = cap.read()
    
    cv2.imshow('LOWER',img)
    cv2.imshow('UPPER',img2)

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('LR','LOWER')
    g = cv2.getTrackbarPos('LG','LOWER')
    b = cv2.getTrackbarPos('LB','LOWER')
    s = cv2.getTrackbarPos(switchL,'LOWER')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

    # get current positions of four trackbars
    r2 = cv2.getTrackbarPos('UR','UPPER')
    g2 = cv2.getTrackbarPos('UG','UPPER')
    b2 = cv2.getTrackbarPos('UB','UPPER')
    s2 = cv2.getTrackbarPos(switchU,'UPPER')

    if s2 == 0:
        img2[:] = 0
    else:
        img2[:] = [b2,g2,r2]
    
    #===========================================
        
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #lower = np.array([27,77,101])
    #upper = np.array([82,154,189])
    lower = np.array([r,g,b], dtype=np.uint8)
    upper = np.array([r2,g2,b2], dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

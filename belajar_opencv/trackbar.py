import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((150,600,3), np.uint8)
img2 = np.zeros((150,600,3), np.uint8)

cv2.namedWindow('image')
cv2.namedWindow('image2')

# create trackbars for color change
cv2.createTrackbar('LR','image',int(-10),255,nothing)
cv2.createTrackbar('LG','image',-10,255,nothing)
cv2.createTrackbar('LB','image',-10,255,nothing)

cv2.createTrackbar('UR','image2',0,255,nothing)
cv2.createTrackbar('UG','image2',0,255,nothing)
cv2.createTrackbar('UB','image2',0,255,nothing)

# create switch for ON/OFF functionality
switchL = '0:OFF 1:ON'
cv2.createTrackbar(switchL, 'image',0,1,nothing)

# create switch for ON/OFF functionality
switchU = '0:OFF 1:ON'
cv2.createTrackbar(switchU, 'image2',0,1,nothing)


while(1):
    cv2.imshow('image',img)
    cv2.imshow('image2',img2)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('LR','image')
    print r
    g = cv2.getTrackbarPos('LG','image')
    b = cv2.getTrackbarPos('LB','image')
    s = cv2.getTrackbarPos(switchL,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

    # get current positions of four trackbars
    r2 = cv2.getTrackbarPos('UR','image2')
    g2 = cv2.getTrackbarPos('UG','image2')
    b2 = cv2.getTrackbarPos('UB','image2')
    s2 = cv2.getTrackbarPos(switchU,'image2')

    if s2 == 0:
        img2[:] = 0
    else:
        img2[:] = [b2,g2,r2]


cv2.destroyAllWindows()

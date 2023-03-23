#Before install opencv on Terminal: $ pip install opencv-python

##
## Function: Draw circles with two diferente colors, using the click of mouse or the trackpad.
##

import cv2
import numpy as np

####################
##### FUNCTION #####
#------------------#

def draw_circle(event,x,y,flags,parm):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 45, (255,255,0),-1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 45, (255,0,255),-1)


cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)


#####################################
##### SHOWING IMAGE WITH OPENCV #####
#-----------------------------------#

img = np.zeros((800,800,3))
while True:
    cv2.imshow('my_drawing',img)

    # IF we've waited at least 1 ms AND we've pressed rhe Esc key by default
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
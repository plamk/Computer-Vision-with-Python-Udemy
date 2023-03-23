#Before run the script, you have to install opencv on Terminal: 
## $ pip install opencv-python
##
## Function: Draw circles with two diferente colors, using the click of mouse or the trackpad.
##
import cv2
import numpy as np

#------------------#
##### VARIABLES #####

#True while mouse button DOWN, False while mouse button IP
drawing = False
ix = -1
iy = -1


#------------------#
##### FUNCTION #####


def draw_rectangle(event,x,y,flags,parm):

    global ix,iy,drawing

    #when press left button of the mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img, (x,y), 45, (255,255,0),-1)
        drawing = True
        ix,iy = x,y
    
    #when move the mouse
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        #cv2.circle(img, (x,y), 45, (255,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing == False:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)


#---------------------------#
##### SHOWING THE IMAGE #####


#---------------#
##### BLACK #####

img = np.zeros((800,800,3))

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_rectangle)


while True:
    cv2.imshow('my_drawing',img)

    # IF we've waited at least 1 ms AND we've pressed rhe Esc key by default
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
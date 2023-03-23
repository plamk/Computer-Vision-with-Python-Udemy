import cv2
import numpy as np


##### FUNCTION #####
def draw_circle(event,x,y,flags,parm):

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,0,255),thickness=8)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

##### SHOWING IMAGE WITH OPENCV #####
img = cv2.imread('../../DATA/dog_backpack.jpg')
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

while True:
    cv2.imshow('my_drawing',img)

    # IF we've waited at least 1 ms AND we've pressed rhe Esc key by default
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
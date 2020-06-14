# import libraries of python OpenCV  
# where its functionality resides 
import cv2  
  
# np is an alias pointing to numpy library 
import numpy as np 
  
# capture frames from a camera 
cap = cv2.VideoCapture(0) 

# loop runs if capturing has been initialized 
while(1):

    # reads frames from a camera 
    ret, frame = cap.read()

    # Converting the image to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Converting gray scale image to GaussianBlur  
    # so that change can be find easily 
    gaussianblur = cv2.GaussianBlur(gray, (5, 5), 0)

    # using Canny function
    edges = cv2.Canny(gaussianblur, 60, 120)

    #original frame
    cv2.imshow('Original',frame) 

    # edge frame
    cv2.imshow('edges', edges)

    #exit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  




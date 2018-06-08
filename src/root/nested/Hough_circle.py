'''
Created on 7. jun. 2018

@author: Morten
'''
import sys
import cv2
import numpy as np

def main(argv):
    
    #cam = cv2.VideoCapture(0)
    #running, frame = cam.read()
    frame = cv2.imread('p5.jpg',0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
    
    gray = cv2.medianBlur(gray, 5)
    
    
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 1,
                               param1=100, param2=30,
                               minRadius=100, maxRadius=500)
    
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(frame, center, radius, (255, 0, 255), 3)
    
    
    cv2.imshow("detected circles", frame)
    cv2.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
import cv2
import numpy as np
from function import image_differencing


video_input = input("Enter Video Path: ")
cap = cv2.VideoCapture(video_input)

image_differencing(cap)


    




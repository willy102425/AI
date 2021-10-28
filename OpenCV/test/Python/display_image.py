#================================================#
#  Auther:   Willy Xie                           #
#  Filename: display_image.py                    #
#  Version:  1.0                                 #
#=============================================== #
#  Description:                                  #
#  An example of using opencv to read and        #
#  display image.                                #
#================================================#

# Reference : https://blog.gtwang.org/programming/ubuntu-linux-install-opencv-cpp-python-hello-world-tutorial/
#-*- coding: utf-8 -*-
import cv2
import sys

# Check for existence of the input image
if (len(sys.argv) != 2):
  print("usage: " + sys.argv[0] + " <Image_Path>n")
  sys.exit(-1);

# Read the frame
img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

# Display the image until any keyboard interrupt is received
cv2.namedWindow("Display Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow('Display Image', img)
cv2.waitKey(0)

"""
# Project: Object Extraction
# Filename: pixel_estimator.py
# Description: Algorithm for replacing the pixels inside of
#              an image with estimated pixel values using the
#              pixels around that area. 
#
# Collaborator: Eliasar Gandara
#
# Date Created: 2/25/15
# Last Modified: 2/25/15
"""

# from PIL import Image
from numpy import *
from scipy import misc

"""
Will create an imaage from an array
@param obj Object with array interface
@param mode (RGBA) Way to save an image
@return image Returns an image object
"""
# PIL.Image.fromarray(obj, mode=None)


# PIL Stuff
"""
image = Image.open("cow.jpg") # opens the image into a variable
dimensions = image.size # returns the dimensions of the image
width, height = dimensions[0], dimensions[1] # returns the height and width into seperate variables

pixels = list(image.getdata())
"""


pixels = misc.imread("cow.jpg")             # assigns the data from the image into a numpy array
height, width, dimensions = pixels.shape    # assigns the height, width, and dimensions of the array to variables
num_pixels = 0

for row in range(0, height):                # iterates through the rows of the arrray
    for column in range(0, width):          # iterates through the columns of the array
        num_pixels += 1




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

from PIL import Image
from numpy import *
from scipy import misc

# --------------------------------------------------------------------------------------------------------

def isPatternUsable(kernel, row, column):
    index = 0
    for i in range(0,9):
        red, green, blue = kernel[index]
        index += 1
        if (red < 50 and green < 50 and blue > 200):
            return False
    return True

# --------------------------------------------------------------------------------------------------------

def getPattern(painted, row, column):
    height, width, dimensions = painted.shape   # assigns the height, width, and dimensions of the array to variables
    red, green, blue = 0, 0, 0
    pixel = painted[row][column]

    if ((row > 0 and column > 0) and
        (row > 0 and column < width - 2) and
        (row < height - 2 and column > 0) and
        (row < height - 2 and column < width - 2)):
        best_pattern = []

        top_left_pattern = []           # Lists for holding the pixel kernel
        bottom_left_pattern = []        # for the pattern to use
        top_right_pattern = []
        bottom_right_pattern = []

        for i in range(-9, -6):                                         # Retrieve the pixel kernels for the 
            for j in range(-9, -6):                                     # four different diagonals from the pixel
                top_left_pattern.append(painted[row + i][column + j])
                
        for i in range(-9, -6):
            for j in range(9, 12):
                top_right_pattern.append(painted[row + i][column + j])

        for i in range(9, 12):
            for j in range(-9, -6):
                bottom_left_pattern.append(painted[row + i][column + j])

        for i in range(9, 12):
            for j in range(9, 12):
                bottom_right_pattern.append(painted[row + i][column + j])

        top_left_total = 0              # Add up the total pixel values in 
        bottom_left_total = 0           # each of the lists
        top_right_total = 0
        bottom_right_total = 0

        isTopLeftUsable = isPatternUsable(top_left_pattern, row, column)          # Booleans used for checking if a 
        isBottomLeftUsable = isPatternUsable(bottom_left_pattern, row, column)    # specific list is usable for the
        isTopRightUsable = isPatternUsable(top_right_pattern, row, column)        # pattern
        isBottomRightUsable = isPatternUsable(bottom_right_pattern, row, column)

        for pixel in range(0, 9):
            for value in range(0,3):
                top_left_total += top_left_pattern[pixel][value]
                bottom_left_total += top_left_pattern[pixel][value]
                top_right_total += top_left_pattern[pixel][value]
                bottom_right_total += top_left_pattern[pixel][value]

        if (isTopLeftUsable):
            return top_left_pattern
        elif (isBottomLeftUsable):
            return bottom_left_pattern
        elif (isTopRightUsable):
            return top_right_pattern
        elif (isBottomRightUsable):
            return bottom_right_pattern

        # Next check which direction you just moved from to determine which function to return
        # This will require being able to go in a circle around the painted area


# --------------------------------------------------------------------------------------------------------

def main():
    
    painted_image = "drawing.png"


    painted = misc.imread(painted_image) # assigns the data from the painted image into a nupy array

    height, width, dimensions = painted.shape   # assigns the height, width, and dimensions of the array to variables

    for row in range(0, height):                # iterates through the rows of the arrray
        for column in range(0, width):          # iterates through the columns of the array
            red, green, blue = painted[row][column]
            if (red < 50 and green < 50 and blue > 200):
                pattern = getPattern(painted, row, column) # gets a pixel kernel that is 3x3 pixels
                
                index = 0
                for i in range(-2, 1):      # changes the pixels in the original pixel array
                    for j in range(-2, 1):  # with the pixel kernel in pattern
                        painted[row + i][column + j] = pattern[index]
                        index += 1

    new_image = Image.fromarray(painted)    # Creates an image object from the pixels in the array
    new_image.show()    # displays the new_image to the screen
            
# --------------------------------------------------------------------------------------------------------

main() # Calls all of the functions into a main function




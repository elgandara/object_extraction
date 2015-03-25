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


"""
Will create an imaage from an array
@param obj Object with array interface
@param mode (RGBA) Way to save an image
@return image Returns an image object
"""
# PIL.Image.fromarray(obj, mode=None)

# --------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------

#def replacePixels(pixels):

# --------------------------------------------------------------------------------------------------------

def getDiagonalPixel(painted, row, column):

    """ Will find the pixel that has not been changed and
    is diagnonally across to the bottom right of the pixel entered"""

    height, width, dimensions = painted.shape    # assigns the height, width, and dimensions
                                                # of the array to variables
    red, green, blue = painted[row][column]     # Gets the color values in the pixel
    
    while ((red < 10 and green < 10 and blue > 245) and (row < height and column < width)):

        red, green, blue = painted[row][column]     # Gets the color values in the pixel
        if (red != 0 and green != 0 and blue != 254):
            return painted[row][column]

        row += 1
        column += 1


    return None

# --------------------------------------------------------------------------------------------------------

def getLowerPixel(painted, row, column):
    """ Will find the pixel that has not been changed and
    is vertically below the pixel entered"""

    height, width, dimensions = painted.shape    # assigns the height, width, and dimensions
                                                # of the array to variables
    red, green, blue = painted[row][column]     # Gets the color values in the pixel


    while ((red < 10 and green < 10 and blue > 245) and row < height - 1):

        red, green, blue = painted[row][column]     # Gets the color values in the pixel
        if (red != 0 and green != 0 and blue != 254):
            return painted[row][column]
        
        row += 1

    return None

# --------------------------------------------------------------------------------------------------------

def getRightPixel(painted, row, column):
    """ Will find the pixel that has not been changed and
    is horizontally right of the pixel entered"""

    height, width, dimensions = painted.shape   # assigns the height, width, and dimensions
                                                # of the array to variables
    red, green, blue = painted[row][column]     # Gets the color values in the pixel

    while ((red < 10 and green < 10 and blue > 245) and column < width - 1):

        red, green, blue = painted[row][column]     # Gets the color values in the pixel
        if (red != 0 and green != 0 and blue != 254):
            return painted[row][column]
        
        column += 1
            
        

    return None

# --------------------------------------------------------------------------------------------------------

def getLeftPixel(painted, row, column):
    '''Will find the pixel that has not been changed and
       is located left of the current pixels'''

    height, width, dimensions = painted.shape   # assigns the height, width, and dimensions
                                                # of the array to variables
    red, green, blue = painted[row][column]     # Gets the color values in the pixel

    while ((red < 10 and green < 10 and blue > 245) and column > 0):

        red, green, blue = painted[row][column]     # Gets the color values in the pixel
        if (red != 0 and green != 0 and blue != 254):
            return painted[row][column]

        column -= 1

    return None

# --------------------------------------------------------------------------------------------------------

def replaceLeftDiagonalPixel(painted, row, column):
    '''Will create a new pixel for a painted pixel and replace it with and
       estimated value produced from neighboring pixels'''

    height, width, dimensions = painted.shape
    red, green, blue = painted[row][column]
    x = row;
    y = column;

    while ((red < 10 and green < 10 and blue > 245) and x > row - 5 and y > column - 5):
        red, green, blue = painted[x][y]
        
        if (red != 0 and green != 0 and blue != 254):
            return painted[x][y]

        x -= 1
        y -= 1
        
    return None
        
# --------------------------------------------------------------------------------------------------------

#def createNewPixel(subArray):

# --------------------------------------------------------------------------------------------------------

def getPattern(painted, row, column):
    height, width, dimensions = painted.shape   # assigns the height, width, and dimensions of the array to variables
    red, green, blue = 0, 0, 0
    pixel = painted[row][column]

    if ((row > 0 and column > 0) and
        (row > 0 and column < width - 2) and
        (row < height - 2 and column > 0) and
        (row < height - 2 and column < width - 2)):
        sub_array = []

        for i in range(-8, -5):
            for j in range(-3, 2):
                sub_array.append(painted[row + i][column + j])

        # Add a part that grabs a sub array from each direction and then chooses the one
        # that does not have any blue pixels to replace the area with

    return sub_array
    
        
# --------------------------------------------------------------------------------------------------------

#image = "blue_cow.jpg"
painted_image = "blue_cow.jpg"
count = 0
total = 0
success = 0
fail = 0


#pixels = misc.imread(image)         # assigns the data from the image into a numpy array
painted = misc.imread(painted_image) # assigns the data from the painted image into a nupy array

height, width, dimensions = painted.shape   # assigns the height, width, and dimensions of the array to variables

for row in range(0, height):                # iterates through the rows of the arrray
    for column in range(0, width):          # iterates through the columns of the array
        red, green, blue = painted[row][column]
        if (red < 50 and green < 50 and blue > 200):
            pattern = getPattern(painted, row, column)
            
            index = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    painted[row + i][column + j] = pattern[index]
                    index += 1
            
            

            

            

print "Made it to the end"
            

new_image = Image.fromarray(painted)
new_image.show()


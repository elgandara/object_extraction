"""
# Project: Object Extraction
# Filename: object_extraction.py
# Description: The program will allow the user to color a region
#              from an image and then will replace the pixels in
#              that area with what it estimates would be in that
#              location of the image.
#
# Contributor: Salvador Ramirez
# Contributor: Eliasar Gandara
#
# Date Created: 2/25/15
# Last Modified: 2/25/15
"""
#----------Imported to get file directory---
from Tkinter import *
from tkFileDialog import askopenfilename
Tk().withdraw()
#-------------------------------------------


from pygame import *	
import pygame

from PIL import Image




def main():
    
    done = False
    open_image = askopenfilename()              #gets file directory
    background = pygame.image.load(open_image)

    im = Image.open(open_image)
    width, height = im.size                     # gets width and height of image


    init()					    # Start PyGame
    screen = display.set_mode((width, height))  # Give us a nice window

    display.set_caption('Sathya Project')
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (255, 255, 255)
    lineWidth = 7

    screen.blit(background, (0,0))          #sets background
    pygame.display.flip()
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(screen, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            

        pygame.display.flip()


main()

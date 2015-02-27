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
    
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 255)
    lineWidth = 7

    screen.blit(background, (0,0))          #sets background
    pygame.display.flip()
    
    while keepGoing:
        
        print screen.get_at((mouse.get_pos())) 
        
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





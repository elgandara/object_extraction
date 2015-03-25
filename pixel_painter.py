#----------Imported to get file directory---
from Tkinter import *
from tkFileDialog import askopenfilename
Tk().withdraw()
#-------------------------------------------
from pygame import *	
import pygame
from PIL import Image
from functools import wraps # need for counting function calls
#--------------Function allows function calls to be counted----------------
def counter(fn):
    @wraps(fn)
    def tmp(*args, **kwargs):
        tmp.count += 1
        return fn(*args, **kwargs)
    tmp.count = 0
    return tmp

    
@counter # Determines what function's function calls will be called
def Big():
    print "Big" #prints 'Big' on the IDLE window 
@counter
def Medium():
    print "Medium"
@counter
def Small():
    print "Small"
@counter
def Red():
    print "Red"
@counter
def Green():
    print "Green"
@counter
def Blue():
    print "Blue"
@counter
#-----------------------------------------------------------------------------
def ExitChoice():#function allows user to choose a picture
    Painting(Big.count, Medium.count, Small.count, Red.count, Green.count, Blue.count)
    print Big.count, Medium.count, Small.count, Red.count, Green.count, Blue.count
    exit()

#--------------------------------------
def Painting(Big,Medium,Small,Red,Green,Blue):
    done = False
    open_image = askopenfilename()              #gets file directory
    background = pygame.image.load(open_image)

    im = Image.open(open_image)
    width, height = im.size                     # gets width and height of image


    init()					    # Starts PyGame
    screen = display.set_mode((width, height))  # Makes a Window based on height and width

    display.set_caption('Sathya Project')
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    #-------checks what function was called to determine the color chosen by the user---------------------
    if(Blue > 0):
        drawColor = (0, 0, 255)# Sets the Blue color
    elif(Red > 0):
        drawColor = (255, 0, 0)# Sets the Red color
    elif(Green > 0):
        drawColor = (0, 255, 0)# Setthe Green color
    else:
        drawColor = (255,255,255)# sets the default white color
    if(Big > 0):
        lineWidth = 30 # sets the Big brush
    elif(Medium > 0):
        lineWidth = 10 # sets the Medium brush
    elif(Small > 0):
        lineWidth = 3 # Sets the small brush
    else:
        lineWidth = 5 #sets the default brush
    #----------------------------------------------------------------------------------------------------
    screen.blit(background, (0,0))          #sets background
    pygame.display.flip()
    
    while keepGoing:#keeps looping to determin where the mouse is
        clock.tick(30)
        print screen.get_at((mouse.get_pos())) #prints the current position of the mouse

        if pygame.mouse.get_pressed() == (0, 0, 1):# Ends the program when the user makes a right click
            keepGoing = False
            exit()
            
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()# gets the last position of the mouse
                if pygame.mouse.get_pressed() == (1, 0, 0): #draws on the picture if the user makes a left click
                    pygame.draw.line(screen, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd

        pygame.display.flip()
        #image.save(screen, "drawing.png")
    image.save(screen, "drawing.png")
        
def Gui():#-----------Function creates GUI with choices--------------------------
    
    app = Tk()
    app.title("Choose brush size and color")# Title of the GUI
    app.geometry("400x200")# size of the GUI

    relStatus = StringVar()
    relStatus.set(None)
    radio1 = Radiobutton(app, text = "Big",value = "Big", variable = relStatus, command = Big).pack()# Makes a choice for the user
    radio1 = Radiobutton(app, text = "Medium", value = "Medium", variable = relStatus, command = Medium).pack()
    radio1 = Radiobutton(app, text = "Small", value = "Small", variable = relStatus, command = Small).pack()
    radio1 = Radiobutton(app, text = "Red", value = "Red", variable = relStatus, command = Red).pack()
    radio1 = Radiobutton(app, text = "Green", value = "Green", variable = relStatus, command = Green).pack()
    radio1 = Radiobutton(app, text = "Blue", value = "Blue", variable = relStatus, command = Blue).pack()
    radio1 = Radiobutton(app, text = "Choose Picture", value = "Choose Picture", variable = relStatus, command = ExitChoice).pack()
    app.mainloop()
    exit()
    #---------------------------------------------------------------------------------

def main():
    Gui()

main()





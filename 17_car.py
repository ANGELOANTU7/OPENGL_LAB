'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 17             ####
####    EXPERIMENT NAME:CAR            ####
####                                   ####
###########################################
###########################################

'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
from playsound import playsound
import pygame

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
speed=10
FPS=60

factor=1

# initialising pygame
pygame.init()
 

pygame.font.init()
pygame.mixer.init() # add this line
# creating display
display = pygame.display.set_mode((300, 300))


music = pygame.mixer.music.load('breakout.mp3')
pygame.mixer.music.play(-1)
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawCircle(x,y,s):
    i=0.0
    if s==0:
        y=y-100-35
        x=x-50
    else:
        y=y-100-35
        x=x+50
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x,35*math.sin(math.pi*i/180.0)+y)
    glEnd()
def drawRectangle(x,y):
    glBegin(GL_QUADS)
    glVertex2f(x-100,y+50)
    glVertex2f(x+100,y+50)
    glVertex2f(x+100,y-100)
    glVertex2f(x-100,y-100)
    glEnd()

def drawCar():
    global GLOBAL_X
    global GLOBAL_Y
    global DIR
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    drawRectangle(GLOBAL_X,GLOBAL_Y)
    drawCircle(GLOBAL_X,GLOBAL_Y,0)
    drawCircle(GLOBAL_X,GLOBAL_Y,1)
    glutSwapBuffers()


def animate(temp):
    global WINDOW_SIZE
    global GLOBAL_X
    global GLOBAL_Y
    global factor
    
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))

    if(GLOBAL_X+100<WINDOW_SIZE):          
        GLOBAL_X=GLOBAL_X+factor
    else:
        GLOBAL_X=-400

    ouch = pygame.mixer.Sound('engine.mp3')
    horn = pygame.mixer.Sound('horn.mp3')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                print("left")
                factor=factor-1
                pygame.mixer.Sound.play(ouch)
               
            # checking if key "D" was pressed
            if event.key == pygame.K_d:
                print("right")
                factor=factor+1
                pygame.mixer.Sound.play(ouch)

            # checking if key "S" was pressed
            if event.key == pygame.K_s:
                print("stop")
                factor=0
              
            # checking if key "H" was pressed
            if event.key == pygame.K_h:
                print("horn")
                factor=factor-1
                pygame.mixer.Sound.play(horn)




def main():

    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Car")
    glutDisplayFunc(drawCar)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawCar)
    init()
    glutMainLoop()

main()

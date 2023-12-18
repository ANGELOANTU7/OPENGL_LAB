'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 8              ####
####     EXPERIMENT NAME: CIRCLE       ####
####                                   ####
###########################################
###########################################

'''
import math,time
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

x=100
y=0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)

def drawCircle(x,y,s):

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361):
        glVertex2f(5/100*math.cos(math.pi*i/180.0)+x/100,5/100*math.sin(math.pi*i/180.0)+y/100)
    glEnd()





def snowman():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    drawCircle(50,50,0)
    drawCircle(30,20,1)
    glutSwapBuffers()



glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(600,0)
glutCreateWindow("SAMPLE")
snowman()
init()
glutMainLoop()

'''
###########################################
###########################################
             
              OUTPUT

IMAGE ATTACHED

###########################################
###########################################

'''

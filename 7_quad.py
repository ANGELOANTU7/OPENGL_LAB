'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 7              ####
####     EXPERIMENT NAME: QUAD         ####
####                                   ####
###########################################
###########################################

'''
import math,time
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

x=-200
y=0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-300,300,-300,300)

def draw():
	global x,y
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,1)
	glLineWidth(2)
	glBegin(GL_QUADS)
	glVertex2f(x,y)
	glVertex2f(x+50,y)
	glVertex2f(x+50,y+50)
	glVertex2f(x,y+50)
	glEnd()
	glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(600,0)
glutCreateWindow("SAMPLE")
glutDisplayFunc(lambda:draw())
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

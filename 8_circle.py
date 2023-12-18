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
	gluOrtho2D(-300,300,-300,300)

def plot():
	global x,y
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,1)
	glLineWidth(2)

	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)

	for i in range (0,361):
		
		glVertex2f(x+50*math.cos(i),y+50*math.sin(i))
	x=x+1;
	y=y+1;
	print(x)
	glEnd()
	glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(600,0)
glutCreateWindow("SAMPLE")

glutDisplayFunc(lambda:plot())
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

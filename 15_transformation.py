'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 15             ####
####    EXPERIMENT NAME:TRANSFORMATION ####
####                                   ####
###########################################
###########################################

'''

import math
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-500,500.0,-500,500.0)

def plotaxes():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	glBegin(GL_LINES)
	glVertex2f(0,-500)
	glVertex2f(0,500)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(500,0)
	glVertex2f(-500,0)
	glEnd()

def plotgrid():
	glColor3f(0.202,0.202,0.202)
	for i in range(-500,500,50):
		if i!=0:
			glBegin(GL_LINES)
			glVertex2f(i, 500)
			glVertex2f(i, -500)
			glEnd()	
			glBegin(GL_LINES)
			glVertex2f(500,i)
			glVertex2f(-500,i)
			glEnd()	

def plotTriangle(x1,x2,x3,y1,y2,y3):
	glBegin(GL_LINES)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x2, y2)
	glVertex2f(x3, y3)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x3, y3)
	glVertex2f(x1, y1)
	glEnd()

def drawTranslated(x1,x2,x3,y1,y2,y3,tx,ty):
	points = [[x1, y1],[x2, y2],[x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([point[0]+tx, point[1]+ty])
	print(newpoints)
	
	plotaxes()
	plotgrid()
	glColor3f(0,0,1)
	plotTriangle(x1,x2,x3,y1,y2,y3)
	glColor3f(1,0,1)
	plotTriangle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
	glFlush()

def translate(x1,x2,x3,y1,y2,y3,tx,ty):
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("2d TRANSFORMATIONS")
	glutDisplayFunc(lambda: drawTranslated(x1,x2,x3,y1,y2,y3,tx,ty))
	init()
	glutMainLoop()

def drawScaled(x1,x2,x3,y1,y2,y3,tx,ty):
	points = [[x1, y1],[x2, y2],[x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([point[0]*tx, point[1]*ty])
	print(newpoints)
	
	plotaxes()
	plotgrid()
	glColor3f(0,0,1)
	plotTriangle(x1,x2,x3,y1,y2,y3)
	glColor3f(1,0,1)
	plotTriangle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
	glFlush()

def scale(x1,x2,x3,y1,y2,y3,tx,ty):
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("2d TRANSFORMATIONS")
	glutDisplayFunc(lambda: drawScaled(x1,x2,x3,y1,y2,y3,tx,ty))
	init()
	glutMainLoop()

def drawRotated(x1,x2,x3,y1,y2,y3,theta):
	points = [[x1, y1],[x2, y2],[x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([round(point[0]*math.cos(theta)-point[1]*math.sin(theta)),round(point[0]*math.sin(theta)+point[1]*math.cos(theta))])
	print(newpoints)
	
	plotaxes()
	plotgrid()
	glColor3f(0,0,1)
	plotTriangle(x1,x2,x3,y1,y2,y3)
	glColor3f(1,0,1)
	plotTriangle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
	glFlush()

def rotate(x1,x2,x3,y1,y2,y3):
	theta = (math.pi/180)*int(input("Enter no. of degrees to be rotated"))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("2d TRANSFORMATIONS")
	glutDisplayFunc(lambda: drawRotated(x1,x2,x3,y1,y2,y3,theta))
	init()
	glutMainLoop()

def drawReflected(x1,x2,x3,y1,y2,y3,ch):
	points = [[x1, y1],[x2, y2],[x3, y3]]
	newpoints = []
	for point in points:
		if(ch == 1):
			newpoints.append([point[0], -point[1]])
		elif(ch == 2):
			newpoints.append([-point[0], point[1]])
		elif(ch == 3):
			newpoints.append([-point[0], -point[1]])
		elif(ch == 4):
			newpoints.append([point[1], point[0]])
		elif(ch == 5):
			newpoints.append([-point[1], -point[0]])
	print(newpoints)
	
	plotaxes()
	plotgrid()
	glColor3f(0,0,1)
	plotTriangle(x1,x2,x3,y1,y2,y3)
	glColor3f(1,0,1)
	plotTriangle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
	glFlush()

def reflect(x1,x2,x3,y1,y2,y3):
	ch = int(input("Enter type of reflection\n1.about x axis\n2.about y axis\n3.about origin\n4.about x=y line\n5.about x=-y line"))

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("2d TRANSFORMATIONS")
	glutDisplayFunc(lambda: drawReflected(x1,x2,x3,y1,y2,y3,ch))
	init()
	glutMainLoop()

def main():
	print("Triangle coordinates:")
	x1 = float(input("x1 = "))
	y1 = float(input("y1 = "))
	side = float(input("side = "))
	x2 = side
	y2 = y1
	x3 = x1 + side/2
	y3 = y1+0.866025*side

	while(True):

		choice = int(input("Enter choice as follows for different methods of transformations\n1.Translation\n2.Scaling\n3.Rotation\n4.Reflection"))
		
		if choice == 1:
			tx = int(input("x translation: "))
			ty = int(input("y translation: "))
			translate(x1,x2,x3,y1,y2,y3,tx,ty)
		elif choice == 2:
			tx = int(input("x scale: "))
			ty = int(input("y scale: "))
			scale(x1,x2,x3,y1,y2,y3,tx,ty)
		elif choice == 3:
			rotate(x1,x2,x3,y1,y2,y3)
		elif choice == 4:
			reflect(x1,x2,x3,y1,y2,y3)
		else:
			break;

main() 

'''
###########################################
###########################################
             
              OUTPUT

IMAGE ATTACHED

###########################################
###########################################

'''

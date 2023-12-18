'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 14             ####
####    EXPERIMENT NAME:ELLIPSE        ####
####                                   ####
###########################################
###########################################

'''
import math
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 500
scale = 100

xc = yc = 0
rx = ry = 1

def init_display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(5)

def no_ellipse():
	pass


def polar_ellipse():
	glBegin(GL_POINTS)
	
	global rx, ry, xc, yc
	theta = 0.0
	while theta <= 1.57:
		x = float(rx)*math.cos(theta)
		y = float(ry)*math.sin(theta)
		plot_symmetric_points(x, y)
		theta += 0.001
	glEnd()
	glFlush()

def nonpolar_ellipse():
	glBegin(GL_POINTS)
	
	global rx, ry, xc, yc
	x = 0
	while x<=rx:
		y = ry*math.sqrt(1-((x*x)/(rx*rx)))
		plot_symmetric_points(x, y)
		x += 0.01
	glEnd()
	glFlush()

def midpoint_ellipse():
	

	glBegin(GL_POINTS)
	
	global rx, ry, xc, yc
	x = 0
	y = ry
	d1 = (ry*ry)-(rx*rx*ry)+(0.25*rx*rx)
	dx = 2*ry*ry*x
	dy = 2*rx*rx*y

	while(dx<dy):
		plot_symmetric_points(x, y)	
		
		if(d1<0):
			x += 1
			dx = dx + (2*ry*ry)
			d1 = d1 + dx + (ry*ry)
		
		else:
			x += 1
			y -= 1
			dx = dx + (2*ry*ry)
			dy = dy - (2*rx*rx)
			d1 = d1 + dx - dy + (ry*ry)

	d2 = ((ry*ry)*((x+0.5)*(x+0.5))) + ((rx*rx)*((y-1)*(y-1))) - ((rx*rx)*(ry*ry))
	while(y>=0):
		plot_symmetric_points(x, y)
		
		if(d2>0):
			y -= 1
			dy = dy - (2*rx*rx)
			dx = dx + (2*ry*ry)
			d2 = d2 - dy + (rx*rx)
		
		else:
			y -= 1
			x += 1
			dx = dx + (2*ry*ry)
			dy = dy - (2*rx*rx)
			d2 = d2 + dx - dy + (rx*rx)

	glEnd()
	glFlush()

def plot_symmetric_points(x, y):
	global xc, yc
	glVertex2f((xc + x)/scale, (yc + y)/scale)
	glVertex2f((xc - x)/scale, (yc + y)/scale)
	glVertex2f((xc + x)/scale, (yc - y)/scale)
	glVertex2f((xc - x)/scale, (yc - y)/scale)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	global xc, yc, rx, ry
	xc= int(input("Enter x of centre: "))
	yc= int(input("Enter y of centre: "))
	rx= int(input("Enter length of semimajor axis: "))
	ry= int(input("Enter length of semiminor axis: "))

	choice = int(input("Enter choice, 1. Mid-point method, 2.Polar Method, 3.Non-polar Method\n"))
	
	glutCreateWindow("Ellipse")
	init_display()
	if choice == 1:
		glutDisplayFunc(midpoint_ellipse)
	elif choice == 2:
		glutDisplayFunc(polar_ellipse)
	elif choice == 3:
		glutDisplayFunc(nonpolar_ellipse)
	else:
		glutDisplayFunc(no_ellipse)

	glutMainLoop()

main()


'''
###########################################
###########################################
             
              OUTPUT

IMAGE ATTACHED

###########################################
###########################################

'''

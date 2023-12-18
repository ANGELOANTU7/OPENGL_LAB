'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 9              ####
####     EXPERIMENT NAME: POLYGON      ####
####                                   ####
###########################################
###########################################

'''

import math,time
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

x=0
y=0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-300,300,-300,300)

def draw(coordinate_list):
	global x,y
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,1)
	glLineWidth(2)

	glBegin(GL_POLYGON)
	

	for i in coordinate_list:
		
		glVertex2fv(i)
	
	glEnd()
	glutSwapBuffers()



list1=[]
no=0
no=int(input("Enter how many vertices: "))

for i  in range (0,no):
	xy=[]
	xy.append(float(input("enter x"+str(i+1)+" :")))
	xy.append(float(input("enter x"+str(i+1)+" :")))
	list1.append(xy)

print(list1)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(600,0)
glutCreateWindow("SAMPLE")

glutDisplayFunc(lambda:draw(list1))
init()
glutMainLoop()


'''
###########################################
###########################################
              INPUT
             
Enter how many vertices: 6
enter x1 :150
enter x1 :100
enter x2 :150
enter x2 :200
enter x3 :100
enter x3 :250
enter x4 :50
enter x4 :200
enter x5 :50
enter x5 :100
enter x6 :100
enter x6 :50



              OUTPUT

IMAGE ATTACHED

###########################################
###########################################

'''

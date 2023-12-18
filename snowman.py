from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def drawci(r,cx,cy,R,G,B):
	
	glColor3f(R,G,B)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(cx,cy)
	for i in range(0,361,):
		glVertex2f(r*math.cos(math.pi*i/180)+cx,r*math.sin(math.pi*i/180)+cy)
	glEnd()
	glFlush()
def drawhand(x1,y1,x2,y2):
	glBegin(GL_LINES)
	glVertex2f(x1,y1)	
	glVertex2f(x2,y2)
	glEnd()

def nose():
	
	glColor3f(1,0,0)
	glLineWidth(20)
	glBegin(GL_POLYGON)
	glVertex2f(0,125)
	glVertex2f(5,110)
	glVertex2f(50,110)
	glEnd()

def smile():
	cx=0
	cy=125
	glColor3f(0,0,0)
	r=2
	glBegin(GL_LINES)
	glLineWidth(5)
	glVertex2f(cx,cy)
	for i in range(0,180,):
		glVertex2f(r*math.cos(math.pi*i/180)+cx,r*math.sin(math.pi*i/180)+cy)
	glEnd()
	glFlush()
	
 



def snowman():
	
	drawci(80,0,0,1,1,1)
	drawci(40,0,120,1,1,1)

	drawci(5,-20,130,0,0,0)
	drawci(5,20,130,0,0,0)
	nose()
	

	

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	snowman()
	glutSwapBuffers()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(600,0)
	glutCreateWindow("Snowman")
	glutDisplayFunc(lambda:Display())
	gluOrtho2D(-300,300,-300,300)
	glutMainLoop()
main()


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


angle = 0
x = 0
forward = True


def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 60)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(77/255, 179/255, 179/255, 1)


def draw():
    global angle
    global x
    global forward

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # terrain
    glColor3f(68/255, 155/255, 13/255)
    glBegin(GL_QUADS)
    glVertex(-500, -1.25 * 0.5 - 0.6, -15)
    glVertex(-500, -1.25 * 0.5 - 0.6, 10)
    glVertex(30, -1.25 * 0.5 - 0.6, 10)
    glVertex(30, -1.25 * 0.5 - 0.6, -15)
    glEnd()

    # road
    glColor3f(115/255, 145/255, 141/255)
    glBegin(GL_POLYGON)
    glVertex(-300, -1.25 * 0.5 - 0.5, -4.5)
    glVertex(-300, -1.25 * 0.5 - 0.5, 4.5)
    glVertex(10, -1.25 * 0.5 - 0.5, 4.5)
    glVertex(10, -1.25 * 0.5 - 0.5, -4.5)
    glEnd()

    # lanes
    for i in range(-30, 11, 4):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex(i, -1.25 * 0.5 - 0.4, -0.5)
        glVertex(i, -1.25 * 0.5 - 0.4, 0.5)
        glVertex(i + 3, -1.25 * 0.4 - 0.5, 0.5)
        glVertex(i + 3, -1.25 * 0.4 - 0.5, -0.5)
        glEnd()


    # Lower
    glColor3f(0.769, 0.275, 0.271)
    glTranslate(x, 0, 0)
    glScale(1, 0.15, 0.5)
    glutSolidCube(5)
    glColor3f(0.25, 0, 0)
    glutWireCube(5.02)

    # Upper
    glColor3f(0.906, 0.361, 0.357)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, 0.25)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0.25, 0, 0)
    glutWireCube(5.02)

    # Wind Shields
    glLoadIdentity()
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_POLYGON)
    glVertex(x + 1.26, 1.25 / 2 + 1.25, 1.5 - 0.1)
    glVertex(x + 1.26, 1.25 / 2, 1.5 - 0.1)
    glVertex(x + 1.26, 1.25 / 2, -1 + 0.1)
    glVertex(x + 1.26, 1.25 / 2 + 1.25, -1 + 0.1)
    glEnd()

    # Side
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_POLYGON)
    glVertex(x + 1.2, 1.25 / 2 + 1.25 - 0.05, 1.51)
    glVertex(x + 1.2, 1.25 / 2 + 0.05, 1.51)
    glVertex(x - 1.2, 1.25 / 2 + 0.05, 1.51)
    glVertex(x - 1.2, 1.25 / 2 + 1.25 - 0.05, 1.51)
    glEnd()

    # Wheels
    glColor3f(0.113, 0.09, 0.082)
    glLoadIdentity()
    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.25, 0.375, 20, 20)
    glColor3f(0.855, 0.819, 0.819)
    glutSolidSphere(0.25, 20, 20)

    glColor3f(0.113, 0.09, 0.082)
    glLoadIdentity()
    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, - 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.25, 0.375, 20, 20)
    glColor3f(0.855, 0.819, 0.819)
    glutSolidSphere(0.25, 20, 20)

    glColor3f(0.113, 0.09, 0.082)
    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, -0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.25, 0.375, 20, 20)
    glColor3f(0.855, 0.819, 0.819)
    glutSolidSphere(0.25, 20, 20)

    glColor3f(0.113, 0.09, 0.082)
    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.25, 0.375, 20, 20)
    glColor3f(0.855, 0.819, 0.819)
    glutSolidSphere(0.25, 20, 20)
    glutSwapBuffers()

    if forward:
        angle -= 0.4
        x += 0.006
        if x > 5:
            forward = False
    else:
        angle += 0.4
        x -= 0.006
        if x < -5:
            forward = True


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

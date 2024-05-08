import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Back Face
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Top Face
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Bottom Face
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Right face
    glColor3f(1.0, 0.0, 1.0)  # Purple
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Left Face
    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    glEnd()

def setup():
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)

def main():
    pygame.init()
    setup()

    drag = False
    rotate_x, rotate_y = 0, 0
    drag_start = [0, 0]
    rotation_mouse_step = 0.05
    end_step = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    drag = True
                    drag_start = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drag = False
            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    x, y = event.pos
                    dx = x - drag_start[0]
                    dy = y - drag_start[1]
                    drag_start = [x, y]
                    rotate_x += dy * rotation_mouse_step
                    rotate_y += dx * rotation_mouse_step

        # Auto slow down rotation
        if rotate_x > 0:
            rotate_x -= end_step
            if rotate_x < 0:
                rotate_x = 0
        else:
            rotate_x += end_step
            if rotate_x > 0:
                rotate_x = 0

        if rotate_y > 0:
            rotate_y -= end_step
            if rotate_y < 0:
                rotate_y = 0
        else:
            rotate_y += end_step
            if rotate_y > 0:
                rotate_y = 0

        glRotatef(rotate_x, 1, 0, 0)
        glRotatef(rotate_y, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

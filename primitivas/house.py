from OpenGL.GL import *
from glew_wish import *
from math import * 
import glfw


def draw_roof():
    glBegin(GL_TRIANGLES)
    glColor3f(0.2,0.2,0.2)

    glVertex3f(-0.8,0.4,0)
    glVertex3f(0.9,0.4,0)
    glVertex3f(0.05,0.90,0)

    glEnd()

def draw_dirt():
    glBegin(GL_QUADS)
    glColor3f(0.9,0.9,0.5)

    glVertex3f(-1,-1,0)
    glVertex3f(1,-1,0)
    glVertex3f(1,-0.5,0)
    glVertex3f(-1,-0.3,0)

    glEnd()

def draw_casa_fondo():
    glBegin(GL_QUADS)
    glColor3f(0.23,0.2,0.2)

    glVertex3f(-0.5,-0.5,0)
    glVertex3f(0.6,-0.5,0)
    glVertex3f(0.6,0.4,0)
    glVertex3f(-0.5,0.4,0)

    glEnd()

def draw_casa_door():
    glBegin(GL_QUADS)
    glColor3f(0.8,0.8,0.7)

    glVertex3f(-0.2,-0.5,0)
    glVertex3f(0.3,-0.5,0)
    glVertex3f(0.3,-0.1,0)
    glVertex3f(-0.2,-0.1,0)

    glEnd()

def draw_window():
    glBegin(GL_QUADS)
    glColor3f(0.6,0.7,1)

    glVertex3f(0.1,0,0)
    glVertex3f(0.4,0,0)
    glVertex3f(0.4,0.3,0)
    glVertex3f(0.1,0.3,0)

    glEnd()

def draw_tree():
    glBegin(GL_QUADS)
    glColor3f(0.7,0.5,0.3)

    glVertex3f(-0.78,-0.62,0)
    glVertex3f(-0.63,-0.62,0)
    glVertex3f(-0.63,0,0)
    glVertex3f(-0.78,0,0)

    glEnd()

def draw_window_linesExt():
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)

    glVertex3f(0.1,0,0)
    glVertex3f(0.4,0,0)
    glVertex3f(0.4,0.3,0)
    glVertex3f(0.1,0.3,0)

    glEnd()

def draw_window_linesInt():
    glBegin(GL_LINES)
    glColor3f(0,0,0)

    glVertex3f(0.1,0.15,0)
    glVertex3f(0.4,0.15,0)
    glVertex3f(0.25,0.0,0)
    glVertex3f(0.25,0.3,0)
    glEnd()

def draw_sun():
    posx, posy = -0.85,0.85  
    sides = 32    
    radius = 0.25   
    glBegin(GL_POLYGON)
    glColor3f(0.9,0.9,0.3)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_cloud():
    posx, posy = - 0.2,0.8 
    sides = 32    
    radius = 0.1  
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_cloud2():
    posx, posy = - 0.3,0.8 
    sides = 32    
    radius = 0.1  
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_cloud3():
    posx, posy = - 0.23,0.85 
    sides = 32    
    radius = 0.1  
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_cloud4():
    posx, posy = - -0.55,0.6 
    sides = 32    
    radius = 0.1  
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_cloud5():
    posx, posy = - -0.67,0.6 
    sides = 32    
    radius = 0.1  
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_cloud6():
    posx, posy = - -0.6,0.65 
    sides = 32    
    radius = 0.1  
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_raySun():
    glBegin(GL_QUADS)
    glColor3f(0.9,0.9,0.3)

    glVertex3f(-0.6,0.78,0)
    glVertex3f(-0.4,0.75,0)
    glVertex3f(-0.35,0.85,0)
    glVertex3f(-0.55,0.85,0)

    glEnd()

def draw_raySun2():
    glBegin(GL_QUADS)
    glColor3f(0.9,0.9,0.3)

    glVertex3f(-0.8,0.55,0)
    glVertex3f(-0.6,0.55,0)
    glVertex3f(-0.55,0.65,0)
    glVertex3f(-0.55,0.65,0)

    glEnd()

def draw_cope():
    posx, posy = - 0.7,0 
    sides = 32    
    radius = 0.2  
    glBegin(GL_POLYGON)
    glColor3f(0,0.4,0)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def draw_knob():
    posx, posy = 0.252,-0.345  
    sides = 32    
    radius = 0.02  
    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "Mi ventana", None, None)

    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    #Establecer Contexto
    glfw.make_context_current(window)

    #inicializar Glew
    glewExperimental = True
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return
    
    #Imprimir Version
    version = glGetString(GL_VERSION)
    print(version)
 
 
    #Draw Loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0, 800, 800)
        #Establecer color de borrado
        glClearColor(0.6,0.9,1 ,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        draw_dirt()
        draw_casa_fondo()
        draw_window()
        draw_window_linesExt()
        draw_window_linesInt()
        draw_cloud()
        draw_cloud2()
        draw_cloud3()
        draw_cloud4()
        draw_cloud5()
        draw_cloud6()
        draw_roof()
        draw_casa_door()
        draw_tree()
        draw_sun()
        draw_raySun()
        draw_raySun2()
        draw_cope()
        draw_knob()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ =="__main__":
    main()

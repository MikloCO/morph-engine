import ctypes
import os
from typing import Type
from OpenGL.GL import *
#from OpenGL.GLUT import *
import sdl3

from src.core.render.window import Window2d, Window3d

os.environ["SDL_MAIN_USE_CALLBACKS"] = "1"

sdl_context = sdl3.SDL_GL_CreateContext(None)


def get_open_gl_info():
    try:
        list =[
            glGetString(GL_VENDOR).decode('utf-8'),
            glGetString(GL_RENDERER).decode('utf-8'),
            glGetString(GL_VERSION).decode('utf-8'),
            glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8')

        ]
        print(list)
    except Exception as e:
        print({e})


def init_program():
    if sdl3.SDL_InitSubSystem(sdl3.SDL_INIT_VIDEO) < 0:
        raise Exception(f"SDL couldn't be initialized! {sdl3.SDL_GetError()}")


def clean_up(w: sdl3.SDL_Window):
    sdl3.SDL_DestroyWindow(w)
    sdl3.SDL_Quit()




def PreDraw():
    pass


def Draw():
    pass

    # Input
    # Update
    # Render / pre render
    # Clean memory


def main():
    init_program()
    window = Window3d(title=b"Morph in 3D", width=800, height=800, flags=sdl3.SDL_WINDOW_OPENGL)
    # renderer = sdl3.SDL_CreateRenderer(window.window, None)
    open_gl_context = sdl3.SDL_GL_CreateContext(window.window)
    if open_gl_context is None:
        print(f"Not av {sdl3.SDL_GetError()}")

    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MAJOR_VERSION, sdl3.SDL_GL_CONTEXT_PROFILE_MASK)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_DOUBLEBUFFER, 1)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_DEPTH_SIZE, 24)
    get_open_gl_info()
    #glGenVertexArrays() - Vertex array objects (VAO)
    #glBindVertexArray() - Vertex buffer object (VBO)
    exitloop = False

    Input(exitloop)

    #  Input()
    sdl3.SDL_GL_SwapWindow(window.window)  # Update screen

    #       sdl3.SDL_RenderClear(renderer)
    #       sdl3.SDL_RenderPresent(renderer)


    window.cleanup_window()


def Input(exitloop):
    event = sdl3.SDL_Event()
    while not exitloop:
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            if event.type == sdl3.SDL_EVENT_QUIT:
                exitloop = True


if __name__ == "__main__":
    raise SystemExit(main())

import ctypes
import os
import sys
from ctypes import ARRAY
from typing import Type
from OpenGL.GL import *
# from OpenGL.GLUT import *
import sdl3
import numpy as np

from src.core.render.window import Window3d

os.environ["SDL_MAIN_USE_CALLBACKS"] = "1"


def main():
    context = sdl3.SDL_GL_CreateContext(None)
    window_object = Window3d(title=b"Morph in 3D", width=800, height=800, flags=sdl3.SDL_WINDOW_OPENGL)
    if sdl3.SDL_InitSubSystem(sdl3.SDL_INIT_VIDEO) < 0:
        raise Exception(f"SDL couldn't be initialized! {sdl3.SDL_GetError()}")
    open_gl_context = sdl3.SDL_GL_CreateContext(window_object.window)
    if open_gl_context is None:
        print(sdl3.SDL_GetError())
    sdl3.SDL_GL_SwapWindow(window_object.window)  # Update screen

    glClearColor(1.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    sdl3.SDL_GL_SwapWindow(window_object.window)
    sdl3.SDL_Delay(2000)
    glClearColor(0.0, 1.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    sdl3.SDL_GL_SwapWindow(window_object.window)
    sdl3.SDL_Delay(2000)
    glClearColor(0.0, 0.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    sdl3.SDL_GL_SwapWindow(window_object.window)
    sdl3.SDL_Delay(2000)

    exit_loop = False
    Input(exit_loop)

    sdl3.SDL_GL_DeleteContext(context)
    sdl3.SDL_DestroyWindow(window_object)
    sdl3.SDL_Quit()


def Input(exitloop):
    event = sdl3.SDL_Event()
    while not exitloop:
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            if event.type == sdl3.SDL_EVENT_QUIT:
                exitloop = True


if __name__ == "__main__":
    raise SystemExit(main())

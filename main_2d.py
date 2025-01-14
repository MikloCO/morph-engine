import ctypes
import os
from typing import Type
from OpenGL.GL import *
from OpenGL.GLUT import *
import sdl3

from src.core.render.window import Window2d, Window3d

os.environ["SDL_MAIN_USE_CALLBACKS"] = "1"


def main():
    if sdl3.SDL_InitSubSystem(sdl3.SDL_INIT_VIDEO) < 0:
        raise Exception("SDL couldn't be initialized!")

    window = Window2d(title=b"Morph", width=800, height=800, flags=sdl3.SDL_WINDOW_RESIZABLE)

    renderer = sdl3.SDL_CreateRenderer(window.window, None)
    image = sdl3.IMG_Load(b"assets/images/morph.png")
    bitmapTex = sdl3.SDL_CreateTextureFromSurface(renderer, image)
    sdl3.SDL_DestroySurface(image)
    stop = False
    event = sdl3.SDL_Event()  # Create an instance of SDL_Event

    while not stop:
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            if event.type == sdl3.SDL_EVENT_QUIT:
                stop = True
        sdl3.SDL_RenderClear(renderer)
        sdl3.SDL_RenderTexture(renderer, bitmapTex, None, None)
        sdl3.SDL_RenderPresent(renderer)

    window.cleanup_window()
    sdl3.SDL_RenderClear(renderer)
    sdl3.SDL_free(image)
    sdl3.SDL_Quit()


if __name__ == "__main__":
    raise SystemExit(main())

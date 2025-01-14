import sdl3
from OpenGL.GL import *
from OpenGL.GLUT import *


class Window2d:
    def __init__(self, title: bytes, width: int, height: int, flags: sdl3.SDL_WindowFlags | int):
        self.title = title
        self.width = width
        self.height = height
        self.flags = flags
        self.window: sdl3.SDL_Window | None = None

        self.setup_window()

    def setup_window(self):
        self.window = sdl3.SDL_CreateWindow(self.title,
                                            self.width,
                                            self.height,
                                            self.flags)
        if self.window is None:
            print(f"Failed to create window: {sdl3.SDL_GetError()}")

    def cleanup_window(self):
        sdl3.SDL_DestroyWindow(self.window)

    def window(self) -> sdl3.SDL_Window:
        return self.window


class Window3d:
    """"https://www.khronos.org/opengl/wiki/Tutorial3:_Rendering_3D_Objects_(C_/SDL)
        https://www.libsdl.org/release/SDL-1.2.15/docs/html/guidevideoopengl.html"""""

    def __init__(self, title: bytes, width: int, height: int, flags: sdl3.SDL_WindowFlags | int):
        self.title = title
        self.width = width
        self.height = height
        self.flags = flags
        self.window = None #: sdl3.SDL_Window | None = None

        self.setup_window()

    def setup_window(self):
        self.window = sdl3.SDL_CreateWindow(self.title,
                                            self.width,
                                            self.height,
                                            self.flags)

        if self.window is None:
            print(f"Failed to create window: {sdl3.SDL_GetError()}")

    def cleanup_window(self):
        sdl3.SDL_DestroyWindow(self.window)

    def window(self) -> sdl3.SDL_Window:
        return self.window

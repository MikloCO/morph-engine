import ctypes
import os
import sdl3

os.environ["SDL_MAIN_USE_CALLBACKS"] = "1"


if __name__ == "__main__":
    if sdl3.SDL_InitSubSystem(sdl3.SDL_INIT_VIDEO) < 0:
        raise Exception("SDL couldn't be initialized!")

    window = sdl3.SDL_CreateWindow(b"Title",
                                   800,
                                   800,
                                   0)

    renderer = sdl3.SDL_CreateRenderer(window, None)

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

    sdl3.SDL_free(image)
    sdl3.SDL_RenderClear(renderer)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()



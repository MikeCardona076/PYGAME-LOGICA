# Example file showing a basic pygame "game loop"
import pygame
import sys

# pygame setup
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # CARGAR UNA CANCION Y REPRODUCIRLA
    try:
        pygame.mixer.music.load('Media\mikesonido.mp3')
        print("Música cargada correctamente.")
        pygame.mixer.music.play()
        print("Reproduciendo...")
    except pygame.error as e:
        print(f"No se pudo cargar el archivo de música: {e}")



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
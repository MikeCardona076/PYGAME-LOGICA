# Example file showing a basic pygame "game loop"
import pygame
import sys

# pygame setup
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ==========================================
# 1. CONFIGURACIÓN DE AUDIO (FUERA DEL BUCLE)
# ==========================================
try:
    pygame.mixer.music.load('Media/mikesonido.mp3')
    pygame.mixer.music.play(-1) # El -1 hace que la música se reproduzca en bucle
    print("Música cargada y reproduciéndose de fondo.")
except pygame.error as e:
    print(f"No se pudo cargar el archivo de música: {e}")


# ==========================================
# 2. CONFIGURACIÓN DE IMÁGENES (FUERA DEL BUCLE)
# ==========================================
# Cargamos las imágenes y las ajustamos al tamaño de la pantalla (1280x720)
try:
    img1 = pygame.image.load('Media/avedeto-pixel-art-8395222_1920.png')
    img1 = pygame.transform.scale(img1, (1280, 720))
    
    img2 = pygame.image.load('Media/gdj-calendar-9489720_1920.png')
    img2 = pygame.transform.scale(img2, (1280, 720))
    
    img3 = pygame.image.load('Media/pikura-tv-8760950_1920.png')
    img3 = pygame.transform.scale(img3, (1280, 720))
    
    # Las metemos en una lista
    lista_imagenes = [img1, img2, img3]
except pygame.error as e:
    print(f"Error al cargar las imágenes: {e}. Asegúrate de tenerlas en la carpeta Media.")
    lista_imagenes = []

# Variables para controlar la secuencia
indice_imagen = 0
tiempo_inicial = pygame.time.get_ticks()
tiempo_cambio = 2000 # 2000 milisegundos = 2 segundos


# ==========================================
# 3. EL BUCLE PRINCIPAL DEL JUEGO
# ==========================================
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- LÓGICA DEL TEMPORIZADOR ---
    tiempo_actual = pygame.time.get_ticks()
    # Si ha pasado el tiempo de cambio (2 segundos)...
    if tiempo_actual - tiempo_inicial > tiempo_cambio:
        indice_imagen += 1
        # Si llegamos al final de la lista, volvemos a empezar
        if indice_imagen >= len(lista_imagenes):
            indice_imagen = 0
        # Reiniciamos el cronómetro
        tiempo_inicial = tiempo_actual


    # --- RENDERIZADO (DIBUJAR EN PANTALLA) ---
    # Ya no hace falta el screen.fill("black") porque la imagen cubre todo
    if lista_imagenes:
        # Dibujamos la imagen actual en la coordenada (0,0)
        screen.blit(lista_imagenes[indice_imagen], (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()
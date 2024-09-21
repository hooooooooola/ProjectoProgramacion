import pygame
import sys

pygame.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)

FUENTE = pygame.font.SysFont(None, 36)

CELDA_SIZE = 50
ROWS = 5
COLS = 5
MARGIN = 100  
SIZE = (COLS * CELDA_SIZE + MARGIN, ROWS * CELDA_SIZE + MARGIN)

# solucion del ejemplo
solucion = [
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1]
]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Nanograma")

# matriz del juego inicializada en cero
tablero_jugador = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# pistas
pistas_ROWS = [[1, 1, 1], [2], [1, 2], [2, 1], [1, 1]]
pistas_COLS = [[1, 2], [1, 1], [2, 1], [2], [1, 1, 1]]

# funcion para dibujar el tablero
def draw():
    # dibujar las pistas de las filas
    for i, pista in enumerate(pistas_ROWS):
        superficie_texto = FUENTE.render(" ".join(map(str, pista)), True, NEGRO)
        screen.blit(superficie_texto, (10, i * CELDA_SIZE + MARGIN + 15))

    # dibujar  las pistas de las columnas
    for j, pista in enumerate(pistas_COLS):
        for k, numero in enumerate(pista):
            superficie_texto = FUENTE.render(str(numero), True, NEGRO)
            screen.blit(superficie_texto, (j * CELDA_SIZE + MARGIN + 15, 10 + (k * 30)))

    # dibujar la cuadricula con las celdas
    for fila in range(ROWS):
        for columna in range(COLS):
            color = GRIS if tablero_jugador[fila][columna] == 0 else NEGRO
            pygame.draw.rect(screen, color, [(columna * CELDA_SIZE + MARGIN), (fila * CELDA_SIZE + MARGIN), CELDA_SIZE, CELDA_SIZE])
            pygame.draw.rect(screen, NEGRO, [(columna * CELDA_SIZE + MARGIN), (fila * CELDA_SIZE + MARGIN), CELDA_SIZE, CELDA_SIZE], 1)

# funcion para ver si hemos ganado
def verificar():
    for fila in range(ROWS):
        for columna in range(COLS):
            if tablero_jugador[fila][columna] != solucion[fila][columna]:
                return False
    return True

# main
while True:
    # manejador de eventos
    for evento in pygame.event.get():
        # salir
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # clics
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if x > MARGIN and y > MARGIN:
                columna = (x - MARGIN) // CELDA_SIZE
                fila = (y - MARGIN) // CELDA_SIZE
                # marcada
                if fila < ROWS and columna < COLS:
                    tablero_jugador[fila][columna] = 1 - tablero_jugador[fila][columna]

    # dibujamos
    screen.fill(BLANCO)
    draw()

    # comprobamos y mostramos mensaje si hemos ganado
    if verificar():
        texto = pygame.font.SysFont(None, 60).render("¡Has ganado!", True, ROJO)
        screen.blit(texto, (MARGIN // 2, ROWS * CELDA_SIZE // 2))

    # actualizar 
    pygame.display.flip()

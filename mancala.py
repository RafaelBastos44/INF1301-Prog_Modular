import pygame
import sys

WIDTH = 1400
HEIGHT = 800

corTabuleiro = (222,184,135)
corCasa = (106,75,53)

pygame.init()

# Configs da janela
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mancala")

def draw():
    # Cor de fundo
    screen.fill((44, 130, 87))

    # Tabuleiro
    pygame.draw.rect(screen,corTabuleiro,(50,50,WIDTH-100,HEIGHT-100),border_radius=30)
    pygame.draw.line(screen,(0,0,0),(100,HEIGHT/2),(1300,HEIGHT/2),5)
    pygame.draw.rect(screen,corCasa,(75,100,100,HEIGHT-200),border_radius=30)
    pygame.draw.rect(screen,corCasa,(WIDTH-175,100,100,HEIGHT-200),border_radius=30)

    for i in range(6):
        pygame.draw.rect(screen,corCasa,(185+(175*i),100,155,250),border_radius=30)
        pygame.draw.rect(screen,corCasa,(185+(175*i),450,155,250),border_radius=30)
    
    # Atualizar a tela
    pygame.display.flip()


# Loop do jogo
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Função que atualiza a imagem na tela
    draw()
    


pygame.quit()
sys.exit()

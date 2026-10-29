import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Project 4 - Rotating Wheel")
running = True
while running:
    for session in pygame.event.get():
        if session.type == pygame.QUIT:
            running = False

    screen.fill((245, 245, 245))
    pygame.display.flip()
pygame.quit()

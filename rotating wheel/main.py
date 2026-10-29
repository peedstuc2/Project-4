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
    pygame.draw.circle(screen, (0, 0, 0), (400, 300), 50)
    #So i decided to just add an inner circle to blend with the background but make it smaller by reducing the radius. So the tire outline actually shows itself also i just decided to make the spokes black like how we initially planned.
    pygame.draw.circle(screen, (245, 245, 245), (400, 300), 45)
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 5)
    pygame.draw.line (screen, (0, 0, 0), (400, 300), (445, 300))
    pygame.display.flip()
pygame.quit()

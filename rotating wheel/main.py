import pygame
import math

#spokescount = 18
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

    #spokes
    TotalSpokes = 0
    angle = 0
    while TotalSpokes < 36:
    #for spokes in spokescount:

        lon = 300
        lat = 400
        end_x = lat + 50 * math.cos(math.radians(angle))
        end_y = lon + 50 * math.sin(math.radians(angle))

        pygame.draw.line(screen, (0, 0, 0), (400, 300), (end_x, end_y))
        angle += 10
        TotalSpokes += 1
    #pygame.draw.circle(screen, (255, 0, 0), (400, 300), 5) - I decided to remove this for now. The spokes kinda makes a clean looking diamond in the middle.

    pygame.display.flip()
pygame.quit()

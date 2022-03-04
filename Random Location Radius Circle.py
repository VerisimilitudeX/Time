# Libraries
import random
import pygame
pygame.init()

# Variables
w = pygame.display.set_mode([200, 200])
w.fill((255, 255, 255))
c = pygame.time.Clock()

# Main loop
animating = True
while animating:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False

    if pygame.time.get_ticks():
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        r = random.randint(1, 50)
        pygame.draw.circle(w, (0, 0, 0), (x, y), r)

    # Finish
    pygame.display.flip()
    c.tick(60)

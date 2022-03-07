# Libraries
import random
import pygame
pygame.init()

# Window
w = pygame.display.set_mode([200, 200])
w.fill((255, 255, 255))
pygame.display.flip()

c = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("The window was open for " + str(pygame.time.get_ticks() / 1000))
            running = False

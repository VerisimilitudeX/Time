# Libraries
import random
import pygame
pygame.init()

# Basic Setup
window = pygame.display.set_mode([500, 500])
c = pygame.time.Clock()
quit = False
timer = 500

# Animation Setup
x1 = 250
x2 = 0
x3 = 50
x4 = 450
x5 = 500
y1 = 125
y2 = 250
y3 = 350
y4 = 250
y5 = 125

# Main loop
while not quit:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    # Advance timer
    timer -= pygame.time.get_ticks()

    # Re-set points
    if timer >= 0:
        x1 = random.randint(225, 275)
        x2 = random.randint(0, 50)
        x3 = random.randint(25, 75)
        x4 = random.randint(425, 475)
        x5 = random.randint(450, 500)
        y1 = random.randint(100, 150)
        y2 = random.randint(225, 275)
        y3 = random.randint(325, 375)
        y4 = random.randint(225, 275)
        y5 = random.randint(100, 150)

    # Re-set timer
    if timer <= 0:
        timer = 50000

    # Draw
    window.fill((0, 25, 100))
    pygame.draw.polygon(window, (255, 255, 150), [(x1, 0), (175, y1), (x2, 125), (150, y2), (x3, 500), (250, y3), (x4, 500), (350, y4), (x5, 125), (325, y5)])

    # Finish
    c.tick(5)
    pygame.display.flip()

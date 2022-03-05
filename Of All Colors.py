"""
LESSON: 3.6 - Time
EXERCISE: Moving Art Gallery
PROBLEM: 2 of 4
"""

# Libraries
import random
import pygame
pygame.init()

# Basic Setup
window = pygame.display.set_mode([400, 600])
window.fill((0, 0, 0))
c = pygame.time.Clock()
quit = False
appearance_rate = 2000
last_circle_appeared = pygame.time.get_ticks()

# Main loop
while not quit:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    # Create new circle if necessary
    now = pygame.time.get_ticks()
    if now - last_circle_appeared > appearance_rate:

        # Draw new circle
        x = random.randint(0, 400)
        y = random.randint(0, 600)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        size = random.randint(10, 100)
        pygame.draw.circle(window, color, (x, y), size)

        # Re-set timing
        last_circle_appeared += c.get_time()
        appearance_rate -= 50
        if appearance_rate < 10:
            appearance_rate = 10

    # Finish
    c.tick(30)
    pygame.display.flip()

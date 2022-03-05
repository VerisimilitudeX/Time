"""
LESSON: 3.6 - Time
EXERCISE: Moving Art Gallery
PROBLEM: 4 of 4
"""

# Libraries
import pygame
pygame.init()

# Basic Setup
window = pygame.display.set_mode([600, 600])
c = pygame.time.Clock()
quit = False

# Animation Setup
x_speed = 8
y_speed = 7
x = 200
y = 300
hit = c.get_time()
pygame.time.wait(200)

# Main loop
while not quit:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    # Get times
    now = pygame.time.get_ticks()
    since_hit = pygame.time.get_ticks()

    # Bounce if necessary
    if x > 550:
        x_speed = -8
        hit = now

    elif x < 50:
        x_speed = 8
        hit = now

    elif y > 550:
        y_speed = -7
        hit = now

    elif y < 50:
        y_speed = 7
        hit = now

    # Move ball
    move = 1
    if since_hit != 0:
        move = 15/since_hit

    if x_speed < 0:
        x_speed += move
    else:
        x_speed -= move

    if y_speed < 0:
        y_speed += move
    else:
        y_speed -= move

    x += x_speed
    y += y_speed

    # Draw ball and background
    r = int(255 - (since_hit/5))
    g = int(255 - (since_hit/10))
    b = 150
    if r < 0 or r > 255:
        r = 0
    if g < 0 or g > 255:
        g = 0
    window.fill((r, g, b))
    pygame.draw.circle(window, (255, 255, 255), (int(x), int(y)), 50)

    # Finish
    c.tick(30)
    pygame.display.flip()

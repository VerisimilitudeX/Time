"""
LESSON: 3.6 - Time
EXERCISE: Moving Art Gallery
PROBLEM: 1 of 4
"""

# Libraries
import pygame
pygame.init()

# Basic setup
window = pygame.display.set_mode([400, 250])
c = pygame.time.Clock()
timer = 0
quit = False

# Animation setup
iris_x = 0
pupil_x = 0
black = (0, 0, 0)
iris_color = (50, 200, 200)
movingRight = True

# Main loop
while not quit:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    # Movement timer
    if movingRight:
        timer += c.get_time()
        iris_x = timer/5
        pupil_x = timer/5
    else:
        timer -= c.get_time()
        iris_x += timer/5
        pupil_x += timer/5
    # Move eye



    if iris_x > 400 or iris_x < -10:
        movingRight = not movingRight
    if pupil_x > 400 or pupil_x < -10:
        movingRight = not movingRight
        
    # Draw eye
    pygame.draw.circle(window, iris_color, (int(iris_x), 125), 70)
    pygame.draw.circle(window, black, (int(pupil_x), 125), 20)

    pygame.draw.polygon(window, black, [(0, 0), (200, 0), (0, 125)])
    pygame.draw.polygon(window, black, [(200, 0), (400, 0), (400, 125)])
    pygame.draw.polygon(window, black, [(400, 125), (400, 250), (200, 250)])
    pygame.draw.polygon(window, black, [(200, 250), (0, 250), (0, 125)])

    # Finish
    c.tick(30)
    pygame.display.flip()
    window.fill((255, 255, 255))

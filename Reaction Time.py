import random
import pygame

# Setup
pygame.init()
window = pygame.display.set_mode([200, 200])
c = pygame.time.Clock()
# variables
timer = 0
time_limit = 500
hit = False
duration_before_test = random.randint(3000, 5000)
# main loop
running = True
# event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if timer > duration_before_test:
                hit = True
# timer
    if timer > duration_before_test + time_limit:
        running = False
    if timer < duration_before_test:
        window.fill((255, 0, 0))
    else:
        window.fill((0, 255, 0))
# each frame
    c.tick(30)
    timer += c.get_time()
    pygame.display.flip()
# end stuff
if hit:
    print("You made it in time! Congratulations!! ")
else:
    print("I'm sorry, you didn't make it in time, please run the program to try again ")

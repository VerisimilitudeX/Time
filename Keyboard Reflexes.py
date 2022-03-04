import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((60, 60, 60))
button_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
pygame.draw.circle(window, (0, 0, 0), (200, 200), 85, 10)
pygame.draw.circle(window, button_color, (200, 200), 80)

print("Try to press a button every second!")

clock = start_time = pygame.time.get_ticks()
timer = 0

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.KEYDOWN:

            timer = clock.get_time()
            print(timer)

            timer = start_time

            button_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.circle(window, button_color, (200, 200), 80)

        pygame.display.flip()

import pygame
import random
pygame.init()

window = pygame.display.set_mode([600, 400])
sky_color = (120, 160, 250)
grass_color = (50, 180, 30)
track_color = (140, 70, 80)
runner_color = (180, 120, 200)
ground_rect = pygame.Rect(0, 220, 600, 180)
track_rect = pygame.Rect(0, 240, 600, 40)
runner = pygame.Rect(0, 180, 50, 80)
start_time = pygame.time.get_ticks()

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    runner.x += random.randint(2, 4)
    if runner.x > 530:
        drawing = False

    window.fill(sky_color)
    pygame.draw.rect(window, grass_color, ground_rect)
    pygame.draw.rect(window, track_color, track_rect)
    pygame.draw.line(window, (255, 255, 255), (0, 250), (600, 250), 3)
    pygame.draw.line(window, (255, 255, 255), (0, 260), (600, 260), 3)
    pygame.draw.line(window, (255, 255, 255), (0, 270), (600, 270), 3)
    pygame.draw.line(window, (255, 255, 255), (555, 240), (550, 280), 20)
    pygame.draw.ellipse(window, runner_color, runner)
    pygame.draw.ellipse(window, (0, 0, 0), runner, 3)

    pygame.display.flip()

end_time = pygame.time.get_ticks()
time_taken = end_time - start_time
time_taken /= 1000
print("You crossed the finish line in " +str(time_taken) + " seconds! ")

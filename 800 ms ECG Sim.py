import pygame
import random
pygame.init()

window = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()

frame_color = (230, 230, 200)
bg_color = (20, 20, 20)
line_color = (80, 255, 80)

screen = pygame.Rect(50, 50, 300, 300)

line_height = 30
line_speed = 8

timer = 0
time_limit = 800

drawing = True
while drawing:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += 50

    if timer > time_limit:
        line_speed *= -1
        timer = 0
        time_limit -= 50

    line_height += line_speed
    
    window.fill(frame_color)
    pygame.draw.rect(window, (255, 255, 255), screen, 5)
    pygame.draw.rect(window, bg_color, screen)
    pygame.draw.line(window, line_color, (50, 250), (150, 250))
    pygame.draw.line(window, line_color, (250, 250), (350, 250))
    pygame.draw.line(window, line_color, (150, 250), (200, 280 - line_height))
    pygame.draw.line(window, line_color, (250, 250), (200, 280 - line_height))

    pygame.display.flip()
    c.tick(30)

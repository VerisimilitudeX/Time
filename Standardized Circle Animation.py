import pygame
pygame.init()

window = pygame.display.set_mode([512, 256])
c = pygame.time.Clock()

ball_x = 0
back = False

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if ball_x >= 496:
        back = True
    if ball_x <= 0:
        back = False

    if back:
        ball_x -= 16
    else:
        ball_x += 16

    brightness = int(ball_x / 2)
    bg_color = (brightness, brightness, brightness)
    ball_color = (255 - brightness, 255 - brightness, 255 - brightness)
    window.fill(bg_color)
    pygame.draw.circle(window, ball_color, (ball_x, 128), 128)
    pygame.display.flip()

    c.tick(30)

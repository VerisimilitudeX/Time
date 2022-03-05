import pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode([500, 500])

timer = 0

moving_down = True
ball_x = 0
ball_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    if timer > 1000:
        moving_down = not moving_down
        timer = 0

    if moving_down:
        ball_y += 3

    else:
        ball_x += 3

    window.fill((23, 121, 223))
    pygame.draw.circle(window, (53, 31, 187), (ball_x, ball_y), 25)

    clock.tick(30)
    timer += clock.get_time()
    pygame.display.flip()

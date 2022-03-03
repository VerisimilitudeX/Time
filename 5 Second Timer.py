import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()

hourglass_top = pygame.Rect(170, 30, 60, 150)
hourglass_bottom = pygame.Rect(170, 379, 60, 1)
hourglass_back = [(170, 30), (170, 180), (190, 200), (170, 220), (170, 370), (230, 370), (230, 220), (210, 200), (230, 180), (230, 30)]

hourglass_back_color = (30, 30, 30)
hourglass_lining_color = (240, 240, 240)
sand_color = (200, 180, 80)

sand = 0
speed = 3
time = 0

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    time += c.get_time()
    sand += speed

    hourglass_top = pygame.Rect(170, 30 + sand, 60, 150 - sand)
    hourglass_bottom = pygame.Rect(170, 370 - sand, 60, 1 + sand)
    if sand >= 150:
        drawing = False

    window.fill((0, 0, 0))
    pygame.draw.polygon(window, hourglass_back_color, hourglass_back)
    pygame.draw.polygon(window, sand_color, [(170, 180), (190, 200), (210, 200), (230, 180)])
    pygame.draw.rect(window, sand_color, hourglass_top)
    pygame.draw.rect(window, sand_color, hourglass_bottom)
    pygame.draw.polygon(window, hourglass_lining_color, hourglass_back, 5)
    pygame.display.flip()

    c.tick(10.27)

print("The hourglass took " + str(time) + " milliseconds.")

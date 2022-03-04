import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()

sky_color = (180, 200, 255)
grass_color = (90, 200, 70)
tree_color = (100, 75, 50)
squirrel_color = (150, 140, 145)

grass = pygame.Rect(0, 300, 400, 100)
tree = pygame.Rect(150, 0, 100, 400)
leaves = pygame.Rect(25, -150, 350, 300)
squirrel = pygame.Rect(240, 300, 30, 60)

timer = 0
time_limit = 3000

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    squirrel.y -= 5
    timer += 50

    if timer > time_limit:
        squirrel.y = 300
        timer = 0

    window.fill(sky_color)
    pygame.draw.rect(window, tree_color, tree)
    pygame.draw.rect(window, squirrel_color, squirrel)
    pygame.draw.rect(window, grass_color, grass)
    pygame.draw.ellipse(window, grass_color, leaves)

    pygame.display.flip()
    c.tick(30)

import pygame
pygame.init()
c = pygame.time.Clock()

w = pygame.display.set_mode([200, 200])
clicks = 0
frames = 0

while clicks < 10:
    frames += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clicks = 100

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
    c.tick(20)

print("You took " + str(frames) + " frames to click 10 times")

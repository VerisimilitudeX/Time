import pygame
pygame.init()

window = pygame.display.set_mode([450, 400])

# --- Graphic variables --- #
background_color = (220, 230, 220)
clock_color = (50, 45, 60)

clock = start_time = pygame.time.get_ticks()

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    # --- Calculate time values --- #
    milliseconds = pygame.time.get_ticks()

    seconds = int(milliseconds / 1000)
    milliseconds = milliseconds % 1000
    tens = int(seconds / 10)
    seconds = seconds % 10

    # --- Draw --- #
    mills_rect = pygame.Rect(300, 0, 150, int(milliseconds * 0.4))
    seconds_rect = pygame.Rect(150, 0, 150, 40 * seconds)
    tens_rect = pygame.Rect(0, 0, 150, 40 * tens)

    window.fill(background_color)
    pygame.draw.rect(window, clock_color, seconds_rect)
    pygame.draw.rect(window, clock_color, mills_rect)
    pygame.draw.rect(window, clock_color, tens_rect)

    pygame.display.flip()

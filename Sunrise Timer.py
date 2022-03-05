#### ---- SETUP ---- ####

# --- Libraries --- #
import pygame
pygame.init()

# --- User input --- #
total_time = float(input("How long (in seconds) should the sunrise be? ")) * 1000

# --- Variables --- #
window = pygame.display.set_mode([300, 600])
c = pygame.time.Clock()
start_time = pygame.time.get_ticks()

sun_speed = 550 / total_time
sun_start = 575
sun_y = 575
sun_offset = 0
sky_color = 0

#### ---- MAIN LOOP ---- ####
running = True

while running:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Quit when time is up --- #
    current_time = pygame.time.get_ticks()
    
    if current_time - start_time > total_time:
        running = False

    # --- Move sun --- #
    sun_offset += sun_speed * 30
    sun_y = int(sun_start - sun_offset)

    # --- Calculate sky color --- #
    if sun_y < 300:
        sky_color = 255 - sun_y + 50
        
    if sky_color > 255:
        sky_color = 255

    elif sky_color < 0:
        sky_color = 0

    # --- Draw frame --- #
    window.fill((0, sky_color, 255))
    pygame.draw.circle(window, (255, 255, 0), (150, sun_y), 50)
    ground = pygame.Rect(0, 550, 300, 50)
    pygame.draw.rect(window, (150, 150, 60), ground)

    # --- Finish --- #
    c.tick(30)
    pygame.display.flip()

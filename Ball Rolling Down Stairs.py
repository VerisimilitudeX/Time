"""
LESSON: 3.6 - Time
EXERCISE: Stair Ball
"""

#### ---- SETUP ---- ####

# --- Libraries & window --- #

# Import pygame
import pygame

# INITialize pygame
pygame.init()
clock = pygame.time.Clock()

# Create a [500, 500] WINDOW and assign to window
window = pygame.display.set_mode([500, 500])

# --- Time variables --- #

# Create a CLOCK variable called c
# ---> TEST AFTER THIS LINE <--- #


# Create a variable called timer and assign the value 0
timer = 0


# --- Animation variables --- #

# Assign variable moving_down the value True
moving_down = True

# Assign variable ball_x the value 0
ball_x = 0

# Assign variable ball_y the value 0
ball_y = 0


#### ---- MAIN LOOP ---- ####

# Assign variable running the value True
running = True

# While running
while running:


    # --- Event loop --- #

    # Create an EVENT LOOP that gets all pygame events
    for event in pygame.event.get():

        # If the event TYPE is equal to QUIT
        if event.type == pygame.QUIT: 

            # Assign running the value False
            # ---> TEST AFTER THIS LINE <--- #
            running = False


    # --- Calculate ball direction & position --- #

    # If timer is greater than 1000
    if timer > 1000:

        # Assign moving_down the value not moving_down
        moving_down = not moving_down

        # Assign timer the value 0
        timer = 0

    # If moving_down
    if moving_down:

        # Increment ball_y by 3
        ball_y += 3

    # Else
    else:
        
        # Increment ball_x by 3
        # ---> TEST AFTER THIS LINE <--- #
        ball_x += 3


    # --- Draw frame --- #

    # FILL window with any COLOR
    window.fill((23, 121, 223))

    # Draw a CIRCLE in window with any COLOR at
    # ball_x, ball_y with radius 25
    pygame.draw.circle(window, (53, 31, 187), (ball_x, ball_y), 25)


    # --- Finish --- #

    # TICK c with 30
    clock.tick(30)

    # Increment timer by GET_TIME
    timer += clock.get_time()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()


# Turn in your Coding Exercise.

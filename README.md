# Time
## Framerate
* Framerate is the number of frames (loop iterations) in a second
* Faster computers will have higher framerates
## Why is it important?
* A program will look different on computers with different speeds
* PyGame Clock object keeps a constant framerate in the program
## How to use the PyGame Clock
*pygame.time.Clock() 
  * creates a clock (save in a variable)
*clock_variable.tick(framerate) 
  * advances the clock by one frame
*tick() should be called every loop iteration
* framerate argument is the maximum framerate you want (usually 30 or 60)
## How to track time
* clock_variable.get_time()
  * gets duration (time taken) of the previous frame
* Increment a variable by this amount each frame to track time that has passed 
  * Example: timer += c.get_time()
* Count down by decrementing timer
* Set up the timer variable in the setup section of the program
## How to record a specific time in the program
* pygame.time.get_ticks()
    * Can be called in a frame to get the current time
    * Returns milliseconds since the program started
## How to find the duration between times
* Duration is the amount of time that has passed
* Get two points in time 
  * pygame.time.get_ticks()
  * duration = later_time - earlier_time * Example: class_duration = class_end - class_start

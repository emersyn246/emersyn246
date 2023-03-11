import pygame
from bubble import Bubble
from paddle import Paddle
from bullet import Bullet

# setting up the display
pygame.init()
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]

display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()

run_game = True
background_color = [177,188,85] # chartreuse green

# this is so the paddle and the bubble will move at the same speed
paddle_and_bullet_speed = 3

# set up bubble
bubble_x = 50
bubble_y = 39
bubble_radius = 15
bubble_speed_y = 3
bubble_speed_x = 3
bubble_colour = [251, 202, 120] # mimosa yellow bubble
bubble = Bubble(bubble_x, bubble_y, bubble_radius, bubble_colour, bubble_speed_x, bubble_speed_y)

# set up the paddle
paddle_colour = [255, 179, 71] # pale orange paddle
paddle = Paddle(DISPLAY_WIDTH//2, DISPLAY_HEIGHT-10, 50, 20, paddle_colour, paddle_and_bullet_speed) #__init__(self, x, y, width, height, colour, speed)
paddle_coordinates = paddle.get_coordinates()

# set up the line
line_x1 = 0
line_y1 = DISPLAY_HEIGHT//2
line_x2 = DISPLAY_WIDTH
line_y2 = DISPLAY_HEIGHT//2
line_colour = [255, 255, 255] # white line

# set up the bullet
bullet_colour = [255, 83, 73] # red orange bullet -- I'm literally so obsessed with the colour scheme :)
bullet_speed_y = 3
bullet = Bullet((paddle_coordinates[0] + paddle_coordinates[2]//2) - 5, paddle_coordinates[1]-10, 10, 10, bullet_colour, paddle_and_bullet_speed, bullet_speed_y)

# the trigger variables
move_left = False
move_right = False

# game loop -- Everything involving the movement of the GUI components moving around the screen are event driven. This means the 
# the GUI componenets will not move without the appropriate event occurring. The way this works in my design is that pygame creates
# a list of keys that have been pressed (these are the events here). Depending on which key has been pressed, the program will then 
# change the appropriate trigger variable to true. Once this happens, the main program will then call the methods from the class to 
# manipulate the GUI object. I designed the main program and the classes in the way that I did so that the GUI objects can only be 
# manipulated if the class methods are called, rather that the main program itself manipulating it. The big way event driven 
# programming is used in my design is so that the objects are being controlled and not moving around randomly. Meaning that the 
# objects can only move and be manipulated if the event happens. 
while run_game:
    
    # Position list: [min x-coordinate, max x-coordinate, max y-coordinate]
    # Position list can also be: [padde x, paddle y, paddle width, paddle height] if the direction is 'down'

    # The paddle and bullet are idependent of each other -- so if the bullet is shooting, the paddle can still move
    # left or right but the bullet can't move left or right
    if move_left:
        paddle.move_left()

    elif move_right:
        paddle.move_right()
    
    # Oh my lord this part was such a headache to figure out :/
    # Thank you for all of your help :)

    # While the bullet has not been triggered, the bullet is allowed to move left and right if the move_left or 
    # move_right trigger variables have been switched to true.
    if not bullet.get_been_triggered():
        if move_left:
            bullet.move([DISPLAY_WIDTH - 480, DISPLAY_WIDTH - 40, 0], "left")
        elif  move_right:
            bullet.move([DISPLAY_WIDTH - 480, DISPLAY_WIDTH - 40, 0], "right")
    
    # Once the been_triggered variable in the bullet class has been switched to true, the bullet will not be allowed to move left 
    # or right even if the left or right arrow keys are being pressed. The program will call the wall_collision method to see if 
    # the bullet has reached the top of the screen. If it hasn't, the bullet will continue to move up. If it has, it will call the 
    # change_been_triggered method to change been_triggered variable back to false and then call the move method with the paddle 
    # coordinates in the position list spot and the direction 'down' to send it back to the paddle. 
    else:
        has_hit = bullet.wall_collision()
        if has_hit:
            bullet.change_been_triggered(False)
            current_coordinates = paddle.get_coordinates()
            bullet.move(current_coordinates, "down")
        else:
            bullet.move([DISPLAY_WIDTH - 480, DISPLAY_WIDTH - 40, 0], "up")

            
    # making sure we can close out of the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        
        # I heard the guy that was sitting across from me (American and wears glasses, I don't know his name) talk about this
        # UPDATE -- I heard his name is Aiden (really smart dude)

        # This will create a list of which keys have been pressed. 
        keys = pygame.key.get_pressed()

        # if the left arrow key is being pressed, then it will set the move_left trigger to true and move_right trigger to false
        if keys[pygame.K_LEFT]:
            move_left = True
            move_right = False

        # if the right arrow key is being pressed, then it will set the move_right trigger to true and move_left trigger to false
        elif keys[pygame.K_RIGHT]:
            move_left = False
            move_right = True

        # if the space bar is pressed, then it will set the been_triggered variable in the bullet class to True and the move 
        # variables to false
        elif keys[pygame.K_SPACE]:
            bullet.change_been_triggered(True)
            move_left = False
            move_right = False
    
        # if the user lets go of the left or right arrow keys, it will switch the move_left or move_right
        # trigger variables to false so the objects stop moving.
        if event.type == pygame.KEYUP:
            move_left = False
            move_right = False
        
    
    # setting everything up
    display.fill(background_color)
    bubble.draw(display)
    paddle.draw(display)
    bullet.draw(display)
    
    pygame.draw.line(display, line_colour, [line_x1,line_y1], [line_x2, line_y2], 4)
    bubble.move(DISPLAY_WIDTH, (DISPLAY_HEIGHT//2 - 5))

    pygame.display.update()
    clock.tick(45)

# closing pygame
pygame.quit()
quit()

import pygame

class Bullet():
    
    # initializing everything -- These are all private variables, meaning they cannot be modified
    # outside of the class. By the way I designed this class, each bullet object that is created in the main
    # program will be independent of each other. Each object that is created in the main will be able to behave 
    # in their own way without relying on any other object that is created in the main program. The main program
    # will figure out which event has occured, then call the appropriate method in this class. I chose to do instance variables 
    # in case someone wanted to modify my project and have two player game or something like that, then they would be able 
    # to make two GUI components that are completely independent of one another.

    def __init__(self, x, y, width, height, colour, speed_x, speed_y):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]
        self.__speed_y = speed_y
        self.__speed_x = speed_x
        self.__colour = colour
        self.__been_triggered = False
    
    def draw(self, display):
        # drawing the bullet with the colour and coordinates the user sends in 
        pygame.draw.rect(display, self.__colour, self.__coordinates)

    # With the design of this move method, the bullet's coordinates are being changed depending on the direction that gets
    # sent in. Depending on what key is being pressed, the main program will send in that direction to say how the coordinates
    # should change. This is known as event driven programming. The main program will decide when the event occurs, then call
    # the move method and send in the appropriate direction and position list depending on what event occurred. 
     
    def move(self, pos: list, direction):
        # Position list: [min x-coordinate, max x-coordinate, max y-coordinate, paddle x, paddle y, paddle width]

        if direction == "left":
            self.__coordinates[0] -= self.__speed_x
            
            # making sure the ball doesn't go off of the screen
            if self.__coordinates[0] <= pos[0]:
                self.__coordinates[0] = pos[0]

        elif direction == "right":
            self.__coordinates[0] += self.__speed_x
            
            # making sure the ball doesn't go off of the screen
            if self.__coordinates[0] >= pos[1]: 
                self.__coordinates[0] = pos[1]
            
        elif direction == "up":
            self.__coordinates[1] -= self.__speed_y

        elif direction == "down":
            # this is sending it back to the paddle so the user can shoot again
            self.__coordinates = [(pos[0] + pos[2]//2) - 5, pos[1]-10, 10, 10]
    
    # The wall_collision method is deciding whether the bullet has hit the top of the screen, aka the y-coordinate is 0 or less.
    # When this method is called, it will look at the y-coordinate in the self.__coordinates list and compare it to 0.
    # If it is less than 0, it will return true, indicating it has hit the wall. Otherwise it will return false, meaning 
    # it has not hit the wall.
    def wall_collision(self):
        if self.__coordinates[1] < 0:
            return True
        else:
            return False
    
    # The change_been_triggered will change the variable self.__been_triggered to whatever boolean value (true or false) 
    # gets sent in. The self.__been_triggered variable will be used in the main program to determine if the bullet has 
    # been triggered to shoot.
    def change_been_triggered(self, val):
        self.__been_triggered = val
    
    # The get_been_triggered method returns the variable self.__been_triggered which is boolean value of true or false.
    def get_been_triggered(self):
        return self.__been_triggered

    # The get_coordinates method returns the current coordinates of the bullet.
    def get_coordinates(self):
        return self.__coordinates
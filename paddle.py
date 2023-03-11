import pygame

class Paddle():
    
    # initializing everything -- By the way this class designed, it will create the paddle object so it is 
    # idenpendent of the other GUI components and not dependent on their movements. Each method can be called 
    # from the main program without having to know the information of the other GUI compenents that were created.
    # I chose to do instance variables in case someone wanted to modify my project and have two player game or something 
    # like that, then they would be able to make two GUI components that are completely independent of one another.
    def __init__(self, x, y, width, height, colour, speed):
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__width = width
        self.__height = height
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]
        self.__speed = speed

    # this method draws the paddle onto the screen
    def draw(self, display):
        pygame.draw.rect(display, self.__colour, self.__coordinates)

    # When the two move methods are called, it will change the x-coordinate to make the paddle appear to be moving along 
    # the x-axis
    def move_left(self):
        self.__coordinates[0] -= self.__speed # updating the coordinates

        # making sure the paddle doesn't go off of the screen
        if self.__coordinates[0] <= 0:
            self.__coordinates[0] = 0

    def move_right(self):
        self.__coordinates[0] += self.__speed # updating the coordinates
        
        # making sure the paddle doesn't go off of the screen
        if self.__coordinates[0] >= 440: 
            self.__coordinates[0] = 440
        
    # This returns the current coordinates of the paddle
    def get_coordinates(self):
        return self.__coordinates # [self.__x, self.__y, self.__width, self.__height]
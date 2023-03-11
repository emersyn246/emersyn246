import pygame
import random

class Bubble:
    # initiallizing everything -- These are all private variables. For the purpose of this assignment, the bubble 
    # is very independent from the other objects created in the main program. Once the bubble has been created in 
    # the main program, the main program will call the draw method and the move method, doing so when the pygame 
    # application is created and not dependent on other GUI components. The variables used in this class are all instance
    # variables. I chose to do instance variables in case someone wanted to modify my project and have two bubbles instead of
    # one, then they would be able to make two GUI components that are completely independent of one another.
    def __init__(self, x, y, radius, colour, speed_x, speed_y):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__coordinates = [self.__x, self.__y]
        self.__speed_y = speed_y
        self.__speed_x = speed_x
        self.__colour = colour

    # the method that draws the bubble
    def draw(self, display):
        pygame.draw.circle(display, self.__colour, self.__coordinates, self.__radius)

    # the method that controls the movements -- As of right now, the bubble will continuously move around the top of 
    # the screen without interruptions. If the bubble reaches either the left or right wall, it will switch directions
    # by multiplying the speed by -1. Now when the speed gets added to the x-coordinate, it will move in the opposite 
    # direction. When the bubble hits the line, it will trigger the randint method to pick a y-coordinate for the 
    # bubble to move to. 
    def move(self, horizontal_bound, vertical_bound):  
        
        # checking if the ball hit the right wall
        if self.__coordinates[0] >= horizontal_bound:
            self.__speed_x = -self.__speed_x

        # checking if the ball hit the left wall
        elif self.__coordinates[0] <= 0:
            self.__speed_x = -self.__speed_x
        
        # checking if the ball hit the line 
        elif self.__coordinates[1] > vertical_bound:
            self.__coordinates[1] = random.randint(0,vertical_bound)
            
        self.__coordinates[1] += self.__speed_y # moving along the y axis and updating the coordinates
        self.__coordinates[0] += self.__speed_x # moving along the x axis and updating the coordinates
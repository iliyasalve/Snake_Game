import pygame, random
from pygame.math import Vector2


class Obstacle:
    def __init__(self, cell_number, cell_size, screen, obstacle_color):

        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.obstacle_color = obstacle_color

        self.random_position()

    
    def draw_obstacle(self):
        '''
        Draw an obstacle
        '''

        obstacle_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, self.obstacle_color, obstacle_rect)


    def random_position(self):
        '''
        Obtaining coordinates for an obstacle
        '''

        self.x = random.randint(0, self.cell_number -1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
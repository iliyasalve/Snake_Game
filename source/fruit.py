import pygame, random
from pygame.math import Vector2


class Fruit:
    def __init__(self, cell_number, cell_size, screen, fruit_color):

        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.fruit_color = fruit_color

        self.random_position()
    

    def draw_fruit(self):
        '''
        Draw a fruit
        '''

        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, self.fruit_color, fruit_rect)


    def random_position(self):
        '''
        Obtaining coordinates for a fruit
        '''

        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
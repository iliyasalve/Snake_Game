import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self, cell_size, screen, snake_head_color, snake_tail_color):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.cell_size = cell_size
        self.screen = screen
        self.snake_head_color = snake_head_color
        self.snake_tail_color = snake_tail_color


    def draw_snake(self):
        '''
        Draw a snake
        '''

        for index, block in enumerate(self.body):
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)

            if index == 0:
                pygame.draw.rect(self.screen, self.snake_head_color, block_rect)
            else:
                pygame.draw.rect(self.screen, self.snake_tail_color, block_rect)

    def move_snake(self):
        '''
        Moving the snake
        '''

        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        '''
        Lengthen the snake's tail
        '''

        self.new_block = True

    def reset (self):
        '''
        Snake tail dump
        '''

        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
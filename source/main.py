import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.math import Vector2

from game import Game

# pygame initialisation
pygame.init()

# game settings
CELL_SIZE = 25 # number of lines
CELL_NUMBER = 24 # cells in one line

WINDOW_WIDTH = CELL_NUMBER * CELL_SIZE + ((CELL_NUMBER * CELL_SIZE) / 2) # 900
WINDOW_HEIGHT = CELL_NUMBER * CELL_SIZE # 600

MAIN_COLOR = (175, 215, 70)
GRASS_COLOR = (167, 209, 61)
TEXT_COLOR = (56, 74, 12)
SNAKE_HEAD_COLOR = (150, 75, 0)
SNAKE_TAIL_COLOR = (202, 147, 91)
FRUIT_COLOR = (0, 175, 0)
OBSTACLE_COLOR = (88,88,88)

NUMBER_OBSTACLES = 10
SNAKE_SPEED = 150

# font initialisation
pygame.font.init()

# checks whether the computer has the given font
if pygame.font.match_font("georgia"):
    path = pygame.font.match_font("georgia")
else:
    path = None
game_font = pygame.font.Font(path, 25)

# creating a window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, SNAKE_SPEED)

game = Game(CELL_NUMBER, 
            CELL_SIZE, 
            NUMBER_OBSTACLES, 
            screen, 
            game_font,
            TEXT_COLOR, 
            GRASS_COLOR,
            SNAKE_HEAD_COLOR,
            SNAKE_TAIL_COLOR,
            FRUIT_COLOR,
            OBSTACLE_COLOR)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            game.update()
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1: # so as not to turn 180 degrees
                    game.snake.direction = Vector2(0, -1)

            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)

            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)

    screen.fill(MAIN_COLOR)

    game.draw_elements()

    pygame.display.update()
    clock.tick(60)
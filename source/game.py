import os

import pygame
from pygame.math import Vector2

from fruit import Fruit
from snake import Snake
from obstacle import Obstacle


class Game:
    def __init__(self, cell_number, cell_size, number_obstacles, 
                 screen, game_font, text_color, 
                 grass_color, snake_head_color, snake_tail_color, fruit_color, obstacle_color):

        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.game_font = game_font
        self.grass_color = grass_color
        self.text_color = text_color
        self.obstacle_color = obstacle_color

        self.score = 0

        if os.path.exists('data/highscore.data'):
            with open("data/highscore.data", "r") as f:
                self.best_score = int(f.read())
        else:
            self.best_score = 0

        self.current_tries = 1

        if os.path.exists('data/total_tries.data'):
            with open("data/total_tries.data", "r") as f:
                self.total_tries = int(f.read()) + self.current_tries
        else:
            self.total_tries = 1

        self.number_obstacles = number_obstacles

        self.snake = Snake(self.cell_size, self.screen, snake_head_color, snake_tail_color)

        self.fruit = Fruit(self.cell_number, self.cell_size, self.screen, fruit_color)
        
        self.dic_obstacles = {}
        
        for i in range(self.number_obstacles):
            self.dic_obstacles["obstacle_rect" + str(i)] = Obstacle(self.cell_number, 
                                                                    self.cell_size, 
                                                                    self.screen, 
                                                                    self.obstacle_color)

 

    def update(self):
        '''
        Updates game elements
        '''

        self.snake.move_snake()
        self.check_collision()
        self.check_fail()


    def draw_elements(self):
        '''
        Draws game elements
        '''

        self.draw_grass()

        self.fruit.draw_fruit()

        for i in range (self.number_obstacles):
            self.dic_obstacles["obstacle_rect" + str(i)].draw_obstacle()

        self.snake.draw_snake()
        
        self.draw_title()

        self.draw_best_score()
        self.draw_score()

        self.draw_current_tries()
        self.draw_total_tries()

        self.draw_separate_lines()


    def check_collision(self):
        '''
        Checking collisions of different elements
        '''

        # check if the snake has eaten the fruit
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random_position()
            self.snake.add_block()

        # check if the fruit is placed on an obstacle
        for i in range (self.number_obstacles):
            if self.fruit.pos == self.dic_obstacles["obstacle_rect" + str(i)].pos:
                self.fruit.random_position()

        for bloc in self.snake.body[1:]:

            # check if the fruit is placed on the snake's tail
            if bloc == self.fruit.pos:
                self.fruit.random_position()
                
            # check if there is an obstacle on the snake's tail
            for i in range (self.number_obstacles):
                if bloc == self.dic_obstacles["obstacle_rect" + str(i)].pos:
                    self.dic_obstacles["obstacle_rect" + str(i)].random_position()


    def check_fail(self):
        '''
        Checking for game ending conditions
        '''

        # check if the snake goes beyond the playing field
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

        # check if the snake is trying to eat itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        # check if the snake has encountered an obstacle
        for i in range (self.number_obstacles):
            if self.dic_obstacles["obstacle_rect" + str(i)].pos == self.snake.body[0]:
                self.game_over()


    def draw_grass(self):
        '''
        Draws a chess field for the game
        '''
        
        for row in range(self.cell_number):
            for col in range(self.cell_number):
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
                    grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, self.grass_color, grass_rect)


    def draw_title(self):
        '''
        Draws the name of the game
        '''

        title = "Snake Game"

        title_surface = self.game_font.render(title, True ,self.text_color)

        pos_x = int(self.cell_size * self.cell_number + 150)
        pos_y = int(self.cell_size * self.cell_number - 520)
        
        title_rect = title_surface.get_rect(center = (pos_x, pos_y))

        self.screen.blit(title_surface, title_rect)


    def draw_score(self):
        '''
        Draws the game score
        '''

        title = "Score"
        self.score = len(self.snake.body) - 3
        score_text = str(self.score)

        title_surface = self.game_font.render(title, True ,self.text_color)
        score_surface = self.game_font.render(score_text, True ,self.text_color)

        pos_x = int(self.cell_size * self.cell_number + 150)
        pos_y = int(self.cell_size * self.cell_number - 370)

        text_rect = title_surface.get_rect(center = (pos_x, pos_y - 30))
        score_rect = score_surface.get_rect(center = (pos_x, pos_y))

        self.screen.blit(title_surface, text_rect)
        self.screen.blit(score_surface, score_rect)

    
    def draw_best_score(self):
        '''
        Draws the best score of the game
        '''

        title = "Best Score"
        best_score_text = str(self.best_score)

        title_surface = self.game_font.render(title, True ,self.text_color)
        best_score_surface = self.game_font.render(best_score_text, True ,self.text_color)

        pos_x = int(self.cell_size * self.cell_number + 150)
        pos_y = int(self.cell_size * self.cell_number - 290)

        title_rect = title_surface.get_rect(center = (pos_x, pos_y - 30))
        best_score_rect = best_score_surface.get_rect(center = (pos_x, pos_y))

        self.screen.blit(title_surface, title_rect)
        self.screen.blit(best_score_surface, best_score_rect)


    def draw_current_tries(self):
        '''
        Draws the number of game restarts in the current session
        '''

        title = "Current tries"
        best_score_text = str(self.current_tries)

        title_surface = self.game_font.render(title, True ,self.text_color)
        best_score_surface = self.game_font.render(best_score_text, True ,self.text_color)

        pos_x = int(self.cell_size * self.cell_number + 150)
        pos_y = int(self.cell_size * self.cell_number - 135)

        title_rect = title_surface.get_rect(center = (pos_x, pos_y - 30))
        best_score_rect = best_score_surface.get_rect(center = (pos_x, pos_y))

        self.screen.blit(title_surface, title_rect)
        self.screen.blit(best_score_surface, best_score_rect)


    def draw_total_tries(self):
        '''
        Draws the number of game restarts for the entire time 
        '''

        title = "Total tries"

        best_score_text = str(self.total_tries)

        title_surface = self.game_font.render(title, True ,self.text_color)
        best_score_surface = self.game_font.render(best_score_text, True ,self.text_color)

        pos_x = int(self.cell_size * self.cell_number + 150)
        pos_y = int(self.cell_size * self.cell_number - 60)

        title_rect = title_surface.get_rect(center = (pos_x, pos_y - 30))
        best_score_rect = best_score_surface.get_rect(center = (pos_x, pos_y))

        self.screen.blit(title_surface, title_rect)
        self.screen.blit(best_score_surface, best_score_rect)


    def draw_separate_lines(self):
        bg_rect = (0, 0, self.cell_number * self.cell_size + ((self.cell_number * self.cell_size) / 2), self.cell_number * self.cell_size)
        pygame.draw.rect(self.screen, self.text_color, bg_rect, 1)

        pygame.draw.line(self.screen, self.text_color, (self.cell_number * self.cell_size, 0), (self.cell_number * self.cell_size, self.cell_number * self.cell_size))

    
    def game_over(self):
        '''
        Game reset
        '''

        if self.score > self.best_score:
            self.best_score = self.score
            with open("data/highscore.data", "w") as f:
                f.write(str(self.best_score))

        self.snake.reset()

        self.fruit.random_position()

        for i in range(0, 10):
            self.dic_obstacles["obstacle_rect" + str(i)] = Obstacle(self.cell_number, self.cell_size, self.screen, self.obstacle_color)

        self.current_tries += 1
        self.total_tries += 1

        with open("data/total_tries.data", "w") as f:
            f.write(str(self.total_tries))

        # auto direction to the right to avoid the mistake of the snake eating itself cyclically
        self.snake.direction = Vector2(1, 0)
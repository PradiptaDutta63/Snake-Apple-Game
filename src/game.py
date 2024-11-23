#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from snake import Snake
from apple import Apple
import time

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.screen = pygame.display.set_mode((800, 800))
        self.snake = Snake(self.screen, 2)
        self.apple = Apple(self.screen)

    def play(self):
        self.snake.crawl()
        self.apple.draw()

        if self.snake.collide(self.snake.block_x[0], self.snake.block_y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.move("up")
                    elif event.key == pygame.K_DOWN:
                        self.snake.move("down")
                    elif event.key == pygame.K_LEFT:
                        self.snake.move("left")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.move("right")
            self.play()
            time.sleep(0.2)


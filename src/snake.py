#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import numpy as np

SIZE = 40

class Snake:
    def __init__(self, surface, length):
        self.parent_surface = surface
        self.length = length
        self.block_img = pygame.image.load("resources/block.jpg").convert()
        self.block_x = [SIZE * i for i in range(length)]
        self.block_y = [0] * length
        self.direction = "right"

    def draw(self):
        for i in range(self.length):
            self.parent_surface.blit(self.block_img, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()

    def move(self, direction):
        self.direction = direction

    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def crawl(self):
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == "up":
            self.block_y[0] -= SIZE
        elif self.direction == "down":
            self.block_y[0] += SIZE
        elif self.direction == "left":
            self.block_x[0] -= SIZE
        elif self.direction == "right":
            self.block_x[0] += SIZE

        self.draw()

    def collide(self, x1, y1, x2, y2):
        return x1 in range(x2, x2 + SIZE) and y1 in range(y2, y2 + SIZE)

    def outside_range(self):
        if self.block_x[0] >= self.parent_surface.get_width():
            self.block_x[0] = 0
        elif self.block_x[0] < 0:
            self.block_x[0] = self.parent_surface.get_width() - SIZE

        if self.block_y[0] >= self.parent_surface.get_height():
            self.block_y[0] = 0
        elif self.block_y[0] < 0:
            self.block_y[0] = self.parent_surface.get_height() - SIZE


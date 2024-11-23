#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random

SIZE = 40

class Apple:
    def __init__(self, surface):
        self.parent_surface = surface
        self.apple_img = pygame.image.load("resources/apple.jpg").convert()
        self.move()

    def draw(self):
        self.parent_surface.blit(self.apple_img, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = SIZE * random.randint(0, 19)
        self.y = SIZE * random.randint(0, 19)


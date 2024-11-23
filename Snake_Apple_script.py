import pygame
from pygame.locals import *
import random as random
import time
import numpy as np

SIZE = 40
BACKGROUND_COLOR = (36,238,170)
class Apple:
    def __init__(self, surface):
        self.parent_surface = surface
        self.apple_img = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE*random.randint(0,19)
        self.y = SIZE*random.randint(0,19)

    def draw(self):
        self.parent_surface.blit(self.apple_img,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = SIZE*random.randint(0,19)
        self.y = SIZE*random.randint(0,19)

class Snake:
    def __init__(self, surface, length):
        self.parent_surface = surface
        self.length = length
        self.block_img = pygame.image.load("resources/block.jpg").convert()
        self.block_x = [random.choice(np.arange(0,self.parent_surface.get_width()- self.block_img.get_width(),40))]*length
        self.block_y = [random.choice(np.arange(0,self.parent_surface.get_height()- self.block_img.get_height(),40))]*length
        self.direction = "right"

    def draw(self):
        for i in range(self.length):
            self.parent_surface.blit(self.block_img, (self.block_x[i],self.block_y[i]))
        pygame.display.flip()


    def move(self, key_pressed):
        self.direction = key_pressed


    def increase_length(self):
        self.length += 1
        self.block_x.append(1)
        self.block_y.append(1)

    def crawl(self):

        for i in range(self.length-1,0,-1):
            self.block_x[i] = self.block_x[i-1]
            self.block_y[i] = self.block_y[i-1]

        if self.direction == "up":
            self.block_y[0] += -SIZE
        if self.direction == "down":
            self.block_y[0] += SIZE
        if self.direction == "left":
            self.block_x[0] += -SIZE
        if self.direction == "right":
            self.block_x[0] += SIZE
        self.draw()


    def collide(self, x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    
    
    def outside_range(self):
        if (self.block_x[0] > self.parent_surface.get_width()):
            self.block_x[0] = 0
        elif (self.block_x[0] < 0):
            self.block_x[0] = self.parent_surface.get_width() - self.block_img.get_width()

        if self.block_y[0] > self.parent_surface.get_height():
            self.block_y[0] = 0 
        elif self.block_y[0] < 0:
            self.block_y[0] = self.parent_surface.get_height() - self.block_img.get_height()


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_bg_music()
        pygame.display.set_caption("SNAKE")
        self.screen = pygame.display.set_mode((800,800))
        self.snake = Snake(self.screen,2)
        self.apple = Apple(self.screen)


    def score(self):
        font = pygame.font.SysFont("arial", 30, bold=True)
        score = font.render(f"Score: {self.snake.length-2}", True, (225,225,225), (0,0,0))
        self.screen.blit(score, (600,10))
        pygame.display.flip()


    def background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.screen.blit(bg, (0,0))

    def play_bg_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def play_sound(self,sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play(self):
        self.background()
        self.snake.crawl()
        self.apple.draw()
        self.score()

        #snake and apple colliding
        if self.snake.collide(self.snake.block_x[0],self.snake.block_y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        #snake and snake colliding
        for i in range(3,self.snake.length):
            if self.snake.collide(self.snake.block_x[0],self.snake.block_y[0], self.snake.block_x[i], self.snake.block_y[i]):
                self.play_sound("crash")
                raise "Game Over"


    def show_game_over(self):
        self.screen.fill((36,238,170))
        font = pygame.font.SysFont("arial", 40, bold=True)
        l1_game_over = font.render("Game Over", True, (255,255,255))
        self.screen.blit(l1_game_over,(200,400))
        l2_play_again = font.render("To play again press ENTER",True, (255,255,255))
        self.screen.blit(l2_play_again,(200,200))
        l3_score = font.render(f"Your Score : {self.snake.length-2}", True, (255,255,255))
        self.screen.blit(l3_score,(200,300))
        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset_game(self):
        self.snake = Snake(self.screen,2)
        self.apple = Apple(self.screen)

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move("up")
                        if event.key == K_DOWN:
                            self.snake.move("down")
                        if event.key == K_LEFT:
                            self.snake.move("left")
                        if event.key == K_RIGHT:
                            self.snake.move("right")

                elif event.type == pygame.QUIT:
                    running = False

            try:
                if not pause:
                    self.snake.outside_range()
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset_game()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()

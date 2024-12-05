import pygame
from pygame.locals import *

from Ball import Ball
from Brick import Brick
from Player import Player

class Game:
    def __init__(self, width=1280, height=720):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.BRICK_MARGIN = 10

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.ball = None
        self.player = Player(self)
        self.bricks = self.gen_bricks()



    def gen_bricks(self):
        bricks_i = 10
        bricks_j = 10
        bricks = []

        # bricks
        for i in range(bricks_i):
            for j in range(bricks_j):
                bricks.append(Brick(self, i, j))

        return bricks

    def new_ball(self):
        self.ball = Ball(self)
        return self.ball

    def get_delta_time(self):
        my_fps = self.clock.get_fps() if self.clock.get_fps() != 0 else 1
        return 1/my_fps

    def get_debug_info(self):
        fps = self.clock.get_fps()
        return f"fps: {int(fps)}, {round(self.get_delta_time(), 6)} ms, you are {'dead' if self.ball and self.ball.dead else 'alive'}"

    def show_debug_info(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = font.render(self.get_debug_info(), True, pygame.Color("grey"))
        self.screen.blit(text_surface, (0, 0))


    def on_key_press(self, keys_pressed):
        if keys_pressed[K_DELETE]:
            self.ball = self.new_ball()
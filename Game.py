import pygame
from pygame import Vector2
from pygame.locals import *

from Ball import Ball
from Brick import Brick
from Paddle import Paddle

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
        self.player = Paddle(self)
        self.bricks = self.gen_bricks()


    def gen_bricks(self):
        bricks_i = 50
        bricks_j = 50
        bricks = []

        # bricks
        for i in range(bricks_i):
            for j in range(bricks_j):

                brick_size = Vector2(
                    self.SCREEN_WIDTH / (bricks_i * 2 +1),
                    self.SCREEN_HEIGHT / (bricks_j * 2 +1))

                brick_pos = Vector2(
                    brick_size.x + i * (brick_size.x * 2),
                    brick_size.y + j * (brick_size.y * 2)
                )

                bricks.append(Brick(self, brick_size, brick_pos))

        return bricks

    def new_ball(self):
        self.ball = Ball(self)
        return self.ball

    def get_delta_time(self):
        return self.clock.tick() / 1000

    def get_debug_info(self):
        fps = self.clock.get_fps()
        return f"fps: {int(fps)}, {round(self.get_delta_time()*1000, 3)} ms, {len(self.bricks)} bricks left, you are {'dead' if self.ball and self.ball.dead else 'alive'}"

    def show_debug_info(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = font.render(self.get_debug_info(), True, pygame.Color("grey"))
        self.screen.blit(text_surface, (0, 0))


    def on_key_press(self, keys_pressed):
        if keys_pressed[K_DELETE]:
            self.ball = self.new_ball()


    def delete_brick(self, brick: Brick):
        self.bricks.remove(brick)
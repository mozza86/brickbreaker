import pygame
from pygame import Vector2


class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Ball, self).__init__()
        self.game = game

        self.surf = pygame.image.load("assets/ball.png")
        self.surf.convert()
        size = 40
        self.surf = pygame.transform.scale(self.surf, (size, size))

        self.position = Vector2(self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)
        self.rect = self.surf.get_rect(center=self.position)

        self.velocity = Vector2(1, 1)

        self.speed = 10

        self.dead = False


    def update(self, paddle):
        if self.dead:
            self.surf.fill(pygame.Color("red"))
            return

        if self.rect.x > self.game.SCREEN_WIDTH - self.rect.width or self.rect.x <= 0:  # East/West
            self.velocity = self.velocity.reflect(Vector2(-1, 0))
        if self.rect.y <= 0:  # Top
            self.velocity = self.velocity.reflect(Vector2(0, 1))


        if self.rect.colliderect(paddle.rect):
            self.velocity = self.velocity.reflect(Vector2(0, -1))


        if self.rect.y > self.game.SCREEN_HEIGHT:
            print("YOU DEAD")
            self.dead = True

        before_vel = self.velocity

        delta_time = max(self.game.get_delta_time(), 0.001)
        self.velocity = self.velocity.normalize() * delta_time * 1000 * self.speed

        #print(f"norm+speed: {before_vel} -> {self.velocity}")

        self.rect.move_ip(self.velocity)

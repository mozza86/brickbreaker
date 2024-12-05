import pygame
from pygame.locals import K_LEFT, K_RIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Player, self).__init__()
        self.game = game
        self.surf = pygame.Surface((150, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

        self.rect.x = (self.game.SCREEN_WIDTH / 2) - self.surf.get_width() / 2
        self.rect.y = self.game.SCREEN_HEIGHT - self.surf.get_height() - self.surf.get_height() / 2

        self.speed = 2


    def update(self, pressed_keys):

        mousex, mousey = pygame.mouse.get_pos()

        self.rect.centerx = mousex


        move = self.speed * self.game.get_delta_time() * 1000
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-move, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(move, 0)

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= self.game.SCREEN_WIDTH-self.rect.width:
            self.rect.x = self.game.SCREEN_WIDTH-self.rect.width

import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, game, brick_size, brick_pos):
        super(Brick, self).__init__()
        self.game = game

        self.surf = pygame.Surface(brick_size)
        self.surf.fill(pygame.Color("#915240"))
        self.rect = self.surf.get_rect(center=brick_pos)


    def update(self):
        if self.game.ball and self.rect.colliderect(self.game.ball):
            self.game.delete_brick(self)

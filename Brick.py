import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, game, i, j):
        super(Brick, self).__init__()
        self.game = game
        self.surf = pygame.Surface((117, 50))
        self.surf.fill(pygame.Color("magenta"))
        self.rect = self.surf.get_rect()

        self.i = i
        self.j = j

        self.rect.x = game.BRICK_MARGIN + i*(self.surf.get_width()+game.BRICK_MARGIN)
        self.rect.y = game.BRICK_MARGIN + j*(self.surf.get_height()+game.BRICK_MARGIN)

    def update(self):
        if not self.game.ball:
            self.surf.fill(pygame.Color("black"))
            return

        self.surf.fill(pygame.Color("green"))

        if self.game.ball.rect.y <= self.rect.y:
            self.surf.fill(pygame.Color("aqua"))
        if self.game.ball.rect.y+self.game.ball.rect.height >= self.rect.y+self.rect.height:
            self.surf.fill(pygame.Color("purple"))

        if self.game.ball.rect.x <= self.rect.x:
            self.surf.fill(pygame.Color("orange"))
        if self.game.ball.rect.x+self.game.ball.rect.width >= self.rect.x+self.rect.width:
            self.surf.fill(pygame.Color("red"))

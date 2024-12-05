import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Ball, self).__init__()
        self.game = game


        # self.surf = pygame.Surface((20, 20))
        # self.surf.fill(pygame.Color("blue"))

        self.surf = pygame.image.load("assets/ball.png")
        self.surf.convert()
        self.surf = pygame.transform.scale(self.surf, (20, 20))
        self.rect = self.surf.get_rect()

        self.rect.x = (game.SCREEN_WIDTH  / 2) - self.surf.get_width()  / 2  # x
        self.rect.y = (game.SCREEN_HEIGHT / 2) - self.surf.get_height() / 2  # y


        self.speed = 0.25
        self.speed = 0.4
        self.directionX = 1
        self.directionY = 1

        self.dead = False

    def update(self, player):
        if self.dead:
            self.surf.fill(pygame.Color("red"))
            return

        moveX = self.speed * self.game.get_delta_time() * 1000
        moveY = self.speed * self.game.get_delta_time() * 1000

        if self.rect.x > self.game.SCREEN_WIDTH-self.rect.width:
            self.directionX = -abs(self.directionY)

        if self.rect.y+self.rect.height > player.rect.y:
            if self.rect.x > player.rect.x:
                if self.rect.x+self.rect.width < player.rect.x+player.rect.width:
                    self.directionY = -abs(self.directionY)

        if self.rect.y > self.game.SCREEN_HEIGHT-self.rect.height:
            print("YOU DEAD")

        if self.rect.y > self.game.SCREEN_HEIGHT-self.rect.height:
            self.dead = True

        if self.rect.x <= 0:
            self.directionX = abs(self.directionY)
        if self.rect.y <= 0:
            self.directionY = abs(self.directionY)


        if self.directionX == 1:
            self.rect.x += moveX
        else:
            self.rect.x -= moveX

        if self.directionY == 1:
            self.rect.y += moveY
        else:
            self.rect.y -= moveY

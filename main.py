import pygame
from pygame import K_KP_ENTER
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_DELETE,
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BRICK_MARGIN = 10

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((150, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

        self.rect.x = (SCREEN_WIDTH / 2) - self.surf.get_width() / 2
        self.rect.y = SCREEN_HEIGHT - self.surf.get_height() - self.surf.get_height() / 2

        self.speed = 2


    def update(self, pressed_keys):
        move = self.speed * get_deltaTime()*1000
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-move, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(move, 0)

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SCREEN_WIDTH-self.rect.width:
            self.rect.x = SCREEN_WIDTH-self.rect.width

class Brick(pygame.sprite.Sprite):
    def __init__(self, i, j):
        super(Brick, self).__init__()
        self.surf = pygame.Surface((117, 50))
        self.surf.fill(pygame.Color("magenta"))
        self.rect = self.surf.get_rect()

        self.i = i
        self.j = j

        self.rect.x = BRICK_MARGIN + i*(self.surf.get_width()+BRICK_MARGIN)
        self.rect.y = BRICK_MARGIN + j*(self.surf.get_height()+BRICK_MARGIN)

    def update(self):
        if not ball:
            self.surf.fill(pygame.Color("black"))
            return

        self.surf.fill(pygame.Color("green"))

        if ball.rect.y <= self.rect.y:
            self.surf.fill(pygame.Color("aqua"))
        if ball.rect.y+ball.rect.height >= self.rect.y+self.rect.height:
            self.surf.fill(pygame.Color("purple"))

        if ball.rect.x <= self.rect.x:
            self.surf.fill(pygame.Color("orange"))
        if ball.rect.x+ball.rect.width >= self.rect.x+self.rect.width:
            self.surf.fill(pygame.Color("red"))
        

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20, 20))

        self.surf.fill(pygame.Color("blue"))
        self.rect = self.surf.get_rect()

        self.rect.x = (SCREEN_WIDTH  / 2) - self.surf.get_width()  / 2  # x
        self.rect.y = (SCREEN_HEIGHT / 2) - self.surf.get_height() / 2  # y


        self.speed = 0.25
        self.speed = 0.4
        self.directionX = 1
        self.directionY = 1

        self.dead = False

    def update(self):
        if self.dead:
            self.surf.fill(pygame.Color("red"))
            return

        moveX = self.speed * get_deltaTime()*1000
        moveY = self.speed * get_deltaTime()*1000

        if self.rect.x > SCREEN_WIDTH-self.rect.width:
            self.directionX = -1

        if self.rect.y+self.rect.height > player.rect.y:
            if self.rect.x > player.rect.x:
                if self.rect.x+self.rect.width < player.rect.x+player.rect.width:
                    self.directionY = -1

        if self.rect.y > SCREEN_HEIGHT-self.rect.height:
            print("YOU DEAD")

        if self.rect.y > SCREEN_HEIGHT-self.rect.height:
            self.dead = True

        if self.rect.x <= 0:
            self.directionX = 1
        if self.rect.y <= 0:
            self.directionY = 1


        if self.directionX == 1:
            self.rect.x += moveX
        else:
            self.rect.x -= moveX

        if self.directionY == 1:
            self.rect.y += moveY
        else:
            self.rect.y -= moveY



def get_deltaTime():
    my_fps = clock.get_fps() if clock.get_fps() != 0 else 1
    return 1/my_fps


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
ball = None

bricks_i = 10
bricks_j = 10
bricks = []

# bricks
for i in range(bricks_i):
    for j in range(bricks_j):
        bricks.append(Brick(i, j))

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

running = True
while running:
    clock.tick()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Fill the background with white
    screen.fill(pygame.Color("white"))

    # player

    player.update(pygame.key.get_pressed())
    screen.blit(player.surf, player.rect)



    for brick in bricks:
        brick.update()
        screen.blit(brick.surf, brick.rect)

    if pygame.key.get_pressed()[K_DELETE]:
        ball = Ball()

    # ball
    if ball:
        ball.update()
        screen.blit(ball.surf, ball.rect)

    fps = clock.get_fps()
    text_surface = font.render(f"fps: {int(fps)}, {round(get_deltaTime(), 6)} ms, you are {'dead' if ball and ball.dead else 'alive'}", True, pygame.Color("grey"))
    screen.blit(text_surface, (0, 0))

    #clock.tick(100)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

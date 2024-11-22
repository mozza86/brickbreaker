from sys import displayhook

import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
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


    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super(Brick, self).__init__()
        self.surf = pygame.Surface((117, 50))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player()
    ball = Ball()

    bricks_i = 10
    bricks_j = 3
    bricks = [Brick() for _ in range(bricks_i + bricks_j)]

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
        screen.fill((255, 255, 255))

        # bricks
        for i in range(10):
            for j in range(3):
                cur_brick = bricks[i+j]
                screen.blit(cur_brick.surf, (
                    BRICK_MARGIN + i*(cur_brick.surf.get_width()+BRICK_MARGIN),
                    BRICK_MARGIN + j*(cur_brick.surf.get_height()+BRICK_MARGIN),
                ))

        # ball
        screen.blit(ball.surf, (
            (SCREEN_WIDTH  / 2) - ball.surf.get_width()  / 2,  # x
            (SCREEN_HEIGHT / 2) - ball.surf.get_height() / 2,  # y
        ))

        # player
        screen.blit(player.surf, player.rect)

        # Update the player sprite based on user keypresses
        player.update(pygame.key.get_pressed())


        fps = str(int(clock.get_fps()))
        text_surface = font.render(f"fps: {fps}", True, (255, 0, 0))
        screen.blit(text_surface, (0, 0))

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__ == '__main__':
    main()
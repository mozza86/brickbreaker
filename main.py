import pygame
from pygame.locals import *

from Game import Game

def main():
    game = Game(1280, 720)

    running = True
    while running:
        game.clock.tick()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        # Fill the background with white
        game.screen.fill(pygame.Color("white"))

        game.on_key_press(pygame.key.get_pressed())

        # player
        game.player.update(pygame.key.get_pressed())
        game.screen.blit(game.player.surf, game.player.rect)

        for brick in game.bricks:
            brick.update()
            game.screen.blit(brick.surf, brick.rect)

        # ball
        if game.ball:
            game.ball.update(game.player)
            game.screen.blit(game.ball.surf, game.ball.rect)


        game.show_debug_info()

        #clock.tick(100)
        pygame.display.flip()



    # Done! Time to quit.
    pygame.quit()


if __name__ == '__main__':
    main()
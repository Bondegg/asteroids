import pygame
from constants import *
import player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_active_flag = True

    player_sprite = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    game_clock = pygame.time.Clock()
    dt = 0

    while game_active_flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        game_clock.tick(60)
        dt = (game_clock.tick() / 1000)
            
        screen.fill("black")

        
        player_sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

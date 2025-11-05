import pygame
from constants import *
import player
import shot
import asteroid
import asteroidfield
import sys

def main():
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_active_flag = True

    # Class containers to more efficently update all instances of a given class.
    player.Player.containers = (updateable, drawable)
    asteroid.Asteroid.containers = (updateable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updateable,)
    shot.Shot.containers = (shots, updateable)


    # x/y variables set to set the player sprite middle of the screen on start.
    player_sprite = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield_init = asteroidfield.AsteroidField()
    game_clock = pygame.time.Clock()
    dt = 0
    
    # game_active_flag is irrelevant, just to keep while loop running, use pygame.QUIT to exit game.
    while game_active_flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = (game_clock.tick(60) / 1000)
            
        screen.fill("black")

        updateable.update(dt)

        for a in asteroids:
            if a.collision_check(player_sprite):
               print("Game over!")
               sys.exit()

        for d in drawable:
            d.draw(screen)

        for s in shots:
            s.draw(screen)
        

        pygame.display.flip()


if __name__ == "__main__":
    main()

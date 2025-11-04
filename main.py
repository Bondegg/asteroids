import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_active_flag = True

    game_clock = pygame.time.Clock()
    dt = 0

    while game_active_flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        game_clock.tick(60)
        dt = (game_clock.tick() / 1000)
            
        screen.fill("black")

        pygame.display.flip()


if __name__ == "__main__":
    main()

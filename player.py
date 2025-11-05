from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame

class Player(CircleShape):
    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_timer = 0
        
    def triangle(self):
        # Prebuilt create the points for the triangle shape
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon((screen), "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity = direction * PLAYER_SHOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    # Key press assignments
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt
        
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot()

        

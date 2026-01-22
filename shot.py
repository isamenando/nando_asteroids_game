import pygame
from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # in the Shot class
    def draw(self, screen):
        # Draw the shot as a circle
        # The center is at (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
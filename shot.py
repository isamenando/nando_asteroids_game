import pygame
from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape

# Define the Shot class that inherits from CircleShape
# The shot has a radius of SHOT_RADIUS
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # Draw the shot as a circle
    def draw(self, screen):
        # Draw the shot as a circle
        # The center is at (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    # Update the shot's position based on its velocity 
    def update(self, dt):
        self.position += (self.velocity * dt)
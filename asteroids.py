import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape

# Define the Asteroid class that inherits from CircleShape
# The asteroid has a radius passed in the constructor
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw the asteroid as a circle
    def draw(self, screen):
        # Draw the asteroid as a circle
        # The center is at (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)
    
    # Update the asteroid's position based on its velocity
    # The velocity is a pygame.Vector2 object
    def update(self, dt):
        self.position += (self.velocity * dt)
import random
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event

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
    
    def split(self):
        self.kill()
        # Create two smaller asteroids at the same position
        # Each smaller asteroid has half the radius of the original
        # The smaller asteroids should move faster than the original
        # The smaller asteroids should move in random directions
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_asteroid_1_vector = self.velocity.rotate(random_angle)
            new_asteroid_2_vector = self.velocity.rotate(-random_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid1.velocity = new_asteroid_1_vector * 1.2
            asteroid2.velocity = new_asteroid_2_vector * 1.2
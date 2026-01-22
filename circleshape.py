import pygame

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

    # Check for collision with another CircleShape
    def collides_with(self, other):
        # Calculate the distance between the two circles
        # If the distance is less than or equal to the sum of their radii, they collide
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        else:
            return False

    def draw(self, screen):
        # self.screen = screen
        # self.position = position
        # self.velocity = velocity
        # self.radius = radius
        pass

    def update(self, dt):
        # must override
        pass
import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    # in the Player class
    def triangle(self):
        # Calculate the points of the triangle representing the player
        # The triangle is centered at the player's position
        # The triangle points in the direction of self.rotation
        # Return a list of three pygame.Vector2 points
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # in the Player class
    # Draw the player as a triangle
    # The points of the triangle can be obtained from self.triangle()
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    # in the Player class
    # Rotate the player by PLAYER_TURN_SPEED degrees per second
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # in the Player class
    # Update the player based on keyboard input
    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Rotate and move the player based on key presses
        # A and D to rotate left and right
        # W and S to move forward and backward
        # Space to shoot
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    # in the Player class
    # Move the player in the direction it is facing
    # The speed is PLAYER_SPEED units per second
    # The direction is determined by self.rotation
    # The movement is applied to self.position
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    # in the Player class
    # Shoot a shot in the direction the player is facing
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    # Group holding all the objects that can be updated
    updatable = pygame.sprite.Group()
    # Group holding all the objects that can be drawn
    drawable = pygame.sprite.Group()
    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
        # print(dt)
                        

if __name__ == "__main__":
    main()

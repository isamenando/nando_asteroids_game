import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    while pygame:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # def Player(self):
        #     def __init__(self, x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2):
        #         super().__init__(x, y)
        #         self.rotation = 0

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
        # print(dt)
                        

if __name__ == "__main__":
    main()

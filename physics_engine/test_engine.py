import pygame
from player_movement import PlayerMovement

class BasicGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Testing Player Movement Class")
        self.clock = pygame.time.Clock()
        self.player = PlayerMovement(position=[400, 300], speed=100.0, direction=[1, 0])
        self.player.grounded = True  # Ensure player starts grounded
        self.player.GRAVITY = -9.81  # Set gravity constant
        self.player.jump_velocity = 5.0  # Set jump velocity

    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(60) / 1000  # Amount of seconds between each loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            # WASD movement
            if keys[pygame.K_a]:
                dx = -1
            elif keys[pygame.K_d]:
                dx = 1
            if keys[pygame.K_w]:
                dy = -1
            elif keys[pygame.K_s]:
                dy = 1
            elif keys[pygame.K_SPACE]:
                self.player.jump(delta_time)

            # Jump with spacebar
            if keys[pygame.K_SPACE]:
                self.player.jump(delta_time)

            self.player.set_direction(dx, dy)
            self.player.move_player(delta_time)

            self.screen.fill((0, 0, 0))
            if self.player.grounded:
                color = (255, 0, 0)  # Red when grounded
            else:
                color = (0, 255, 0)  # Green when jumping
            pygame.draw.rect(self.screen, color, (*self.player.get_position(), 50, 50))
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = BasicGame()
    game.run()
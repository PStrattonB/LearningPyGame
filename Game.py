import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):
        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)
        self.level = 1.0

        # Creates the game window
        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.background = GameObject(0, 0, self.width, self.height, 'assets/background.png')
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')

        self.level = 1.0  # setting level to 1

        self.reset_map()  # initialize the map

        # Create a clock variable
        self.clock = pygame.time.Clock()

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

    def draw_objects(self):
        self.game_window.fill(self.white_colour)  # Colours the background white

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))  # sets background to center on the game window at 0, 0 coords
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        # This will render any graphics updates so call this after drawing and filling in all colours
        pygame.display.update()

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
            if self.detect_collision(self.player, self.treasure):
                self.level += 0.5
                return True
            return False

    def reset_map(self):
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)

        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 400, 50, 50, 'assets/enemy.png', speed),
                Enemy(0, 200, 50, 50, 'assets/enemy.png', speed)
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 400, 50, 50, 'assets/enemy.png', speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/enemy.png', speed),
            ]

    def run_game_loop(self):

        player_direction = 0

        while True:
            # Handle events
            # Execute logic
            # Update display
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.KEYDOWN:  # detects if any key has been pressed
                    if event.key == pygame.K_UP:  # detects if key was up arrow
                        player_direction = -1  # moves character up
                    elif event.key == pygame.K_DOWN:  # detects if key was down arrow
                        player_direction = 1  # moves character down

                elif event.type == pygame.KEYUP:  # detects if a key was let go
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # detects if that key was the up or down arrow
                        player_direction = 0  # sets movement to 0

            self.player.move(player_direction, self.height)
            self.move_objects(player_direction)

            self.draw_objects()

            if self.check_if_collided():
                self.reset_map()

            # Setting how many times per sec we want to update the game window
            self.clock.tick(60)

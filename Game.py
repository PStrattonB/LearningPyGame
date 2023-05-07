import pygame

class Game:

    def __init__(self):
        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)

        # Creates the game window
        self.game_window = pygame.display.set_mode((self.width, self.height))

        background = pygame.image.load("assets/background.png")  # Set background image
        self.background = pygame.transform.scale(background, (800, 800))  # Scale background to size of game window

        treasure = pygame.image.load("assets/treasure.png")  # Set treasure asset image
        self.treasure = pygame.transform.scale(treasure, (50, 50))  # Scale treasure asset to appropriate size

        # Create a clock variable
        self.clock = pygame.time.Clock()

    def draw_objects(self):
        # Colours the background white
        self.game_window.fill(self.white_colour)
        self.game_window.blit(self.background, (0, 0))  # sets background to center on the game window at 0, 0 coords
        self.game_window.blit(self.treasure, (375, 50))

        # This will render any graphics updates so call this after drawing and filling in all colours
        pygame.display.update()

    def run_game_loop(self):

        while True:
            # Handle events
            # Execute logic
            # Update display
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return

            self.draw_objects()

            # Setting how many times per sec we want to update the game window
            self.clock.tick(60)

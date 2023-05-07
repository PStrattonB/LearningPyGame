import pygame
pygame.init()  #Before using anything from pyGame it needs to be initialized?

width = 800
height = 800
white_colour = (255, 255, 255)

# Creates the game window
game_window = pygame.display.set_mode((width, height))

# Create a clock variable
clock = pygame.time.Clock()


def run_game_loop():

    while True:
        # Handle events
        # Execute logic
        # Update display
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # Colours the background white
        game_window.fill(white_colour)
        # This will render any graphics updates so call this after drawing and filling in all colours
        pygame.display.update()

        # Setting how many times per sec we want to update the game window
        clock.tick(60)


run_game_loop()


pygame.quit()
quit()  # shutdown any Pygame functionality and close the program properly.


"""if __name__ == '__main__':
"""
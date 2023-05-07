import pygame
pygame.init()  #Before using anything from pyGame it needs to be initialized?

width = 800
height = 800
white_colour = (255, 255, 255)
game_window = pygame.display.set_mode((width, height))


while True:
    game_window.fill(white_colour)
    pygame.display.update()  # This will render any graphics updates so call this after drawing and filling in all colours

pygame.quit()
quit()  # shutdown any Pygame functionality and close the program properly.


"""if __name__ == '__main__':
"""
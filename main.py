import pygame
from Game import Game
pygame.init()  #Before using anything from pyGame it needs to be initialized?

game = Game()
game.run_game_loop()


pygame.quit()
quit()  # shutdown any Pygame functionality and close the program properly.


"""if __name__ == '__main__':
"""
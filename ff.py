import sys
import pygame


class Romvesenerinvasjon:
    """Overordnet klasse for å slå sammen spillressurser og oppførsel"""

    def __init__(self):
        """Initialisering av spillet"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Romvesener er her")

    def run_spille(self):
        """Her er while-løkken for spillet"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


if __name__ == '__main__':
    ri = Romvesenerinvasjon()
    ri.run_spille()
import sys
"her importerer jeg pygame"
import pygame
from settings import Settings
class Romvesenerinvasjon:
    """overordnet klasse for å slå sammen spillressurser og oppførsel"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Romvesener er her")

    def run_spille(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_farge)
            pygame.display.flip()

if __name__ == '__main__':
    ri = Romvesenerinvasjon()
    ri.run_spille()


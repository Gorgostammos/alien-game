import sys
"her importerer jeg pygame"
import pygame

from settings import Settings
from fly import Fly
class Romvesenerinvasjon:
    """overordnet klasse for å slå sammen spillressurser og oppførsel"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Romvesener er her")

        self.fly = Fly(self)

    def run_spille(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.fly.update()
            self.update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.fly.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.fly.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.fly.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fly.moving_left = False

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_farge)
        self.fly.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ri = Romvesenerinvasjon()
    ri.run_spille()
"""Class to manage buttons displayed on-screen."""
import pygame.font


class Button:
    """Class for creating and drawing buttons."""

    def __init__(self, game_instance, message):
        """Initialize button attributes."""
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.dimentions = [100, 50]  # width, height
        self.color = {
                'button': game_instance.setup.colors['button_color'],
                'text': game_instance.setup.colors['bttn_txt_color'],
                }
        self._prepare_message(message)

    def _prepare_message(self, msg):
        """
        Turn msg into a rendered image.

        Center the text on the button.
        """
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(0, 0, self.dimentions[0], self.dimentions[1])
        self.rect.center = self.screen_rect.center
        self.msg_image = self.font.render(msg, True, self.color['text'],
                                          self.color['button'])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button, message on top, then display on screen."""
        self.screen.fill(self.color['button'], self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

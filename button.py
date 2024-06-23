"""Class to manage buttons displayed on-screen."""
import pygame.font


class Button:
    """Class for creating and drawing buttons."""

    def __init__(self, game_instance, message):
        """Initialize button attributes."""
        self.instance = game_instance
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.color = {
                'button': game_instance.setup.color['button'],
                'text': game_instance.setup.color['bttn_txt'],
                }
        self._prepare_message(message)

    def _prepare_message(self, msg):
        """
        Turn msg into a rendered image.

        Center the text on the button.
        """
        # Set button dimentions, font_size as relative to screen rez.
        dimensions = [self.instance.setup.resolution[0] *.15,
                           self.instance.setup.resolution[1] *.1]  # w x h
        font_size = int(self.instance.setup.resolution[0] * .10)
        self.font = pygame.font.SysFont(None, font_size)
        self.rect = pygame.Rect(0, 0, dimensions[0], dimensions[1])
        self.rect.center = self.screen_rect.center
        self.msg_image = self.font.render(msg, True, self.color['text'],
                                          )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button, message on top, then display on screen."""
        self.screen.fill(self.color['button'], self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

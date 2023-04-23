"""Class to manage buttons displayed on-screen."""
import pygame.font


class Button:
    """Class for creating and drawing buttons."""

    def __init__(self, game_instance, message):
        """Initialize button attributes."""
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.setup = game_instance.setup
        self.width, self.height = 100, 50
        self.button_color = self.setup.button_color
        self.text_color = self.setup.bttn_txt_color
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prepare_message(message)

    def _prepare_message(self, msg):
        """
        Turn msg into a rendered image and center the text on
        the button.
        """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button, message on top, then display on screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

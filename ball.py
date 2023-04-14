"""Module to manage the creation of the balls."""


import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """Class to generate the tennis ball.

    Arguments:
            game_instance - the instance of class TableTennis
    """

    def __init__(self, game_instance):
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.setup = game_instance.setup
        self.color = self.setup.ball_color
        self.rect = pygame.Rect(0, 0, self.setup.ball_radius,
                                self.setup.ball_radius)
        self.rect.center = self.screen_rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        # The above lines will be needed when the pace of thegame speeds
        # up in later levels.

    def update(self):
        """Update the ball's position on screen."""
        self.rect.x += self.setup.ball_speed
        if self.rect.right >= self.screen_rect.right:
            self.setup.points -= self.setup.score
            self.rect.center = self.screen_rect.center

    def draw_ball(self):
        """Draw the ball to the screen."""
        pygame.draw.rect(self.screen, self.color, self. rect)

"""Module to manage the creation of the paddles."""

import sys

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    """Class to generate the paddles.

    Arguments:
            game_instance - the instance of class TableTennis
            location - Which side of the screen to put the paddle.
                       Options: 'L', 'R'
    """

    def __init__(self, game_instance, location):
        """Initialize a paddle instance.

        game_instance = an instance of class TableTennis()
        location is a single character 'L' or 'R' denoting the side of
        the screen to place the paddle.
        Calls super(). __init__() first.
        """
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.ball = game_instance.ball
        self.setup = game_instance.setup
        self.stats = game_instance.stats
        self.color = self.setup.color['paddle']
        self.rect = pygame.Rect(0, 0, self.setup.paddle['x'],
                                self.setup.paddle['y'])
        if location not in ('R', 'L'):
            print(f'\nError! Invalid paddle location {location}')
            print('Error most likely in __init__(self) in main.py.')
            sys.exit()
        if location == 'R':
            self.rect.right = self.screen_rect.right - self.rect.width
        elif location == 'L':
            self.rect.left = self.screen_rect.left + self.rect.width
        self.rect.centery = self.screen_rect.centery
        # Needed when the pace of the game speeds up in later levels:
        self.y = float(self.rect.y)  # pylint: disable=invalid-name

    def update(self, *args, **kwargs):
        """Update the paddle's position on screen."""
        # Ball will change direction if it collides with playing_area_border
        play_area_border = 5
        if self.setup.paddle['moving_up'] and self.rect.top > play_area_border:
            self.rect.y -= self.stats.paddle_speed
        if (self.setup.paddle['moving_down'] and
                self.rect.bottom < (self.screen_rect.bottom - play_area_border)):
            self.rect.y += self.stats.paddle_speed

    def tc_update(self, ball_y):
        """Update tc(AI) player's location."""
        self.rect.centery = ball_y

    def draw(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

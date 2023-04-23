"""Module to manage the creation of the paddles."""

import sys

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    """Class to generate the paddles.

    Arguments:
            game_instance - the instance of class TableTennis
            location - Which side of the screen to put the paddle.
                       Options: ['L', 'R']
    """

    def __init__(self, game_instance, location):
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.setup = game_instance.setup
        self.color = self.setup.paddle_color
        self.rect = pygame.Rect(0, 0, self.setup.paddle_x, self.setup.paddle_y)
        if  location != 'R' and location  != 'L':
            print(f'\nError! Invalid paddle location {location}')
            print('See __init__(self) in main.py.')
            sys.exit()
        if location == 'R':
            self.rect.right = self.screen_rect.right - 20
        elif location == 'L':
            self.rect.left = self.screen_rect.left + 20
        self.rect.centery = self.screen_rect.centery
        # Needed when the pace of the game speeds up in later levels:
        self.y = float(self.rect.y)

    def update(self):
        """Update the paddle's position on screen."""
        if self.setup.moving_up and self.rect.top > 0:
            self.rect.y -= self.setup.player_speed
        elif (self.setup.moving_down and
                self.rect.bottom < self.screen_rect.bottom):
            self.rect.y += self.setup.player_speed

    def draw_paddle(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

"""Module to manage the creation of the ball."""

import random
import time

import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """Class to generate the tennis ball.

    Argument:
            game_instance - the instance of class TableTennis
    """

    def __init__(self, game_instance):
        """Initialize the game ball."""
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.setup = game_instance.setup
        self.stats = game_instance.stats
        self.rect = pygame.Rect(0, 0, self.setup.ball['radius'],
                                self.setup.ball['radius'])
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        pygame.draw.rect(self.surface, self.setup.color['ball'], self.rect)
        self.speed = self.stats.ball_speed
        self.x_direction = None
        self.y_direction = None

    def drop(self):
        """Set the starting x_direction of the ball."""
        time.sleep(self.setup.pause_timer)
        self.rect.center = self.screen_rect.center
        self.x_direction = random.choice(['to_left', 'to_right'])
        self.y_direction = random.choice(['to_top', 'to_bottom'])

    def update(self, *args, **kwargs):
        """Update the ball's position on screen."""
        if self.y_direction == 'to_top':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.x_direction == 'to_right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

    def draw(self):
        """Draw the ball to the screen."""
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

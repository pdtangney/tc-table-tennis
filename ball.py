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
        # pylint: disable=invalid-name
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.setup = game_instance.setup
        # ball['radius'], in future version ball may be round
        self.rect = pygame.Rect(0, 0, self.setup.ball['radius'],
                                self.setup.ball['radius'])
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        pygame.draw.rect(self.surface,
                         self.setup.colors['ball_color'], self.rect)
        self.speed = self.setup.ball['speed']
        self.x_direction = None

    def drop(self):
        """Set the starting x_direction of the ball."""
        time.sleep(self.setup.pause_timer)
        self.rect.center = self.screen_rect.center
        self.x_direction = random.choice(['to_left', 'to_right'])

    def update(self, *args, **kwargs):
        """Update the ball's position on screen."""
        if self.x_direction == 'to_right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.left > self.screen_rect.right:
            self.setup.points['score_left'] += (
                    self.setup.points['score_points'])
            self.drop()
        if self.rect.right <= 0:
            self.setup.points['score_right'] += (
                    self.setup.points['score_points'])
            self.drop()
        if (self.rect.bottom >= self.screen_rect.bottom or
                self.rect.top <= 0):
            self.speed = -self.speed

    def draw(self):
        """Draw the ball to the screen."""
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

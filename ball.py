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
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.setup = game_instance.setup
        self.color = self.setup.ball_color
        self.sleep = self.setup.sleep_timer
        self.rect = pygame.Rect(0, 0, self.setup.ball_radius,
                                self.setup.ball_radius)
        self.x_direction = None
        self.speed = self.setup.ball_speed
        # Needed when the pace of the game speeds up in later levels:
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def drop(self):
        """Set the starting x_direction of the ball."""
        time.sleep(self.sleep)
        self.rect.center = self.screen_rect.center
        self.x_direction = random.randint(1, 2)

    def update(self):
        """Update the ball's position on screen."""
        if self.x_direction == 1:
            self.rect.x += self.speed
            self.rect.y += self.speed / 2
        else:
            self.rect.x -= self.speed
        if self.rect.left > self.screen_rect.right:
            self.setup.score_left += self.setup.points
            self.drop()
        if self.rect.right < 0:
            self.setup.score_right += self.setup.points
            self.drop()
        if self.rect.bottom >= self.screen_rect.bottom:
            self.speed = -self.speed
        if self.rect.top < 0:
            self.speed = -self.speed

    def draw(self):
        """Draw the ball to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

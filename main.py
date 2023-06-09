"""
Main game module. Most of the magic lies here. :)

    Tc Table Tennis - A top-down view electronic table tennis game.
    Copyright (C) 2023 Peter Tangney (peteATrockytcgames.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Open the file LICENSE in a text editor for more information.
"""

import sys

import pygame
import random

from settings import Settings
from input_controls import KeyboardInput
from paddle import Paddle
from button import Button
from ball import Ball


class TableTennis:
    """Set up the game."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.setup = Settings()
        self._init_display()
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.input = KeyboardInput()
        self.game_active = False
        #gamestats()
        #scoreboard()
        self.ball = Ball(self)
        self.paddles = pygame.sprite.Group()
        self.player_right = Paddle(self, 'R')
        self.player_left = Paddle(self, 'L')
        self.paddles.add(self.player_right)
        self.paddles.add(self.player_left)
        self.pause_bttn = Button(self, "PAUSE")
        self.draw_net()
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN,
                                  pygame.KEYUP, pygame.MOUSEBUTTONDOWN])

    def _init_display(self):
        """Setup the display and window title."""
        self.screen = pygame.display.set_mode(self.setup.resolution)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tc [ Table | Tennis ] ")
        self.bg_surface = pygame.Surface(self.setup.resolution)
        self.bg_surface.fill(self.setup.bg_color)

    def draw_net(self):
        """Draw the net to the center of the screen."""
        self.net_rect = pygame.Rect(0, 0, self.setup.net_thickness,
                                    self.setup.screen_y)
        self.net_rect.center = self.screen_rect.center
        pygame.draw.rect(self.bg_surface, self.setup.net_color, self.net_rect)

    def run(self):
        """Start the main game loop."""
        self.ball.drop()
        while True:
            self.check_input_events()
            if self.game_active:
                pygame.mouse.set_visible(False)
                self.player_right.update()
                self.ball.update()
                self.timer += 1
                if self.timer == 10:
                    self.player_left.tc_update(self.ball.rect.centery)
                    self.timer = 0
                else:
                    self.player_left.tc_update(self.ball.rect.centery)
                self.check_collisions()
            self._update_screen()

    def check_input_events(self):
        """Watch for player input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_pause_bttn(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to key or button presses."""
        if event.key == self.input.quit:
            sys.exit()
        elif event.key == self.input.pause:
            if self.game_active:
                self.game_active = False
                pygame.mouse.set_visible(True)
            elif not self.game_active:
                self.game_active = True
        if self.game_active:
            if event.key == self.input.player_right_up:
                self.setup.moving_up = True
            elif event.key == self.input.player_right_down:
                self.setup.moving_down = True

    def check_collisions(self):
        """Check for ball, paddle collisions."""
        for paddle in self.paddles:
            if self.ball.rect.colliderect(paddle):
                if self.ball.x_direction == 1:
                    self.ball.x_direction = 2
                else:
                    self.ball.x_direction = 1

    def _check_keyup_events(self, event):
        """Respond to key or button releases."""
        if event.key == self.input.player_right_up:
            self.setup.moving_up = False
        elif event.key == self.input.player_right_down:
            self.setup.moving_down = False

    def _check_pause_bttn(self, mouse_pos):
        """
        Start a new game or resume a paused game when Pleayer
        clicks button.
        """
        button_clicked = self.pause_bttn.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True

    def _update_screen(self):
        """Refresh objects on screen and flip to the new screen."""
        self.screen.blit(self.bg_surface, (0, 0))
        if self.game_active:
            for paddle in self.paddles.sprites():
                paddle.draw()
            self.ball.draw()
        if not self.game_active:
            self.pause_bttn.draw()
        pygame.display.update()
        self.clock.tick_busy_loop(self.setup.FPS)


if __name__ == '__main__':
    tc_tt = TableTennis()
    tc_tt.run()

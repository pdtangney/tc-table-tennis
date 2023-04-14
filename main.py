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
        self.input_button = KeyboardInput()
        self.game_active = False
        #gamestats()
        #scoreboard()
        self.paddles = pygame.sprite.Group()
        self.player = Paddle(self, 'R')
        self.tc_player = Paddle(self, 'L')
        self.paddles.add(self.player)
        self.paddles.add(self.tc_player)
        self.play_button = Button(self, "PAUSE")
        self.ball = Ball(self)
        self.draw_net()

    def _init_display(self):
        """Setup the display and window title."""
        self.screen = pygame.display.set_mode(self.setup.resolution)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tc [ Table | Tennis ] ")

    def draw_net(self):
        """Draw the net to the center of the screen."""
        self.net_rect = pygame.Rect(0, 0, self.setup.net_thickness,
                                    self.setup.screen_y)
        self.net_rect.center = self.screen_rect.center

    def run_game(self):
        """Start the main game loop."""
        while True:
            self.check_input_events()
            if self.game_active:
                pygame.mouse.set_visible(False)
                self.player.update()
                self.ball.update()
            print(self.setup.points)
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
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to key or button presses."""
        if event.key == self.input_button.quit_key:
            sys.exit()
        elif event.key == self.input_button.pause:
            if self.game_active:
                self.game_active = False
                pygame.mouse.set_visible(True)
            elif not self.game_active:
                self.game_active = True
        if self.game_active:
            if event.key == self.input_button.player_up:
                self.setup.moving_up = True
            elif event.key == self.input_button.player_down:
                self.setup.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key or button releases."""
        if event.key == self.input_button.player_up:
            self.setup.moving_up = False
        elif event.key == self.input_button.player_down:
            self.setup.moving_down = False

    def _check_play_button(self, mouse_pos):
        """
        Start a new game or resume a paused game when Pleayer
        clicks button.
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True

    def _update_screen(self):
        """Refresh objects on screen and flip to the new screen."""
        self.clock.tick(self.setup.FPS)
        self.screen.fill(self.setup.bg_color)
        pygame.draw.rect(self.screen, self.setup.net_color, self.net_rect)
        if self.game_active:
            for paddle in self.paddles.sprites():
                paddle.draw_paddle()
            self.ball.draw_ball()
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    tc_tt = TableTennis()
    tc_tt.run_game()

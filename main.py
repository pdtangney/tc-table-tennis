"""
Main game module. Most of the magic lies here. :)

    Tc Table Tennis - A clone of Pong.
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

"""

import sys

import pygame

from settings import Settings
from input_controls import KeyboardInput
from paddle import Paddle


class TableTennis:
    """Set up the game."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.setup = Settings()
        self._init_display()
        self.clock = pygame.time.Clock()
        self.FPS = self.setup.FPS
        self.input_button = KeyboardInput()
        self.game_active = False
        #gamestats()
        #scoreboard()
        self.paddles = pygame.sprite.Group()
        self.player = Paddle(self, 'R')
        self.paddles.add(self.player)
        #computer bar
        #button("PLAY")

    def _init_display(self):
        """Setup the display and window title."""
        self.screen = pygame.display.set_mode(self.setup.resolution)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tc [ Table | Tennis ] ")

    def run_game(self):
        """Start the main game loop."""
        while True:
            self.check_input_events()
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

    def _check_keydown_events(self, event):
        """Respond to key or button presses."""
        if event.key == self.input_button.player_up:
            self.player.moving_up = True
        elif event.key == self.input_button.player_down:
            self.player.moving_down = True
        elif event.key == self.input_button.quit_key:
            sys.exit()
        elif event.key == self.input_button.pause:
            self.game_active = False

    def _check_keyup_events(self, event):
        """Respond to key or button releases."""
        if event.key == self.input_button.player_up:
            self.player.moving_up = False
        elif event.key == self.input_button.player_down:
            self.player.moving_down = False

    def _update_screen(self):
        """Refresh objects on screen and flip to the new screen."""
        self.screen.fill(self.setup.bg_color)
        self.player.draw_paddle()
        pygame.display.flip()
        self.clock.tick(self.setup.FPS)


if __name__ == '__main__':
    tc_tt = TableTennis()
    tc_tt.run_game()

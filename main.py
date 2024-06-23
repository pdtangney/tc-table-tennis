"""
Main game module. Most of the magic lies here.

    Tc Table Tennis - A top-down view electronic table tennis game.
    Copyright (C) 2023 Peter Tangney (peteATrockytcgames.com)

                               GPLv3
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

import sys      # sys.exit()

import pygame

import cmd_args
from settings import Settings
from input_controls import KeyboardInput
from paddle import Paddle
from button import Button
from ball import Ball
from stats import Stats
from scoreboard import ScoreBoard
import audio


class TableTennis:
    """Main game class. Initializes Settings(), sets up input controls,
    initialize game stats. Future versions will save certain stats to a
    file, to enable later retrieval. eg: high score board.
    """

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.setup = Settings()
        self._init_display()
        self.setup.load_setup()
        self.clock = pygame.time.Clock()
        self.input = KeyboardInput()
        self.game_active = False
        self.stats = Stats(self)
        self.score_board = ScoreBoard(self)
        self.ball = Ball(self)
        self.paddles = pygame.sprite.Group()
        self.player_right = Paddle(self, 'R')
        self.player_left = Paddle(self, 'L')
        self.paddles.add(self.player_right)
        self.paddles.add(self.player_left)
        self.pause_bttn = Button(self, "PAUSE")
        self.draw_net()
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN,
                                  pygame.KEYUP])

    def _init_display(self):
        """Initialize the display and window title."""
        if cmd_args.args.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.setup.screen_x = self.screen.get_rect().width
            self.setup.screen_y = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.setup.screen_x,
                                                  self.setup.screen_y))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.setup.game_name)
        self.bg_surface = pygame.Surface((self.setup.screen_x,
                                         self.setup.screen_y))
        self.bg_surface.fill(self.setup.color['background'])

    def draw_net(self):
        """Draw the net to the center of the screen."""
        self.net = pygame.Rect(0, 0, self.setup.net_thickness,
                               self.setup.screen_y)
        self.net.center = self.screen_rect.center
        pygame.draw.rect(self.bg_surface, self.setup.color['net'], self.net)

    def run(self):
        """Start the main game loop."""
        self.stats.init()
        self.ball.drop()
        self.score_board.prep_score()
        self.score_board.prep_lives()
        # Main game loop:
        while True:
            self.check_input_events()
            if self.game_active:
                self.player_right.update()
                self.ball.update()
                self.player_left.tc_update(self.ball.rect.centery)
                self.check_ball_paddle_collisions()
                self.check_ball_wall_collisions()
                self.check_remaining_lives()
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
        if event.key == self.input.quit:
            sys.exit()
        elif event.key == self.input.pause:
            if self.game_active:
                self.game_active = False
                pygame.mouse.set_visible(True)
            elif not self.game_active:
                self.game_active = True
                pygame.mouse.set_visible(False)
        if self.game_active:
            if event.key == self.input.player_right_up:
                self.setup.paddle['moving_up'] = True
            elif event.key == self.input.player_right_down:
                self.setup.paddle['moving_down'] = True

    def _check_keyup_events(self, event):
        """Respond to key or button releases."""
        if event.key == self.input.player_right_up:
            self.setup.paddle['moving_up'] = False
        elif event.key == self.input.player_right_down:
            self.setup.paddle['moving_down'] = False

    def check_ball_paddle_collisions(self):
        """Check for ball - paddle collisions."""
        for paddle in self.paddles:
            if self.ball.rect.colliderect(paddle):
                audio.paddle_hit_snd.play()
                if self.ball.x_direction == 'to_right':
                    self.ball.x_direction = 'to_left'
                else:
                    self.ball.x_direction = 'to_right'

    def check_ball_wall_collisions(self):
        """ChecK if ball has hit any of the four side walls."""
        if self.ball.rect.left > self.screen_rect.right:
            self.stats.score['left'] += self.stats.scoring
            self.stats.player_lives['right'] -= 1
            self.ball.drop()
        elif self.ball.rect.right <= self.screen_rect.left:
            self.stats.score['right'] += self.stats.scoring
            self.stats.player_lives['left'] -= 1
            self.ball.drop()
        if self.ball.rect.bottom >= self.screen_rect.bottom:
            self.ball.y_direction = 'to_top'
        if self.ball.rect.top <= self.screen_rect.top:
            self.ball.y_direction = 'to_bottom'
        self.score_board.prep_score()
        self.score_board.prep_lives()

    def check_remaining_lives(self):
        """Check how many lives remain. When none remain, call
        stats.reset as the game is over."""
        for player_side, lives_remaining in self.stats.player_lives.items():
            if lives_remaining == 0:
                self.stats.reset()

    def _update_screen(self):
        """Refresh objects on screen and flip to the new screen."""
        self.screen.blit(self.bg_surface, (0, 0))
        self.score_board.display_score_and_lives()
        if self.game_active:
            for paddle in self.paddles.sprites():
                paddle.draw()
            self.ball.draw()
        if not self.game_active:
            self.pause_bttn.draw()

        pygame.display.update()
        self.clock.tick_busy_loop(self.setup.frame_rate)


if __name__ == '__main__':
    tc_tt = TableTennis()
    tc_tt.run()

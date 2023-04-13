"""Module to manage configurable settings."""

"""
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


class Settings:
    """
    A class to manage in-game settings.
    Settings are:
        Screen resolution, background color, paddle colors,
        ball color. Game speed and frame-rate.
    """

    def __init__(self):
        """Initialize the settings."""

        self.screen_x = 1024
        self.screen_y = 768
        self.resolution = (self.screen_x, self.screen_y)
        self.equipment_color = (255, 255, 255)
        # By default, paddle, net, pause/play button all share the
        # same color. Color of the ball is slightly darker (see below)
        # In order to visually distinguish it from the net and paddles.
        self.bg_color = (20, 20, 20)
        self.FPS = 30

        # Player settings
        self.player_speed = 30
        self.moving_up = False
        self.moving_down = False
        # Paddle settings
        self.paddle_color = self.equipment_color
        # Set the paddle size to be x = 3%, y = 13% of screen resolution.
        paddle_x = self.screen_x * .03
        paddle_y = self.screen_y * .13
        self.paddle_x = int(paddle_x)  # Thickness
        self.paddle_y = int(paddle_y)  # Height
        self.tc_paddle_speed = 1  # I refer to ai players as tc players

        # Center net settings
        # Net thickness is 4% of screen width.
        thickness = self.screen_x * .04
        self.net_thickness = int(thickness)
        self.net_color = self.equipment_color

        # Button settings
        self.button_color = self.bg_color
        self.bttn_txt_color = self.equipment_color

        # Ball settings
        self.ball_color = (240, 240, 240)
        self.ball_radius = 10
        self.ball_speed = 1.5

        # Points settings
        self.miss = 2
        self.win_level = 5

        # Life settings
        self.misses_allowed = 3  # ...before losing a life
        self.lives = 3

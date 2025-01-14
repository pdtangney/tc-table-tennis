"""Module to manage configurable settings.

Tc Table Tennis - A top-down view electronic table tennis game.
Copyright (C) 2023 - 2025 Peter Tangney (peteATrockytcgames.com)

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


class Settings:
    """
    A class to manage in-game settings.

    Settings are:
        Screen resolution, background color, paddle colors,
        ball color. Game speed and frame-rate.
    """

    game_name = 'Tc [ Table | Tennis ] '
    game_name_alt = 'Tc Table Tennis'  # For use in terminal help.
    code_name = '(Shi shi SHAA!) '
    version = game_name + code_name + '0.0.10 (01/14/2025)'

    def __init__(self):
        """Initialize game settings."""
        self.screen_x = 1024
        self.screen_y = 768

        # By default, paddle, net, pause/play button all share the
        # same color. Color of the ball is DIFFERENT (see below)
        # In order to visually distinguish it from the net and paddles.
        self.color = {
                'ball': (255, 128, 0),
                'background': (26, 153, 0),
                'button': (26, 153, 0),   # Should be same as background
                'equipment': (255, 255, 255),
                'net': (222, 222, 222),
                'paddle': (255, 255, 255),
                'bttn_txt': (255, 255, 255),
                'score_txt': (255, 255, 255),
                }

        self.frame_rate = 60
        self.pause_timer = 0.5

        self.paddle = None
        self.net_thickness = None
        self.ball = None
        self.points = None
        self.lives = None

    def load_setup(self):
        """Call this method after (re)setting the screen resoultion,
        so that scaling of objects works correctly."""
        self.paddle = {'speed': 20,
                       'moving_up': False,
                       'moving_down': False,
                       'x': self.screen_x * .03,   # Width and
                       'y': self.screen_y * .13,   # height of paddle
                       }

        self.net_thickness = self.screen_x * .04

        self.ball = {'radius': self.screen_x * .04,
                     'speed': 7, }

        self.points = {'scoring': 1, 'win_level': 5}

        self.lives = {'maximum': 3, }

"""Module to manage configurable settings.

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


class Settings:
    """
    A class to manage in-game settings.

    Settings are:
        Screen resolution, background color, paddle colors,
        ball color. Game speed and frame-rate.
    """

    def __init__(self):
        """Initialize the settings."""
        self.resolution = (1024, 768)
        # By default, paddle, net, pause/play button all share the
        # same color. Color of the ball is DIFFERENT (see below)
        # In order to visually distinguish it from the net and paddles.
        self.color = {
                'ball': (255, 128, 0),
                'background': (26, 153, 0),
                'button': (62, 153, 36),   # Should be same as background
                'equipment': (255, 255, 255),
                'net': (222, 222, 222),
                'paddle': (255, 255, 255),
                'bttn_txt': (255, 255, 255),
                'score_txt': (255, 255, 255),
                }
        self.frame_rate = 60
        # How long to pause the game after missing the ball/scoring
        self.pause_timer = 0.5

        # Paddle settings
        # Set the paddle size to be x = 3%, y = 13% of screen resolution
        self.paddle = {'speed': 20,
                       'moving_up': False,
                       'moving_down': False,
                       'x': self.resolution[0] * .03,   # Width and
                       'y': self.resolution[1] * .13,   # height of paddle
                       }

        # Center net settings
        # Net thickness is 4% of screen width.
        self.net_thickness = self.resolution[0] * .04

        # Ball settings
        # The radius allows the ball to fit within the width of the net
        # CURRENTLY the ball is a square, so radius is a misnomer.
        # It is named so, to facilitate easier future code changes.
        self.ball = {'radius': self.resolution[0] * .04,
                     'speed': 10, }

        # Points settings
        self.points = {'scoring': 1, 'win_level': 5}

        # Life settings
        # before losing a life.
        self.lives = {'maximum': 3, }

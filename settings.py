"""Module to manage configurable settings."""


class Settings:
    """
    A class to manage in-game settings.
    Settings are:
        Screen resolution, background color, paddle colors,
        ball color. Game speed and frame-rate.
    """

    def __init__(self):
        """Initialize the settings."""

        self.screen_x = 640
        self.screen_y = 480
        self.resolution = (self.screen_x, self.screen_y)
        self.equipment_color = (255, 255, 255)
        # By default, paddle, net, pause/play button all share the
        # same color. Color of the ball is slightly darker (see below)
        # In order to visually distinguish it from the net and paddles.
        self.bg_color = (20, 20, 20)
        self.FPS = 30

        # Paddle settings
        self.paddle_color = self.equipment_color
        # Set the paddle size to be x = 3%, y = 13% of screen resolution.
        paddle_x = self.screen_x * .03
        paddle_y = self.screen_x * .13
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

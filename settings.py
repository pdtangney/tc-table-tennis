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
        self.bg_color = (20, 20, 20)
        self.FPS = 30

        # Paddle settings
        self.paddle_color = (255, 255, 255)
        self.paddle_x = 20  # Thickness
        self.paddle_y = 60  # Height
        self.tc_paddle_speed = 1  # I refer to ai players as tc players

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

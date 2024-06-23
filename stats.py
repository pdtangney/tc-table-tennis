"""Module to manage game stats, such as the current score,
lives remaining, etc."""


class Stats:
    """Track various game statistics. eg: lives, current score, level."""
    def __init__(self, game_instance):
        """Initialize stats."""
        self.instance = game_instance
        self.reset()

    def init(self):
        """Initialise stats

        calls Stats().reset()
        """
        self.reset()

    def reset(self):
        """Intialize stats which can be changed before gameplay.

        Most of these stats also change throughout gameplay.
        eg: score_left, etc.
        When a new game is started this method is called to reset the
        game state to its defaults.
        """
        self.score = {'left': 0, 'right': 0}
        self.player_lives = {'left': self.instance.setup.lives['maximum'],
                             'right': self.instance.setup.lives['maximum']}

        self.scoring = self.instance.setup.points['scoring']
        self.win_level_points = self.instance.setup.points['win_level']
        self.ball_speed = self.instance.setup.ball['speed']
        self.paddle_speed = self.instance.setup.paddle['speed']
        self.instance.game_active = False

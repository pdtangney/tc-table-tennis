"""Module to manage game stats, such as the current score,
lives remaining, etc."""


class Stats:
    """Track various game statistics. eg: lives, current score, level."""
    def __init__(self, game_instance):
        """Initialize stats."""
        self.instance = game_instance
        self.settings = game_instance.setup
        self.reset_stats()

    def reset_stats(self):
        """Intialize stats which can be changed before gameplay.

        Most of these stats also change throughout gameplay.
        eg: score_left, etc.
        When a new game is started this method is called to reset the
        game state to its defaults.
        """
        # self.paddle_speed = self.settings.paddle['speed']
        self.score = {'left': 0, 'right': 0}
        # This setting is dependent on the INITIAL difficulty setting.
        # not-implemented: defaults to 3
        max_lives = self.settings.lives['maximum']
        self.player_lives = {'left': max_lives, 'right': max_lives}

        self.max_misses = self.settings.lives['misses_allowed']
        self.player_miss = {'left': self.max_misses, 'right': self.max_misses}

        self.scoring = self.settings.points['scoring']
        self.win_level_points = self.settings.points['win_level']
        self.ball_speed = self.settings.ball['speed']
        self.paddle_speed = self.settings.paddle['speed']
        self.instance.game_active = False

"""Module to manage game stats, such as the current score,
lives remaining, etc."""

class Stats:
    """Track various game statistics. eg: lives, current score, level."""
    def __init__(self, game_instance):
        """Initialize stats."""
        self.settings = game_instance.setup
        self.reset_stats()

    def reset_stats(self):
        """Intialize stats which can be changed before gameplay.

        Most of these stats also change throughout gameplay. 
        eg: score_left, etc.
        When a new game is started this method is called to reset the
        game state to its defaults.
        """
        #self.paddle_speed = self.settings.paddle['speed']
        # TODO adding levels will increase the value of self.scoring
        self.score = {'left': 0, 'right': 0 }
        # This setting is dependent on the INITIAL difficulty setting.
        # not-implemented: defaults to 3
        self.lives = self.settings.lives['maximum']
        # These change as the difficulty level increases:
        self.misses = self.settings.lives['misses_allowed']
        self.scoring = self.settings.points['scoring']
        self.win_level_points = self.settings.points['win_level']
        self.ball_speed = self.settings.ball['speed']
        self.paddle_speed = self.settings.paddle['speed']

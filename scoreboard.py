"""A class to prepare and show the scoring information on screen."""
import pygame.font


class ScoreBoard:
    """A class representing the scores displayed on screen."""

    def __init__(self, game_instance):
        """Initialize scoring settings."""
        self.game_instance = game_instance
        self.game_instance.screen_rect = self.game_instance.screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image for display."""
        # prep left:
        left_score_str = f"$ {self.game_instance.stats.score['left']}"
        self.left_score_img = self.font.render(
                left_score_str, True,
                self.game_instance.setup.color['score_txt'],
                self.game_instance.setup.color['background'])
        self.left_score_rect = self.left_score_img.get_rect()
        self.left_score_rect.left = self.game_instance.screen_rect.left + 20
        self.left_score_rect.top = 20
        # prep right
        right_score_str = f"$ {self.game_instance.stats.score['right']}"
        self.right_score_img = self.font.render(
                right_score_str, True,
                self.game_instance.setup.color['score_txt'],
                self.game_instance.setup.color['background'])
        self.right_score_rect = self.right_score_img.get_rect()
        self.right_score_rect.right = self.game_instance.screen_rect.right - 20
        self.right_score_rect.top = 20

    def prep_lives(self):
        """Turn the player_lives into a rendered image for display."""
        # prep left
        left_lives_str = '|' * self.game_instance.stats.player_lives['left']
        self.left_lives_img = self.font.render(
                left_lives_str, True,
                self.game_instance.setup.color['score_txt'],
                self.game_instance.setup.color['background'])
        self.left_lives_rect = self.left_lives_img.get_rect()
        self.left_lives_rect.left = self.game_instance.screen_rect.left + 20
        self.left_lives_rect.top = self.left_score_rect.bottom
        # Prep right
        right_lives_str = '|' * self.game_instance.stats.player_lives['right']
        self.right_lives_img = self.font.render(
                right_lives_str, True,
                self.game_instance.setup.color['score_txt'],
                self.game_instance.setup.color['background'])
        self.right_lives_rect = self.right_lives_img.get_rect()
        self.right_lives_rect.right = self.game_instance.screen_rect.right - 20
        self.right_lives_rect.top = self.right_score_rect.bottom

    def display_score_and_lives(self):
        """Draw the scores and lives remaining to the screen."""
        self.game_instance.screen.blit(self.left_score_img,
                                       self.left_score_rect)
        self.game_instance.screen.blit(self.right_score_img,
                                       self.right_score_rect)
        self.game_instance.screen.blit(self.left_lives_img,
                                       self.left_lives_rect)
        self.game_instance.screen.blit(self.right_lives_img,
                                       self.right_lives_rect)

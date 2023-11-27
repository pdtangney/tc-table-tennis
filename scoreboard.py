"""A class to prepare and show the scoring information on screen."""
import pygame.font


class ScoreBoard:
    """A class representing the scores displayed on screen."""
    def __init__(self, game_instance):
        """Initialize scoring settings."""
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game_instance.setup
        self.stats = game_instance.stats

        self.text_color = self.settings.colors['score_txt_color']
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image for display."""
        score_str = ''
        for k, v in self.stats.score.items():
            score_str += f' {k}: {v}'
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.colors['bg_color'])
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def display_score(self):
        """Draw the scores to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

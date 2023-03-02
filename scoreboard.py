import pygame.font


class Scoreboard:
    # a class to report scoring information

    def __init__(self, ai_game):
        # initialize scorekeeping attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settins for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image.
        self.prep_score()

import pygame as p

class Score:
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        self.text_color = (0, 0, 0)
        self.font = p.font.SysFont(None, 48)

        self.reset_score()
        self.update_score()

    def update_score(self):
        score_str = str(round(self.score))
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.game_settings.screen_width - 30
        self.score_rect.top = 20

    def reset_score(self):
        self.score = 0

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)


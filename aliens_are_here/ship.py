import pygame as p
from pygame.sprite import Sprite


class Ship():
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        self.image = p.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)



    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += (self.game_settings.speed_factor)
        if self.moving_left and self.rect.left > 0:
            self.center -= (self.game_settings.speed_factor)
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        Sprite.__init__(self)
        self.screen = screen

        self.rect = p.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y 

    def draw_bullet(self):
        p.draw.rect(self.screen, self.color, self.rect)


class Ships_left:
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        self.text_color = (0, 0, 0)
        self.font = p.font.SysFont(None, 48)

        self.update_ships_left()

        self.image = p.image.load('images/life.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.left = self.ships_left_rect.right + 7
        self.image_rect.bottom = self.ships_left_rect.bottom

    def update_ships_left(self):
        ships_left_str = str(self.game_settings.ships_left)
        self.ships_left_image = self.font.render(ships_left_str, True, self.text_color, self.game_settings.bg_color)
        self.ships_left_rect = self.ships_left_image.get_rect()
        self.ships_left_rect.right = 30
        self.ships_left_rect.top = 20


    def draw_ships_left(self):
        self.screen.blit(self.ships_left_image, self.ships_left_rect)
        self.screen.blit(self.image, self.image_rect)




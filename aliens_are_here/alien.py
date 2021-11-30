import pygame as p 
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game_settings, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.game_settings = game_settings

        self.image = p.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = 1
        self.check = 1


    def move(self):
        if self.check_edges():
            self.direction *= -1
        self.x += self.game_settings.alien_speed_factor * self.direction

        if self.near_edge():
            self.y += self.game_settings.alien_speed_factor

        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        if self.rect.right >= self.game_settings.screen_width:
            return True
        elif self.rect.left <= 0:
            return True


    def near_edge(self):
        if self.rect.right >= (self.game_settings.screen_width - self.rect.height / 2):
            return True
        elif self.rect.left <= self.rect.height / 2:
            return True


class Star(Sprite):
    def __init__(self, game_settings, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.game_settings = game_settings

        self.image = p.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
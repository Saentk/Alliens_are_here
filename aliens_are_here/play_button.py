import pygame as p 

class Button:
    def __init__(self, game_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 250, 100
        self.button_color = (0, 255, 255)
        self.text_color = (255, 255, 255)
        self.font = p.font.SysFont(None, 48)

        self.rect = p.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center 

        self.button_msg(msg)

    def button_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

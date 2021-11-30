import pygame as p
from settings import Settings
from ship import Ship, Ships_left
import game_functions as gf
from play_button import Button
from score import Score

def run_game():
    p.init()
    game_settings = Settings()
    screen = p.display.set_mode(
        (game_settings.screen_width, game_settings.screen_hight))
    p.display.set_caption('Allien Invasion')
    play_button = Button(game_settings, screen, 'Play')
    ships_left = Ships_left(game_settings, screen)
    score = Score(game_settings, screen)
    ship = Ship(game_settings, screen)

    gf.create_fleet(game_settings, screen, ship)
    gf.create_stars(game_settings, screen)

    while True:
        gf.check_events(game_settings, screen, ship, play_button)
        if game_settings.game_active:
            ship.update()
            gf.update_aliens(game_settings, screen, ship, score, ships_left)
            gf.update_bullets(game_settings, screen, ship, score)
        gf.update_screen(game_settings, screen, ship, play_button, score, ships_left)

if __name__ == '__main__':
    run_game()


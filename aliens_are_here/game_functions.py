import sys, random, time
import pygame as p
from ship import Bullet
from alien import Alien, Star
from pygame.sprite import Group

def check_keydown_events(event, game_settings, screen, ship): 
    if event.key == p.K_RIGHT: 
        ship.moving_right = True 
    elif event.key == p.K_LEFT: 
        ship.moving_left = True 
    elif event.key == p.K_SPACE:
        fire_bullets(game_settings, screen, ship)
    elif event.key == p.K_q: 
        sys.exit()

def check_keyup_events(event, ship): 
    if event.key == p.K_RIGHT: 
        ship.moving_right = False 
    elif event.key == p.K_LEFT: 
        ship.moving_left = False 

def check_events(game_settings, screen, ship, play_button): 
    for event in p.event.get(): 
        if event.type == p.QUIT: 
            sys.exit() 
        elif event.type == p.KEYDOWN: 
            check_keydown_events(event, game_settings, screen, ship)
        elif event.type == p.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == p.MOUSEBUTTONDOWN and game_settings.game_active == False:
            mouse_x, mouse_y = p.mouse.get_pos()
            check_play_button(game_settings, play_button, ship, mouse_x, mouse_y)


def check_play_button(game_settings, play_button, ship, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        game_settings.reset_settings()
        game_settings.game_active = True

def update_screen(game_settings, screen, ship, play_button, score, ships_left):
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    stars.draw(screen)
    ships_left.draw_ships_left()
    aliens.draw(screen)
    ship.blitme()
    score.draw_score()
    if game_settings.game_active == False:
        play_button.draw_button()
    p.display.flip()

def update_bullets(game_settings, screen, ship,score):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collisions(game_settings, screen, ship, score)


#       Movement mechanics doesn`t allow to touch bottom without touching ship
def update_aliens(game_settings, screen, ship, score, ships_left):
    for alien in aliens.sprites():
        alien.move()
    if p.sprite.spritecollideany(ship, aliens):
        lose_life(game_settings, screen, ship, score, ships_left)

def lose_life(game_settings, screen, ship, score, ships_left):
    game_settings.ships_left -= 1

    if game_settings.ships_left == 0:
        game_settings.reset_settings()
        score.reset_score()
        score.update_score()
        
    ships_left.update_ships_left()
    bullets.empty()
    aliens.empty()
    time.sleep(0.5)


def check_collisions(game_settings, screen, ship, score):
    collisions = p.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions:
            score.score += game_settings.alien_points
            score.update_score()
    if len(aliens) == 0:
        create_fleet(game_settings, screen, ship)
        # game_settings.new_level_update()
        new_level(game_settings)

def fire_bullets(game_settings, screen, ship):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

# Aliens block

def get_number_aliens(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(game_settings, screen, alien_number, row_number):
    alien = Alien(game_settings, screen)  #changed here
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.y = float(alien.rect.y)
    aliens.add(alien)

def get_number_rows(game_settings, ship_height, alien_height):
    available_space_y = (game_settings.screen_hight - (3 * alien_height) - ship_height)
    rows_number = int(available_space_y / (2 * alien_height))
    return rows_number

def create_fleet(game_settings, screen, ship):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, alien_number, row_number)

# End Aliens block

def create_stars(game_settings, screen):
    for x in range(random.randint(40, 60)):
        star = Star(game_settings, screen)
        star.rect.y = random.randint(0, game_settings.screen_hight)
        star.rect.x = random.randint(0, game_settings.screen_width)
        stars.add(star)

def new_level(game_settings):
    game_settings.alien_points *= game_settings.speed_up
    game_settings.speed_factor *= game_settings.speed_up
    game_settings.bullet_speed_factor *= game_settings.speed_up
    game_settings.alien_speed_factor *= game_settings.speed_up


bullets = Group()
aliens = Group()
stars = Group()



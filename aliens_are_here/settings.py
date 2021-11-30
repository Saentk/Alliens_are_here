
class Settings():

	def __init__(self):
		self.screen_width = 1500
		self.screen_hight = 800

		self.bg_color = (34, 168, 230)

		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 225, 0, 0

		self.speed_up = 1.1

		self.reset_settings()

	def reset_settings(self):
		self.game_active = False

		self.speed_factor = 1
		self.bullet_speed_factor = 1
		self.alien_points = 10
		self.alien_speed_factor = 0.5

		self.ships_left = 3
		self.bullets_allowed = 3

	def new_level_update(self):
		self.alien_points *= self.speed_up

		self.speed_factor *= self.speed_up
		self.bullet_speed_factor *= self.speed_up
		self.alien_speed_factor *= self.speed_up

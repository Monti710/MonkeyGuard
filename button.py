import pygame
import variables

#button class
class Button():
	recoger = pygame.mixer.Sound("data/audio/recoleccion.wav")
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.tocar = True
	def draw(self, surface):
		action = False
		
		pos = pygame.mouse.get_pos()
		
		if not self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				self.tocar = True
		
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 0:
				self.tocar=False
			if pygame.mouse.get_pressed()[0] == 1 and self.tocar==False:
				self.clicked = True
				action = True
				self.recoger.play()
		

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
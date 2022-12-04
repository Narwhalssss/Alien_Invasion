import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)
        
        self.movingRight = False
        self.movingLeft = False
        
    def center_ship(self):
        self.center = self.screen_rect.centerx
            
        
    def updateSelf(self):
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.movingLeft and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            
        #   self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
        
        
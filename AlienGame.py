import pygame
import gameFunctions as gf
from Settings import Settings
from Ship import Ship
from pygame.sprite import Group
from gameStats import GameStats
from Buttons import Button
from scoreboard import Scoreboard

def runGame():
    #initialize screen of game and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make ship
    ship = Ship(ai_settings,screen)
    #make bullet
    bullets = Group()
    #make alien
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #make the Youtube 100mil playbutton
    play_button = Button(ai_settings,screen,"Play")
    
    
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
     # Start the main loop for the game.
    while True:
        gf.checkEvents(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)
        
        if stats.game_active:
            ship.updateSelf()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,bullets)
        
        gf.updateScreen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)

        
    
runGame()
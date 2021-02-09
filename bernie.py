# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:43:07 2021

@author: joshr
"""

import pygame

class Bernie: 
    """A class to manage chairman Bernie"""
    
    def __init__(self, ai_game): 
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get its rect. 
        self.image = pygame.image.load('images/bernie.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of the screen. 
        self.rect.midtop = self.screen_rect.midtop
        
    def blitme(self): 
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
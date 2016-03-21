import pygame
from pygame.locals import *
pygame.init()

class entity(pygame.sprite.DirtySprite):

    def __init__(self, x, y, image):


        pygame.sprite.DirtySprite.__init__(self)

        self.image = image
        self.height = self.image.get_height()
        self.width = self.image.get_width()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dirty = 2

    def move(self,dx,dy):

        self.rect.x+=dx
        self.rect.y+=dy

    def resize(self,x,y):
        self.image = pygame.transform.scale(self.image,(x,y))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect()

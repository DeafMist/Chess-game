import pygame


class Characters(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

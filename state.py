import os
import sys
import pygame

from barrier import Barrier
from cursor import Cursor
from soundlibrary import Soundlibrary
from sprite import Sprite


class State:
    def __init__(self):
        self.cursor = Cursor("aim")
        self.sprite = Sprite((768 - 15, 432 - 35.5), 'swat', self)
        self.bullets = []
        self.soundlibrary = Soundlibrary('assets/audio')

        self.map = pygame.image.load(os.path.join('assets/images', 'map.png'))
        self.map_width, self.map_height = self.map.get_width(), self.map.get_height()

        self.barriers = [Barrier((792, 512), 32, 96)]

    def render_frame(self, surface):
        #surface.blit(self.map, (0, 0))
        self.sprite.render_frame(surface)
        for bullet in self.bullets:
            bullet.render_frame(surface)
        self.cursor.render_frame(surface)

    def update(self, elapsed_seconds):
        self.sprite.update(elapsed_seconds)
        for bullet in self.bullets:
            bullet.update(elapsed_seconds)
            if bullet.dead:
                self.bullets.remove(bullet)
        self.cursor.update()

        if self.sprite.LEFT_KEY:
            pass
        if self.sprite.RIGHT_KEY:
            pass
        if self.sprite.UP_KEY:
            pass
        if self.sprite.DOWN_KEY:
            pass

    def process_input(self):
        for event in pygame.event.get():
            self.sprite.process_input(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    sys.exit()

    @staticmethod
    def is_key_pressed(key):
        return pygame.key.get_pressed()[key]

    @staticmethod
    def is_mouse_pressed(key):
        return pygame.mouse.get_pressed()[key]

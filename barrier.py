import os
import pygame


class Barrier:
    def __init__(self, position, width, height):
        self.position = position
        self.rect = pygame.Rect(position, (width, height))

    def observer_update(self):
        pass

    def update(self, elapsed_seconds):
        pass

    def render_frame(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h))

    def update_laser(self):
        pass

import os
import pygame


class Cursor:
    def __init__(self, name):
        pygame.mouse.set_visible(False)
        self.cursor = pygame.image.load(os.path.join('assets/images', f'{name}.png'))
        self.cursor = pygame.transform.smoothscale(self.cursor, (30, 30))
        self.rect = self.cursor.get_rect()
        self.rect_half_w = self.rect.w / 2
        self.rect_half_h = self.rect.w / 2
        self.mouse_pos = pygame.mouse.get_pos()
        self.position = (pygame.mouse.get_pos()[0] - self.rect_half_w, pygame.mouse.get_pos()[1] - self.rect_half_h)

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.position = (self.mouse_pos[0] - self.rect_half_w, self.mouse_pos[1] - self.rect_half_h)

    def render_frame(self, surface):
        surface.blit(self.cursor, self.position)

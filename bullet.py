import pygame
import os
from cooldown import Cooldown


class Bullet:
    def __init__(self, x, y, angle, rico, flip, state):
        self.state = state
        self.cooldown = Cooldown(2)
        self.dead = False
        self.angle = angle
        self.rico = rico
        self.flip = flip
        self.bullet = pygame.image.load(os.path.join("assets/images", "bullet.png"))
        self.bullet = pygame.transform.scale(self.bullet, (self.bullet.get_width() / 25, self.bullet.get_height() / 25))
        self.bullet = pygame.transform.rotate(self.bullet, self.angle - 90)
        self.rect = self.bullet.get_rect()
        self.bullet_position = pygame.math.Vector2(x - self.rect.w / 2, y - self.rect.h / 2)
        self.mask = pygame.mask.from_surface(self.bullet)
        if self.flip:
            self.speed = 1500
        else:
            self.speed = -1500

    def render_frame(self, surface):
        surface.blit(self.bullet, self.rect)

    def update(self, elapsed_seconds):
        self.cooldown.update(elapsed_seconds)
        if self.cooldown.ready:
            self.dead = True
        self.bullet_position[0] -= elapsed_seconds * self.speed
        self.bullet_position[1] -= self.rico * elapsed_seconds * self.speed
        self.rect.x = self.bullet_position[0]
        self.rect.y = self.bullet_position[1]

    @property
    def get_dead(self):
        return self.dead

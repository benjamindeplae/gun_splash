import math
import os
import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from bullet import Bullet
from cooldown import Cooldown


class Gun:
    def __init__(self, position, observable, state):
        self.state = state
        self.observable = observable
        self.position_gun = (position[0] + self.observable.frameBasedAnimation.width / 2, position[1] + self.observable.frameBasedAnimation.height / 2)
        self.gun = pygame.image.load(os.path.join('assets/images', 'ak47.png'))
        self.gun = pygame.transform.scale(self.gun, (self.gun.get_width() / 14, self.gun.get_height() / 14))
        self.flip_gun = pygame.transform.flip(self.gun, False, True)
        self.rotate_gun = self.gun
        self.rect = self.rotate_gun.get_rect(center=(self.position_gun[0], self.position_gun[1] + 2))
        # De + 2 is nodig, omdat het middelpunt van de sprite lager ligt dan het punt van de loop.
        self.ammo = 30
        self.smallFont = pygame.font.SysFont("arial.ttf", 40)
        self.text_surface = self.smallFont.render(f"ammo: {self.ammo}", True, (255, 255, 255))
        self.angle = 0
        self.mouse_pos = self.state.cursor.mouse_pos
        self.rico = 0
        self.flip = False

        self.barrel_offset = [23, -3]  # Offset of the barrel from the gun's position
        self.barrel_pos = [self.position_gun[0] + self.barrel_offset[0], self.position_gun[1] + self.barrel_offset[1]]
        self.laser_end = self.mouse_pos

        self.shooting = False
        self.cooldown_bullet = Cooldown(0.1)
        self.reload = False
        self.cooldown_reload = Cooldown(2.5)

    def update(self, elapsed_seconds):
        self.mouse_pos = self.state.cursor.mouse_pos
        if self.mouse_pos[0] < self.state.sprite.position[0] + 15:
            self.flip = True
        else:
            self.flip = False
        self.gun_rotation()
        self.update_laser()

        self.cooldown_bullet.update(elapsed_seconds)
        if self.shooting:
            if self.cooldown_bullet.ready and self.ammo > 0 and not self.reload:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/audio/bullet.ogg'))
                self.state.bullets.append(Bullet(self.position_gun[0], self.position_gun[1], self.angle, self.rico, self.flip, self.state))
                self.ammo -= 1
                self.text_surface = self.smallFont.render(f"ammo: {self.ammo}", True, (255, 255, 255))
                self.cooldown_bullet.reset()
        if self.reload:
            self.cooldown_reload.update(elapsed_seconds)
            if self.cooldown_reload.ready:
                self.ammo = 30
                self.text_surface = self.smallFont.render(f"ammo: {self.ammo}", True, (255, 255, 255))
                self.cooldown_reload.reset()
                self.reload = False

    def gun_rotation(self):
        dx = self.mouse_pos[0] - self.position_gun[0]
        dy = self.mouse_pos[1] - self.position_gun[1]
        self.angle = (180 / math.pi) * math.atan2(dx, dy)
        if self.flip:
            self.rotate_gun = pygame.transform.rotate(self.flip_gun, self.angle - 90)
        else:
            self.rotate_gun = pygame.transform.rotate(self.gun, self.angle - 90)
        self.rect = self.rotate_gun.get_rect(center=(self.position_gun[0], self.position_gun[1] + 2))
        # De + 2 is nodig, omdat het middelpunt van de sprite lager ligt dan het punt van de loop.

        # Update barrel position based on gun rotation
        angle_rad = math.radians(self.angle - 90)
        offset_x = int(self.barrel_offset[0] * math.cos(angle_rad))  # Calculate new x offset
        offset_y = int(self.barrel_offset[0] * math.sin(angle_rad))  # Calculate new y offset
        self.barrel_pos[0] = self.position_gun[0] + offset_x
        self.barrel_pos[1] = self.position_gun[1] - offset_y

    def update_laser(self):
        if self.mouse_pos[0] > self.position_gun[0]:
            self.rico = (self.mouse_pos[1] - self.position_gun[1]) / (self.mouse_pos[0] - self.position_gun[0])
            self.laser_end = (1500, self.line(self.rico, 1500, self.barrel_pos[0], self.barrel_pos[1]))
        elif self.mouse_pos[0] < self.position_gun[0]:
            self.rico = (self.position_gun[1] - self.mouse_pos[1]) / (self.position_gun[0] - self.mouse_pos[0])
            self.laser_end = (36, self.line(self.rico, 36, self.barrel_pos[0], self.barrel_pos[1]))

    def render_frame(self, surface):
        surface.blit(self.rotate_gun, self.rect)
        self.render_laser(surface)
        surface.blit(self.text_surface, (20, 20))

    def render_laser(self, surface):
        pygame.draw.line(surface, (0, 255, 0), self.barrel_pos, self.laser_end)

    def process_input(self, event):
        if self.state.is_key_pressed(pygame.K_r):
            if not self.reload:
                self.state.soundlibrary.play('reload')
                self.reload = True
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.shooting = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.shooting = False

    @staticmethod
    def line(rico, x, xa, ya):
        return rico * (x - xa) + ya

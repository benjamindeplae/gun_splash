import pygame
from frameBasedAnimation import FrameBasedAnimation
from gun import Gun


class Sprite:
    def __init__(self, position, string, state):
        self.state = state
        self.position = position
        self.RIGHT_KEY = False
        self.LEFT_KEY = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.flip = False
        self.frameBasedAnimation = FrameBasedAnimation(self.position, string)
        self.gun = Gun(self.position, self, self.state)

    def update(self, elapsed_seconds):
        if self.LEFT_KEY and not self.RIGHT_KEY or self.RIGHT_KEY and not self.LEFT_KEY or self.UP_KEY and not self.DOWN_KEY or self.DOWN_KEY and not self.UP_KEY:
            self.frameBasedAnimation.update(elapsed_seconds, self.flip)
        else:
            if self.flip:
                self.frameBasedAnimation.img = self.frameBasedAnimation.list_reverse[0]
            else:
                self.frameBasedAnimation.img = self.frameBasedAnimation.list[0]
            self.frameBasedAnimation.total_elapsed_time = 0
        self.gun.update(elapsed_seconds)

    def render_frame(self, surface):
        self.frameBasedAnimation.render(surface)
        self.gun.render_frame(surface)

    def process_input(self, event):
        if self.state.is_key_pressed(pygame.K_d):
            self.RIGHT_KEY = True
            self.flip = False
        else:
            self.RIGHT_KEY = False
        if self.state.is_key_pressed(pygame.K_q):
            self.LEFT_KEY = True
            self.flip = True
        else:
            self.LEFT_KEY = False
        if self.state.is_key_pressed(pygame.K_z):
            self.UP_KEY = True
        else:
            self.UP_KEY = False
        if self.state.is_key_pressed(pygame.K_s):
            self.DOWN_KEY = True
        else:
            self.DOWN_KEY = False
        self.gun.process_input(event)

import math
import os
import pygame


class FrameBasedAnimation:
    def __init__(self, position, string):
        self.width = 25
        self.height = 59
        self.list = [
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}1.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}2.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}3.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}4.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}5.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}6.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}7.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}8.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}9.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}10.png')),
                                   (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets/images', f'{string}11.png')),
                                   (self.width, self.height))]
        self.list_reverse = []
        for elem in self.list:
            self.list_reverse.append(pygame.transform.flip(elem, True, False))
        self.frame_duration = 0.1
        self.total_elapsed_time = 0
        self.img = self.list[0]
        self.mask = pygame.mask.from_surface(self.img)
        self.frame_index = 0
        self.position = position

    def reset(self, flip):
        if flip:
            self.img = self.list_reverse[0]
        else:
            self.img = self.list[0]

    def update(self, elapsed_seconds, flip):
        self.total_elapsed_time += elapsed_seconds
        self.frame_index = math.floor(self.total_elapsed_time / self.frame_duration)
        if self.frame_index < len(self.list):
            if flip:
                self.img = self.list_reverse[self.frame_index]
            else:
                self.img = self.list[self.frame_index]
            self.mask = pygame.mask.from_surface(self.img)
        else:
            self.total_elapsed_time = 0
            self.update(elapsed_seconds, flip)

    def render(self, surface):
        surface.blit(self.img, self.position)

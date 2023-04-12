import pygame

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)


def create_main_surface():
    screen_size = (1536, 864)
    surface = pygame.display.set_mode(screen_size)
    return surface


def clear_surface(surface):
    surface.fill((0, 0, 0))

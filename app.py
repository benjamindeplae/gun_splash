import pygame
from state import State
import utility


def main():
    surface = utility.create_main_surface()
    state = State()
    clock = pygame.time.Clock()

    while True:
        elapsed_seconds_since_last_frame = clock.tick() / 1000
        utility.clear_surface(surface)
        state.render_frame(surface)
        state.update(elapsed_seconds_since_last_frame)
        pygame.display.flip()
        state.process_input()


main()

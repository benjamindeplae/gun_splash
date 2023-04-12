
class Cooldown:
    def __init__(self, duration):
        self.__duration = duration
        self.time_passed = 0

    @property
    def ready(self):
        return self.time_passed > self.__duration

    def update(self, elapsed_seconds):
        self.time_passed += elapsed_seconds

    def reset(self):
        self.time_passed = 0

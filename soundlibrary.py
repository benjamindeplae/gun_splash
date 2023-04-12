import os
import random
import pygame
import pygame.mixer


class Soundlibrary:
    def __init__(self, root):
        cwd = os.getcwd()  # get current directory
        os.chdir(root)  # change directory to root
        paths = self.__find_audio_files('./')
        self.__table = self.__create_sound_table(paths)
        os.chdir(cwd)  # change directory to original directory

    def play(self, id):
        self.__table[id].play()

    def __find_audio_files(self, root):
        start_path = root
        list = []
        for path, dirs, files in os.walk(start_path):
            for filename in files:
                filepath = path.replace('\\', '/') + '/' + filename
                list.append(filepath)
        return list

    def __derive_id(self, path):
        string = path
        string = string[2:]
        index = string.index('.')
        string = string[1:index]
        return string

    def __create_sound_table(self, paths):
        dict = {}
        for f in paths:
            sound_id = self.__derive_id(f)
            sound = pygame.mixer.Sound(f)
            dict[sound_id] = sound
        return dict

    def play_background_music(self):
        playlist = list()
        playlist.append("music/1.ogg")
        playlist.append("music/2.ogg")
        playlist.append("music/3.ogg")
        playlist.append("music/death.ogg")
        playlist.append("music/intro.ogg")
        playlist.append("music/nemesis.ogg")
        # Get the first track from the playlist
        pygame.mixer.music.load(playlist.pop())
        pygame.mixer.music.queue(playlist.pop())  # Queue the 2nd song
        pygame.mixer.music.set_endevent(
            pygame.USEREVENT)    # Setup the end track event
        pygame.mixer.music.play()           # Play the music

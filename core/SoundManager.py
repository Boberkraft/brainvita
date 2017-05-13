if __name__ == '__main__':
    import sys
    import pygame
    import glob
    from copy import deepcopy
    from enum import IntEnum
    import builtins

    # sets small buffer  so sound apear fast
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
    pygame.init()
    builtins.pygame = pygame
    builtins.RESOLUTION = (9 * 50, 9 * 50)
    builtins.game_display = pygame.display.set_mode(RESOLUTION)

class SoundManager:
    diff = None

    def __init__(self, music, sound):
        self.music_path = music
        self.sound_path = sound

    def set_theme(self, diff):
        self.name = diff

    def play_background(self):
        pygame.mixer.music.load('{}{}.background.mp3'.format(self.music_path, self.name))
        pygame.mixer.music.set_volume(0.10)
        pygame.mixer.music.play(-1)

    def play_sound(self):
        effect = pygame.mixer.Sound('{}{}.move.wav'.format(self.sound_path, self.name))
        effect.play()

if __name__ == '__main__':
    sound_manager = SoundManager('../music/', '../sound/')
    class xd:
        name = 'Normal'
    sound_manager.set_theme(xd)
    sound_manager.play_background()
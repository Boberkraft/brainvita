import pygame
from enum import IntEnum
import builtins

# sets small buffer so sound apear fast
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
pygame.init()
builtins.pygame = pygame
builtins.RESOLUTION = (9 * 50, 9 * 50)
builtins.game_display = pygame.display.set_mode(RESOLUTION)


from core.SpriteManager import SpriteManager
builtins.sprite_manager = SpriteManager('img/')

from core.DataManager import DataManager
builtins.data_manager = DataManager()

from core.SoundManager import SoundManager
builtins.sound_manager = SoundManager('music/', 'sound/')

from core.GameManager import GameManager
builtins.game_manager = GameManager()

from core.RenderManager import RenderManager
builtins.render_manager = RenderManager()

from core.MapManager import MapManager
builtins.map_manager = MapManager()

from core.Mouse import Mouse
builtins.mouse = Mouse()

from core.Menu import Menu
builtins.menu_manager = Menu()

class Difficulty(IntEnum):
    Normal, Hard, Hardcore = range(3)

builtins.Difficulty = Difficulty


builtins.FONT = pygame.font.Font('fonts/Vera-Bold.ttf', 25)
builtins.BLACK = (0, 0, 0)
builtins.RED = (255, 0, 0)
builtins.GREY = (200, 200, 200)
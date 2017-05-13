import pygame, sys
from pygame.locals import *



class SpriteManager:
    def __init__(self, path):
        self.path = path
        self.sprites = {}

    def __call__(self, name, cords):
        y, x = cords
        return self.sprites[name][y][x]

    def load_sprites(self, name, size):
        width, height = size
        sheet = pygame.image.load(self.path + name).convert_alpha()  # load
        sheet_width, sheet_height = sheet.get_width(), sheet.get_height()
        if sheet_width % width != 0 or sheet_height % height != 0:
            # check if image size is multiply of spritesize
            eprint('COUDNT LOAD:', name)

        # array of sprites
        sprites = [[None for _ in range(sheet_width // width)] for _ in range(sheet_height // height)]

        for i in range(len(sprites)):
            for j in range(len(sprites[0])):
                sheet.set_clip(pygame.Rect(j * width, i * height, width, height))
                sprites[i][j] = sheet.subsurface(sheet.get_clip())

        asset_name = name.split('.')[0]
        self.sprites[asset_name] = sprites


if __name__ == '__main__':
    pygame.init()
    GREY = (200, 200, 200)
    screen = pygame.display.set_mode((500, 500))
    sprite_manager = SpriteManager('../img/')
    sprite_manager.load_sprites('balls.png', (50, 50))
    sprites = sprite_manager.sprites['balls']

    backdrop = pygame.Rect(0,0, 500, 500)
    screen.fill(GREY)
    for i in range(len(sprites)):
        for j in range(len(sprites[0])):
            screen.blit(sprite_manager('balls', (j, i)), (j*50, i*50, 50, 50))
    pygame.display.flip()
    input()
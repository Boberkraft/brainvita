if __name__ == '__main__':
    from SpriteManager import SpriteManager
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    sprite_manager = SpriteManager('../img/')


class Ball:
    sprite_manager.load_sprites('balls.png', (50, 50))

    ball_types = [(0, 0),
                  (1, 0),
                  (2, 0)]

    rect = pygame.Rect((0, 0, 50, 50))
    sprite = sprite_manager('balls', (0, 0))
    sprite_shadow = sprite_manager('balls', (0, 1))

    def __init__(self, rect, shadow=None):
        self.rect = rect
        if shadow:
            self.shadow = shadow


    @classmethod
    def change_sprite(cls, val):
        s, _ = Ball.ball_types[val.value]
        cls.sprite = sprite_manager('balls', (s, 0))
        cls.sprite_shadow = sprite_manager('balls', (s, 1))

class Hole(Ball):
    sprite = sprite_manager('balls', (0,2))

if __name__ == '__main__':
    Ball.change_sprite(0, 0)
    screen.blit(Ball.sprite, (0, 0, 50, 50))
    pygame.display.update()
    input()
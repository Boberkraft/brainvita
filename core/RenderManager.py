from init import *
from core.Ball import Ball

class Renderer:
    def __init__(self, seq, sprite):
        self.seq = seq
        self.sprite = sprite

    def render(self):
        for x in self.seq:
            if isinstance(x, list):
                self.render(x, self.sprite)
            else:
                if self.check(x):
                    render_manager.render(x, self.sprite)

    def check(self, x):
        """Method to be overiden"""
        return True

class RenderManager:
    sprite_manager.load_sprites('borders.png', (50, 2))
    border_light = sprite_manager('borders', (0, 0))
    border_shadow = sprite_manager('borders', (1, 0))
    to_render = []
    renderers = []

    no_shadow_ball = None

    def __init__(self):
        pass

    def reset(self):
        del self.to_render
        self.to_render = []

    def add(self, obj):
        self.to_render.append(obj)


    def render_all(self):
        game_display.fill(GREY)  # default background color
        self.draw_background()

        for renderer in self.renderers:
            renderer.render()

            # self.render(self.to_render)


    def add_renderer(self, obj):
        self.renderers.append(obj)

    def render(self, rect, sprite):
        game_display.blit(sprite, rect)

    def draw_background(self):
        map_to_render = map_manager.map
        BORDER_SHADOW = self.border_shadow
        BORDER_LIGHT = self.border_light
        # oh god
        def draw_on_left(x, y):
            surf = pygame.transform.rotate(BORDER_SHADOW, 90)
            rect = surf.get_rect()
            rect.x, rect.y = x, y
            game_display.blit(surf, rect)

        def draw_on_right(x, y):
            surf = pygame.transform.rotate(BORDER_LIGHT, 90)
            rect = surf.get_rect()
            rect.x, rect.y = x + Ball.rect.width, y
            game_display.blit(surf, rect)

        def draw_on_top(x, y):
            surf = BORDER_SHADOW
            rect = surf.get_rect()
            rect.x, rect.y = x, y
            game_display.blit(surf, rect)

        def draw_on_bottom(x, y):
            surf = BORDER_LIGHT
            rect = surf.get_rect()
            rect.x, rect.y = x, y + Ball.rect.height
            game_display.blit(surf, rect)

        for y, row in enumerate(map_to_render):
            for x, is_ball in enumerate(row):
                if is_ball == 0:
                    try:
                        if map_to_render[y][x - 1] != 0 and x - 1 >= 0:
                            draw_on_left(x * Ball.rect.width, y * Ball.rect.height)
                    except IndexError:
                        pass
                    try:
                        if map_to_render[y][x + 1] != 0:
                            draw_on_right(x * Ball.rect.width, y * Ball.rect.height)
                    except IndexError:
                        pass
                    try:
                        if map_to_render[y - 1][x] != 0 and y - 1 >= 0:
                            draw_on_top(x * Ball.rect.width, y * Ball.rect.height)
                    except IndexError:
                        pass
                    try:
                        if map_to_render[y + 1][x] != 0:
                            draw_on_bottom(x * Ball.rect.width, y * Ball.rect.height)
                    except IndexError:
                        pass
                    # end of oh god

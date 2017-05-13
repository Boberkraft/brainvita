from core.Ball import Ball
from core.RenderManager import Renderer


class Menu:
    """I DON NOT TAKE RESPOSIBILITY FOR THIS CLASS"""
    sprite_manager.load_sprites('menu.png', (25, 25))
    retry_button = sprite_manager('menu', (0,0))
    home_button = sprite_manager('menu', (0,1))

    class Button:
        def __init__(self, name, caption, rect,):
            self.name = name
            self.text = None
            self.caption = caption
            self.text_rect = None
            self.rect = rect
            self.text_rect = rect

        def set_text(self):
            if isinstance(self.name, str):
                self.text = FONT.render(self.caption, True, (97, 97, 97))
            else:
                self.text = FONT.render(self.caption, True, (97 * self.name, 97, 97))
            self.text_rect = self.text.get_rect(center=self.rect.center)

    all_buttons = []
    func_buttons = []
    map_arena = []

    button_size = (25, 25)

    def add_func_button(self, name, img):

        size = self.button_size[0]
        new_button_rect = pygame.Rect(len(self.func_buttons) * size * 1.5 + 10,
                                      10,
                                      size,
                                      size)
        new_button = self.Button(name, 'you cant see this!', new_button_rect)
        new_button.text = img
        self.func_buttons.append(new_button)

    def add_button(self, name, caption):
        # render in the middle of screen
        new_button_rect = pygame.Rect((3 * Ball.rect.width,  # x
                                       (len(self.map_arena)) *  Ball.rect.height),  # y
                                      ((len(map_manager.map[0]) - 6) * Ball.rect.width ,  # width
                                       Ball.rect.width))  # height
        new_button = self.Button(name, caption, new_button_rect)
        new_button.set_text()
        self.all_buttons.append(new_button)

        new_row = [0 if abs(index - len(map_manager.map)//2) > 1 else 1 for index, y in enumerate(map_manager.map)]
        self.map_arena.append(new_row)

        self.map_arena.append([0] * len(map_manager.map[0]))

    def take_free_space(self):
        for _ in range(9 - len(self.map_arena)):
            self.map_arena.append([0] * len(map_manager.map[0]))

    def click_menu(self, pos):
        x, y = pos
        clicked = [button for button in self.all_buttons if button.rect.collidepoint(x, y)]
        if clicked:
            clicked = clicked[0]
            # ok you licked on something
            game_manager.exit = True
            game_manager.difficulty = clicked.name
            game_manager.lvl = 1


    def click_func(self, pos):

        x, y = pos
        clicked = [button for button in self.func_buttons if button.text_rect.collidepoint(x, y)]
        if clicked:
            clicked = clicked[0]
            if clicked.name == 'retry':
                pass
            if clicked.name == 'home':
                game_manager.lvl = 'Menu'
            game_manager.exit = True

    def reset_buttons(self):
        self.all_buttons = []
        self.func_buttons = []
        self.map_arena = []
        self.map_arena.append([0] * len(map_manager.map[0]))

    def make_menu(self):
        self.reset_buttons()
        for name, member in Difficulty.__members__.items():
            # adds buttons to main menu from list of available levels of hardness
            self.add_button(member, name)
        self.take_free_space()
        # GLOB.actual_map = 1
        # # you are in main menu :)
        # draw_background(Menu.map_arena)  # draws contours of main menu
        for button in self.all_buttons:
            # draws all buttons
            render_manager.add_renderer(Renderer([button.text_rect], button.text))
        return self.map_arena

    def make_winning_screen(self):
        self.reset_buttons()
        menu_manager.make_func_buttons()
        self.add_button(game_manager.difficulty, 'You won!')
        self.take_free_space()

        but = self.all_buttons[0]
        render_manager.add_renderer(Renderer([but.text_rect], but.text))
        return self.map_arena

    def make_func_buttons(self):
        self.reset_buttons()
        self.add_func_button('home', self.home_button)
        self.add_func_button('retry', self.retry_button)

        for button in self.func_buttons:
            # draws all buttons
            render_manager.add_renderer(Renderer([button.text_rect], button.text))

# class Overlay:
#     def __init__(self, alpha, color):
#         self.alpha = alpha
#         self.color = color
#
#     def draw(self):
#         s = pygame.Surface(RESOLUTION)
#         s.set_alpha(self.alpha)
#         s.fill(self.color)
#         game_display.blit(s, (0, 0))  # renders on whole screen
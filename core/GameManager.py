from core.Ball import Ball

class GameManager:

    all_balls = []
    all_empty_balls = []
    lvl = None
    difficulty = None
    exit = False
    new_theme = True
    max_maps = 2

    def load(self):
        Ball.change_sprite(self.difficulty)
        menu_manager.make_func_buttons()
        map_manager.map = data_manager.get_data('maps/{}.map'.format(self.lvl))  # load this map
        map_manager.make_map()
        if self.lvl == 1:
            game_manager.new_theme = True
            sound_manager.set_theme(self.difficulty.name)


    def make_menu(self):
        map_manager.map = menu_manager.make_menu()
        sound_manager.set_theme('Menu')
        game_manager.new_theme = True

    def won(self):
        map_manager.map = menu_manager.make_winning_screen()
        self.difficulty = Difficulty.Normal
        self.lvl = 'Menu'
        game_manager.new_theme = True
        sound_manager.set_theme('win')

    def setup(self):
        render_manager.renderers = []  # delete renderers

        if self.lvl == 'Menu':
            # load menu
            self.make_menu()
        else:
            # load map
            if self.lvl > self.max_maps:
                # no more maps to load
                self.won()

            else:
                self.load()



        if self.new_theme:
            sound_manager.play_background()

        self.new_theme = False

        self.exit = False

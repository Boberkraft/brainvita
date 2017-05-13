
class Mouse:
    ball = None
    ball_cords = None
    last_pos = None

    def __init__(self):
        self.initial_cords = None

    def click(self, pos):
        if game_manager.lvl != 'Menu':
            # you are in game
            menu_manager.click_func(pos)
            if self.ball:
                self.set_ball()
            else:
                self.grab_ball(pos)
        else:
            # you are in menu
            menu_manager.click_menu(pos)
            menu_manager.click_func(pos)
            pass

    def grab_ball(self, pos):
        self.ball = map_manager.get_ball(pos)
        if self.ball is not None:
            # in not none
            self.initial_cords = map_manager.get_cords(self.ball)
            self.last_pos = pygame.mouse.get_pos()
            self.ball = map_manager.move_to_front(self.ball)
            render_manager.no_shadow_ball = self.initial_cords
        else:
            pass

    def set_ball(self):
        self.last_pos = pygame.mouse.get_pos()
        ball_cords = map_manager.get_cords(self.ball)
        if map_manager.place(self.initial_cords, ball_cords):
            # ball placed
            self.move()
            sound_manager.play_sound()
        else:
            # ball not placed
            # placing it where it was
            map_manager.place(self.initial_cords, self.initial_cords)
        # map_manager.all_balls.remove(self.ball)
        map_manager.remove(ball=self.ball)
        self.ball = None

    def move(self):
        if not self.ball:
            return

        pos = pygame.mouse.get_pos()

        if game_manager.difficulty == Difficulty.Hardcore:
            dx = self.last_pos[0] - pos[0]
            dy = self.last_pos[1] - pos[1]

            new_pos = (pos[0] + dx * 2, pos[1] + dy *2)
            x,y = new_pos
            if not (x < 0 or y < 0 or x > 50 * len(map_manager.map) or y > 50 * len(map_manager.map)):
                 pygame.mouse.set_pos(new_pos)
            else:
                self.set_ball()
                return
        else:
            new_pos = pos
        self.ball.rect.center = new_pos
        self.last_pos = new_pos
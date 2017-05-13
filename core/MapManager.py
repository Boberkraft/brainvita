from core.Ball import Ball
from core.Ball import Hole
from core.RenderManager import Renderer

class MapManager:
    all_balls = []  # rectangles of every ball
    all_holes = []

    class ShadowRenderer(Renderer):
        def check(self, x):
            """Check"""
            if mouse.ball and x == mouse.ball.rect:
                return False
            return True

    map = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]


    def move_to_front(self, obj):
        """Move object to be first in rendering and returns its"""
        index = self.all_balls.index(obj)
        self.all_balls[-1], self.all_balls[index] = self.all_balls[index], self.all_balls[-1]
        return self.all_balls[-1]

    def make_map(self):
        for _ in range(len(self.all_balls)):
            del self.all_balls[-1]

        for _ in range(len(self.all_holes)):
            del self.all_holes[-1]

        for y, row in enumerate(self.map):
            for x, is_ball in enumerate(row):
                if is_ball:
                    new_ball_rect = Ball.rect
                    new_ball_rect = new_ball_rect.move(x * Ball.rect.width, y * Ball.rect.height)
                    self.all_holes.append(Hole(new_ball_rect))  # adds to list of holes
                    if is_ball == 1:
                        self.all_balls.append(Ball(new_ball_rect.copy()))  # its a ball, so add to list of balls

        render_manager.add_renderer(Renderer(self.all_holes, Hole.sprite))
        render_manager.add_renderer(self.ShadowRenderer(self.all_balls, Ball.sprite_shadow))
        render_manager.add_renderer(Renderer(self.all_balls, Ball.sprite))

    def get_ball(self, pos):
        x, y = pos
        ball_clicked = [ball for ball in self.all_balls if ball.rect.collidepoint(x, y)]
        if ball_clicked:
            return ball_clicked[0]
        else:
            return None

    def __init__(self, map=False):
        if map:
            # by default map dont changes
            self.map = map

    def check(self, who, where):
        """Checks if balls are separated by one square"""
        x = abs(who[1] - where[1])
        y = abs(who[0] - where[0])

        if max(x, y) == 2:
            if min(x, y) == 0:
                return True
        return False
        # return any([abs(x - y) == 2 or abs(x - y) == 0 for x, y in zip(who, where)])

    def remove(self, cords=None, ball=None):
        if cords:
            x, y = self.get_pos(cords)
            [self.all_balls.remove(ball) for ball in self.all_balls if ball.rect.collidepoint(x, y) if ball != mouse.ball]
        if ball:
            self.all_balls.remove(ball)



    def place(self, source, dest):
        """Places ball.
            
            :returns True or False if failed
        """
        if source == dest:
            self.make_ball(dest)


            return True
        if self.map[dest[1]][dest[0]] == 2:
            if self.check(source, dest):
                offset = ((source[1] - dest[1]) // 2, (source[0] - dest[0]) // 2)
                ball_between = (dest[0] + offset[1], dest[1] + offset[0])
                if self.map[ball_between[1]][ball_between[0]] == 1:
                    self.remove(ball_between)
                    self.map[ball_between[1]][ball_between[0]] = 2
                    self.map[source[1]][source[0]] = 2
                    self.map[dest[1]][dest[0]] = 1
                    self.make_ball(dest)
                    self.remove(source)
                    if len(self.all_balls) is 2:
                        game_manager.lvl += 1
                        game_manager.exit = True
                    return True
        return False

    def make_ball(self, where):
        """Makes rect of new ball"""
        x, y = self.get_pos(where)
        rect = pygame.Rect(x, y, Ball.rect.width, Ball.rect.height)
        self.all_balls.append(Ball(rect))

    @staticmethod
    def get_cords(who):
        """Returns coordinates of a square"""
        return int(round(who.rect.x / Ball.rect.width)), int(round(who.rect.y / Ball.rect.height))

    @staticmethod
    def get_pos(who):
        """Returns position on a real screen in pixels"""
        return who[0] * Ball.rect.width, who[1] * Ball.rect.height
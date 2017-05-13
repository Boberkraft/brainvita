"""
author Andrzej Bisewski
andrzej dot bisewski at gmail.com
just credit me :) have fun
"""
import init

game_manager.difficulty = Difficulty.Normal
game_manager.lvl = 'Menu'
while True:
    game_manager.setup()

    while game_manager.exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # you clicked quit
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # you clicked
                mouse.click(event.pos)  # position of cursor
        mouse.move()
        render_manager.render_all()

        pygame.display.update()  # updates screen

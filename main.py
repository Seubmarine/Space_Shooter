import pyxel as px
from entities import Entities


class App:
    def __init__(self):
        px.init(160, 160)
        self.x = 0
        self.y = 0
        px.run(self.update, self.draw)

    def update(self):

        def update_player():
            p_speed = 3
            if px.btnp(px.KEY_UP, 1, 1):
                self.y -= p_speed
            if px.btnp(px.KEY_DOWN, 1, 1):
                self.y += p_speed
            if px.btnp(px.KEY_LEFT, 1, 1):
                self.x -= p_speed
            if px.btnp(px.KEY_RIGHT, 1, 1):
                self.x += p_speed
        update_player()

        # Activate the Entity Class, Entity class only activate a draw rect for now
        self.player = Entities(self.x, self.y, self.x + 7, self.y + 7)

    def draw(self):
        px.cls(0)
        self.player.draw()


App()

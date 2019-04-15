import pyxel as px
from entities import Entities, Spacecraft, Bullet

WIDTH = 150
LENGTH = 200

class App:
    def __init__(self):
        px.init(WIDTH, LENGTH)
        self.x = WIDTH // 2
        self.y = LENGTH // 2
        self.shoot = False
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
        self.player = Spacecraft(self.x, self.y, self.x + 15, self.y + 15, 4)
        self.bullet = Bullet(self.x + 7, self.y - 2, self.x + 8, self.y - 1, 5)
        self.bullet.update()

    def draw(self):
        px.cls(0)
        self.player.draw()
        self.bullet.draw()
        
        # px.rect(self.x + 7, self.y - 2, self.x + 8, self.y - 1, 7)
        
        # Test line
        px.line(55, 23, 65, 90, 12)

App()

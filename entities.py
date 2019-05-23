import pyxel as px
from time import time

WIDTH = 150
HEIGHT = 200
GREEN = 11


class Entities:
    def __init__(self, x, y, h, w, col):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.col = col

    def update(self):
        pass

    def draw(self):
        pass


class En3(Entities):
    def __init__(self, x, y, h, w, col):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.stt = time()
        self.distance = 84
        super().__init__(x, y, h, w, col)

    def update(self, dt, t, stt):

        modulo = (t - self.stt) % 1

        if modulo <= 0.25:
            self.y += self.distance * dt
        elif modulo <= 0.50:
            self.x -= self.distance * dt
        elif modulo <= 0.75:
            self.y += self.distance * dt
        elif modulo <= 1:
            self.x += self.distance * dt

        if self.x > WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH
        elif self.y > HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT

    def draw(self):
        px.circb(self.x, self.y, 4, self.col)


class Bullet(Entities):

    def update(self, dt):
        self.y -= 120 * dt

    def draw(self):
        px.rect(self.x, self.y, self.x + self.h, self.y + self.w, self.col)


class Spacecraft(Entities):
    def __init__(self, x, y, h, w, col):
        self.speed = 100  # player speed per second
        super().__init__(x, y, h, w, col)

    def borders_collision(self):
        if self.x > WIDTH - self.h - 1:
            self.x = WIDTH - self.h - 1
        if self.x <= 0:
            self.x = 0
        if self.y > HEIGHT - self.w - 1:
            self.y = HEIGHT - self.w - 1
        if self.y < 0:
            self.y = 0

    def player_movements(self, dt, player_bullets):
        if px.btnp(px.KEY_UP, 1, 1):
            self.y -= self.speed * dt
        elif px.btnp(px.KEY_DOWN, 1, 1):
            self.y += self.speed * dt
        elif px.btnp(px.KEY_LEFT, 1, 1):
            self.x -= self.speed * dt
        elif px.btnp(px.KEY_RIGHT, 1, 1):
            self.x += self.speed * dt
        if px.btnp(px.KEY_SPACE, 12, 12):
            player_bullets.append(Bullet(self.x + 7, self.y - 2, 2, 2, 7))

    def update(self, dt, player_bullets):
        self.player_movements(dt, player_bullets)
        self.borders_collision()

    def draw(self):
        # px.rectb(self.x, self.y, self.x + self.h, self.y + self.w, self.col)
        px.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)

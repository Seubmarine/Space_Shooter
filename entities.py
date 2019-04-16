import pyxel as px
from time import time

WIDTH = 150
LENGTH = 200
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


class En3:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = LENGTH / 2
        self.speed = 3
        self.pt = 0
        self.distance = 40
        self.modulo = 0
        self.dt = 0
        self.speed = 2

    def update(self):

        t = time()       # actual time
        self.dt = t - self.pt  # give the time between the previous update and now
        self.pt = t      # previous_time set to the actual time so that the next time it will be compared it become the differance with the new update

        self.modulo = t % self.speed

        print(self.modulo)

        if self.modulo < (self.speed / 4):
            self.y += self.distance * self.dt
        elif self.modulo < (self.speed / 4) * 2:
            self.x -= self.distance * self.dt
        elif self.modulo < (self.speed / 4) * 3:
            self.y += self.distance * self.dt
        elif self.modulo < (self.speed / 4)* 4:
            self.x += self.distance * self.dt

        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y > LENGTH:
            self.y = 0
        if self.y < 0:
            self.y = LENGTH

    def draw(self):
        px.circb(self.x, self.y, 4, GREEN)


class Bullet(Entities):

    def update(self):
        self.y -= 2
        if self.y < 0:
            del self  # la bullet sort de l'écran

    def draw(self):
        px.rect(self.x, self.y, self.x + self.h, self.y + self.w, self.col)


class Spacecraft(Entities):
    def __init__(self, x, y, h, w, col):
        self.speed = 100  # player speed per second
        self.pt = 0
        super().__init__(x, y, h, w, col)

    def update(self, player_bullets):
        t = time()
        dt = t - self.pt
        self.pt = t

        def borders_collision():
            if self.x > WIDTH - self.h - 1:
                self.x = WIDTH - self.h - 1
            if self.x <= 0:
                self.x = 0
            if self.y > LENGTH - self.w - 1:
                self.y = LENGTH - self.w - 1
            if self.y < 0:
                self.y = 0

        if px.btnp(px.KEY_UP, 1, 1):
            self.y -= self.speed * dt
        if px.btnp(px.KEY_DOWN, 1, 1):
            self.y += self.speed * dt
        if px.btnp(px.KEY_LEFT, 1, 1):
            self.x -= self.speed * dt
        if px.btnp(px.KEY_RIGHT, 1, 1):
            self.x += self.speed * dt
        if px.btnp(px.KEY_SPACE, 12, 12):
            player_bullets.append(
                Bullet(self.x + 7, self.y - 2, 2, 2, 7)
            )

        borders_collision()

    def draw(self):
        px.rectb(self.x, self.y, self.x + self.h, self.y + self.w, self.col)

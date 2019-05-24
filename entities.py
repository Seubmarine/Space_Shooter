import pyxel as px
import math
from time import time
from constants import WIDTH, HEIGHT, GREEN, RED, YELLOW


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


class En1:
    def __init__(self, x, y=0, delay=0):
        self.startpoint_x = x
        self.y = y
        self.birth = None
        self.delay = delay

    def update(self, dt, t):

        self.y += 40 * dt
        movx = math.cos((t - self.birth) * 4) * 16
        # this add the first given coordinate + the x movement because x is already changing in the loop
        self.x = self.startpoint_x + movx

        if self.y > HEIGHT:
            self.y = 0

    def draw(self):
        px.rectb(self.x - 8, self.y - 8, self.x + 8, self.y + 8, YELLOW)


class En2:
    def __init__(self, x, delay=0, color=RED, direction=1):
        self.x = x
        self.y = -8
        self.cx = x
        self.cy = self.y
        self.birth = None
        self.delay = delay
        self.color = color
        self.dir = direction

    def update(self, dt, t):

        self.cx += 30 * dt * self.dir
        self.cy += 20 * dt

        movx = math.cos((t - self.birth) * 4) * 16 * self.dir
        movy = math.sin((t - self.birth) * 4) * 16 * - 1

        self.x = self.cx + movx
        self.y = self.cy + movy

        if self.x < 0:
            self.x = WIDTH
            self.cx += WIDTH
        if self.x > WIDTH:
            self.x = 0
            self.cx -= WIDTH
        if self.y < 0:
            self.y = HEIGHT
            self.cy += HEIGHT
        if self.y > HEIGHT:
            self.y = 0
            self.cy -= HEIGHT

    def draw(self):
        px.circb(self.x, self.y, 4, self.color)


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

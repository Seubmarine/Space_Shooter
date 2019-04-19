import pyxel as px
from entities import Entities, Spacecraft, Bullet, En3
from time import time
import math

WHITE = 7
RED = 8
YELLOW = 10
GREEN = 11
BLUE = 12

WIDTH = 150
LENGTH = 200

FPS = 60


class App:
    def __init__(self):
        px.init(WIDTH, LENGTH, fps=FPS)

        self.stt = time()  # Starting Time
        self.pt = self.stt  # Buffer Time
        self.dt = 0  # initialize delta time

        self.player = Spacecraft(WIDTH / 2 - 8, LENGTH / 2 - 8, 15, 15, YELLOW)
        self.player_bullets = []
        self.ennemy = En3(WIDTH / 2, LENGTH / 2, 0, 0, GREEN)

        px.run(self.update, self.draw)

    def update(self):

        t = time()            # actual time
        dt = t - self.pt     # give the time between the previous update and now
        self.pt = t           # previous_time set to the actual time so that the next time it will be compared it become the differance with the new update

        self.player.update(dt, self.player_bullets)
        for bullet in self.player_bullets:
            bullet.update(dt)

        self.ennemy.update(dt, t, self.stt)

    def draw(self):
        px.cls(0)

        # Test line
        px.line(WIDTH / 2, 0, WIDTH/2, LENGTH, RED)
        px.line(0, LENGTH/2, WIDTH, LENGTH/2, RED)

        self.player.draw()
        for bullet in self.player_bullets:
            bullet.draw()

        self.ennemy.draw()


App()

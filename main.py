import pyxel as px
from entities import Entities, Spacecraft, Bullet, En3
from time import time
import math
import threading # for debug every 1 sec

WHITE = 7
RED = 8
YELLOW = 10
GREEN = 11
BLUE = 12

WIDTH = 150
HEIGHT = 200

FPS = 60


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=FPS)

        self.stt = time()  # Starting Time
        self.pt = self.stt  # Buffer Time
        self.dt = 0  # initialize delta time

        self.player = Spacecraft(WIDTH / 2 - 8, HEIGHT / 2 - 8, 15, 15, YELLOW)
        self.player_bullets = []
        self.ennemy = En3(WIDTH / 2, HEIGHT, 0, 0, GREEN)

        # self.run_check() # run debug info every 1 second
        px.run(self.update, self.draw)

    def run_check(self):
        # debug info every 1 second
        threading.Timer(1.0, self.run_check).start()
        print(self.player_bullets)

    def update(self):

        t = time()            # actual time
        dt = t - self.pt     # give the time between the previous update and now
        self.pt = t           # previous_time set to the actual time so that the next time it will be compared it become the differance with the new update

        self.player.update(dt, self.player_bullets)
        for bullet in self.player_bullets:
            bullet.update(dt)
            if bullet.y < 0: # if attribute y of actual bullet is over the screen
                self.player_bullets.pop(0) # delete object at index 0 where the actual bullet is located
        self.ennemy.update(dt, t, self.stt)

    def draw(self):
        px.cls(0)

        # Test line
        px.line(WIDTH / 2, 0, WIDTH/2, HEIGHT, RED)
        px.line(0, HEIGHT/2, WIDTH, HEIGHT/2, RED)

        self.player.draw()
        for bullet in self.player_bullets:
            bullet.draw()

        self.ennemy.draw()


App()

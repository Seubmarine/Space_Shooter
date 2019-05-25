import pyxel as px
from entities import Entities, Spacecraft, Bullet, En1, En2, En3
from constants import FPS, WIDTH, HEIGHT, GREEN, RED, YELLOW
from time import time
import math
import threading  # for debug every 1 sec
import os


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=FPS)
        px.load(os.getcwd() + '/game_assets.pyxel')

        def en2(x, delay=0, col=RED, direction=1):
            for e in range(7):
                d = e * 0.15 + delay
                self.vague.append(
                    En2(x, delay=d, col=col, direction=direction))

        self.stt = time()  # Starting Time
        self.pt = self.stt  # Buffer Time
        self.dt = 0  # initialize delta time

        self.player = Spacecraft(WIDTH / 2 - 8, HEIGHT / 2 - 8, YELLOW)
        self.player_bullets = []
        self.vague = [En3(WIDTH / 2, HEIGHT, 0, GREEN),
                      En1(WIDTH / 3)]
        en2(WIDTH / 8 * 7, direction=-1)

        self.ennemis = []
        # self.run_check() # run debug info every 1 second
        px.run(self.update, self.draw)

    def run_check(self):
        # debug info every 1 second
        threading.Timer(1, self.run_check).start()
        print(self.player_bullets)

    def spawn(self, t):
        if len(self.vague):
            time_past = t - self.stt
            for ennemi in self.vague.copy():
                if time_past >= ennemi.delay:
                    ennemi.birth = t
                    self.ennemis.append(ennemi)
                    self.vague.remove(ennemi)

    def update(self):

        t = time()       # actual time
        dt = t - self.pt  # give the time between the previous update and now
        self.pt = t      # previous_time set to the actual time so that the next time it will be compared it become the differance with the new update

        self.spawn(t)

        self.player.update(dt, self.player_bullets)
        for bullet in self.player_bullets:
            bullet.update(dt)
            if bullet.y < 0:  # if attribute y of actual bullet is over the screen
                # delete object at index 0 where the actual bullet is located
                self.player_bullets.pop(0)

        for e in self.ennemis:
            e.update(dt, t)

    def draw(self):
        px.cls(0)

        # Test line
        px.line(WIDTH / 2, 0, WIDTH/2, HEIGHT, RED)
        px.line(0, HEIGHT/2, WIDTH, HEIGHT/2, RED)

        # Game intended object
        self.player.draw()
        for bullet in self.player_bullets:
            bullet.draw()
        for e in self.ennemis:
            e.draw()


App()

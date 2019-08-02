import pyxel as px
from entities import Spacecraft, Bullet, En1, En2, En3, Star, EnemiesBullet
from constants import FPS, WIDTH, HEIGHT, GREEN, RED, YELLOW, PURPLE, WHITE, CYAN
from time import time
from events import Button
import math
import threading  # for debug every 1 sec
import os


def collision_detection(x1, x2, y1, y2, radius1, radius2):
    """Pythagore's theorem to know the distance between two points"""
    calcul = (x1 - x2) ** 2 + (y1 - y2)**2
    maxradius = (radius1 + radius2)**2
    return calcul <= maxradius


class MainScreen():
    def __init__(self):
        self.play_btn = Button(WIDTH/2, HEIGHT/2, 'Play')
        self.settings_btn = Button(WIDTH/2, HEIGHT/8*5, 'Settings')
        self.quit_btn = Button(WIDTH/2, HEIGHT/4*3, 'Quit')

    def update(self):
        self.play_btn.update()
        self.settings_btn.update()
        self.quit_btn.update()

    def draw(self):
        self.play_btn.draw()
        self.settings_btn.draw()
        self.quit_btn.draw()


class App:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=FPS)
        px.load(os.getcwd() + '/game_assets.pyxel')
        px.mouse(True)

        def en2(x, delay=0, col=RED, direction=1):
            for e in range(7):
                d = e * 0.15 + delay
                self.vague.append(
                    En2(x, delay=d, col=col, direction=direction))

        self.stt = time()  # Starting Time
        self.pt = 0  # Buffer Time
        self.pause_time = 0
        self.buffer_time = 0
        self.slowtime = 1
        self.pause = False

        self.starfield = []

        for _ in range(int(HEIGHT/6.5)):
            self.starfield.append(Star())

        self.main_screen = MainScreen()
        self.player = Spacecraft(WIDTH / 2 - 8, HEIGHT / 2 - 8, YELLOW)
        self.enemy_bullets = []
        self.player_bullets = []
        self.vague = [En1(WIDTH / 3), En1(WIDTH/4*3, 3, col=CYAN),
                      En3(WIDTH / 2, HEIGHT, 0, GREEN), ]
        en2(WIDTH / 8 * 7, direction=-1)
        en2(WIDTH / 8 * 2, 4, PURPLE)
        en2(WIDTH / 16 * 9, 10, CYAN)
        self.ennemis = []
        # self.run_check() # run debug info every 1 second
        px.run(self.update, self.draw)

    def run_check(self):
        """debug info every 1 second, need to kill terminal after use"""
        threading.Timer(1, self.run_check).start()
        print(self.vague)

    def spawn(self, t):
        """For every enemy in the vague transfer it to the ennemis list when the given set time of the enemy happens """
        if len(self.vague):
            time_past = t
            for ennemi in self.vague.copy():
                if time_past >= ennemi.delay:
                    ennemi.birth = t
                    self.ennemis.append(ennemi)
                    self.vague.remove(ennemi)

    def update_entity(self, dt, t):
        """Update all entity based on time and collision"""
        self.player.update(dt, self.player_bullets)
        for star in self.starfield:
            star.update(dt)
        for bullet in self.player_bullets:
            bullet.update(dt)
        for e_bullet in self.enemy_bullets:
            e_bullet.update(dt)
            if e_bullet.y < 0 or e_bullet.y > HEIGHT or e_bullet.x < 0 or e_bullet.x > WIDTH:
                # Destroy bullet when they collide with the screen border
                self.enemy_bullets.remove(e_bullet)
            if self.player and len(self.enemy_bullets):
                if collision_detection(self.player.x, e_bullet.x, self.player.y, e_bullet.y, self.player.radius, e_bullet.radius):
                    pass
        for e in self.ennemis:
            e.update(dt, t, self.enemy_bullets, self.player)
            for bullet in self.player_bullets:
                if bullet.y < 0:  # if attribute y of actual bullet is over the screen
                    # delete object at index 0 where the actual bullet is located
                    self.player_bullets.remove(bullet)
                if len(self.ennemis) and len(self.player_bullets):
                    if collision_detection(e.x, bullet.x, e.y, bullet.y, e.radius, bullet.radius):
                        # e.impact_effect()
                        # bullet.impact_effect
                        self.ennemis.remove(e)
                        self.player_bullets.remove(bullet)

    def update(self):
        """Game loop for coordinate, time, event, update and more"""
        looptime = time() - self.stt  # time since the loop started

        if self.pause is True:
            t = self.buffer_time
            self.pause_time = looptime - self.buffer_time
        else:
            t = looptime - self.pause_time

        # give the time between the previous update and now
        dt = (t - self.pt) * self.slowtime
        self.pt = t       # previous_time set to the actual time so that the next time it will be compared it become the differance with the new update
        self.spawn(t)  # spawn ennemy in vague inside the game
        self.update_entity(dt, t)  # update all entity of the game

        if px.btnp(px.KEY_P):
            if self.pause is False:
                self.pause = True
                self.buffer_time = t
                self.slowtime = 0
            elif self.pause is True:
                self.pause = False
                self.slowtime = 1

        if px.btnp(px.KEY_BACKSPACE) and self.main_screen is None:
            self.main_screen = MainScreen()
        if not self.main_screen is None:
            self.main_screen.update()
            if self.main_screen.play_btn.do_action:
                self.main_screen = None
            elif self.main_screen.quit_btn.do_action:
                exit()

    def draw(self):
        """Game loop for drawing on the screen"""
        px.cls(1)

        if not self.main_screen is None:
            self.main_screen.draw()

        # Game intended object
        for star in self.starfield:
            star.draw()
        self.player.draw()
        for bullet in self.player_bullets:
            bullet.draw()
        for e_bullet in self.enemy_bullets:
            e_bullet.draw()
        for e in self.ennemis:
            e.draw()


App()

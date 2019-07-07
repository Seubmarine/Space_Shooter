import pyxel as px
import math
from time import time
from constants import WIDTH, HEIGHT, GREEN, RED, YELLOW, WHITE, CYAN, PURPLE
from random import randint


def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)


class Entities:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.col = col

    def impact_effect(self):
        pass


class Star(Entities):
    def update_speed(self):
        if self.radius == 0:
            return randint(4, 5)
        elif self.radius == 1:
            return randint(6, 7)
        else:
            return randint(8, 9)

    def __init__(self):
        self.radius = randint(0, 2)
        self.speed = self.update_speed() / 10
        self.x = randint(0, WIDTH - self.radius)
        self.y = randint(0, HEIGHT - self.radius)

    def update(self, dt):
        vy = 100 / self.speed * dt
        self.y += vy
        if self.y >= HEIGHT:
            self.radius = randint(1, 3)
            self.speed = self.update_speed() / 10
            self.y = 0
            self.x = randint(0, WIDTH - self.radius)

    def draw(self):
        px.rect(self.x, self.y, self.x + self.radius, self.y + self.radius, 6)


class Enemies(Entities):
    def __init__(self, x, y, delay, col, sprites):
        self.birth = None
        self.delay = delay
        self.sprites = sprites
        self.bullet_delay = int(time() + delay + 2)
        super().__init__(x, y, col)

    def spawn_bullet(self, t, birth, bullet_enemy_list, playerx, playery, second=2):
        #print(int(bullet_delay), int(t))
        if self.bullet_delay == int(t):
            self.bullet_delay += 2
            bullet_enemy_list.append(EnemiesBullet(
                self.x, self.y, playerx, playery))

    def choose_sprite(self, t, set_time):
        """set_time is the number of second to change a frame"""
        i = t % (set_time * 2)
        if i < set_time:
            self.sprite = self.sprites[0]
        else:
            self.sprite = self.sprites[1]


class En1(Enemies):
    def __init__(self, x, delay=0, y=0, col=9, sprites=[(0, 48, 0, 16, 16, 0), (0, 64, 0, 16, 16, 0)]):
        self.startpoint_x = x
        self.radius = 8
        self.sprites = sprites
        super().__init__(x, y, delay, col, sprites)

    def update(self, dt, t, enemy_bullets, player):

        self.choose_sprite(t, 1)

        self.y += 40 * dt
        movx = math.cos((t - self.birth) * 4) * 16
        # this add the first given coordinate + the x movement because x is already changing in the loop
        self.x = self.startpoint_x + movx

        if self.y > HEIGHT:
            self.y = 0

        self.spawn_bullet(t, self.birth, enemy_bullets, player.x, player.y)

    def draw(self):
        # px.circb(self.x, self.y, self.radius, self.col)
        px.blt(self.x - self.radius, self.y - self.radius, *self.sprite)
        # super().draw() # to see method heritage of Entities


class En2(Enemies):
    def __init__(self, x, delay=0, col=RED, direction=1, y=0, sprites=[(0, 16, 0, 16, 16, 0), (0, 32, 0, 16, 16, 0)]):
        self.cx = x
        self.cy = self.y = -8
        self.radius = 8
        self.dir = direction
        super().__init__(x, y, delay, col, sprites)

    def update(self, dt, t, enemy_bullets, player):

        self.choose_sprite(t, 0.5)

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
        # px.circb(self.x, self.y, self.radius, self.col)
        px.blt(self.x - self.radius, self.y - self.radius, *self.sprite)
        # super().draw() # to see method heritage of Entities


class En3(Enemies):
    def __init__(self, x=WIDTH / 2, y=HEIGHT / 2, delay=0, col=YELLOW, bullet_delay=2, sprites=[(0, 48, 0, 16, 16, 0), (0, 64, 0, 16, 16, 0)]):
        self.radius = 4
        self.distance = 84
        self.sprites = sprites
        super().__init__(x, y, delay, col, sprites)

    def update(self, dt, t, enemy_bullets, player):
        modulo = (t - self.birth) % 1

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

        self.spawn_bullet(t, self.birth, enemy_bullets, player.x, player.y)

    def draw(self):
        px.circb(self.x, self.y, self.radius, self.col)
        # super().draw() # to see method heritage of Entities


class EnemiesBullet(Entities):
    def __init__(self, x, y, playerx, playery, col=RED):
        self.radius = 1
        self.x = x
        self.y = y
        distx = playerx - self.x
        disty = playery - self.y
        self.hyp = hypotenuse(distx, disty)
        self.vx = distx / self.hyp
        self.vy = disty / self.hyp

        super().__init__(x, y, col)

    def update(self, dt):
        self.x += self.vx * 100 * dt
        self.y += self.vy * 100 * dt

    def draw(self):
        px.rect(self.x - self.radius, self.y - self.radius,
                self.x + self.radius, self.y + self.radius, self.col)


class Bullet(Entities):

    def __init__(self, x, y, col):
        self.radius = 1
        super().__init__(x, y, col)

    def update(self, dt):
        self.y -= 120 * dt

    def draw(self):
        px.rect(self.x - self.radius, self.y - self.radius,
                self.x + self.radius, self.y + self.radius, self.col)
        # super().draw() # to see method heritage of Entities


class Spacecraft(Entities):
    def __init__(self, x, y, col):
        self.speed = 100  # player speed per second
        self.radius = 15 / 2
        super().__init__(x, y, col)

    def borders_collision(self):
        if self.x > WIDTH - self.radius - 1:
            self.x = WIDTH - self.radius - 1
        if self.x < self.radius:
            self.x = self.radius
        if self.y > HEIGHT - self.radius - 1:
            self.y = HEIGHT - self.radius - 1
        if self.y < self.radius:
            self.y = self.radius

    def player_movements(self, dt, player_bullets):
        if px.btnp(px.KEY_UP, 1, 1):
            self.y -= self.speed * dt
        if px.btnp(px.KEY_DOWN, 1, 1):
            self.y += self.speed * dt
        if px.btnp(px.KEY_LEFT, 1, 1):
            self.x -= self.speed * dt
        if px.btnp(px.KEY_RIGHT, 1, 1):
            self.x += self.speed * dt
        if px.btnp(px.KEY_SPACE, 12, 12):
            player_bullets.append(Bullet(self.x, self.y - 2, self.col))

    def update(self, dt, player_bullets):
        self.player_movements(dt, player_bullets)
        self.borders_collision()

    def draw(self):
        px.blt(self.x - self.radius, self.y - self.radius, 0, 0, 0, 16, 16, 0)
        # super().draw() # to see method heritage of Entities

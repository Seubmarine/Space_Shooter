import pyxel as px
import math
from vector import Vector2D as Vector2
from time import time
from constants import WIDTH, HEIGHT, GREEN, RED, YELLOW, WHITE, CYAN, PURPLE
from random import randint


class Entities2:
    def __init__(self, x, y, r):
        self.location = Vector2(x, y)
        self.radius = r


class Star(Entities2):
    def __init__(self):
        self.radius = randint(0, 2)
        super().__init__(randint(0, WIDTH - self.radius),
                         randint(0, HEIGHT - self.radius), self.radius)
        self.speed = self.update_speed() / 10

    def update_speed(self):
        if self.radius == 0:
            return randint(4, 5)
        elif self.radius == 1:
            return randint(6, 7)
        else:
            return randint(8, 9)

    def update(self, dt):
        self.location.y += 70 / self.speed * dt
        if self.location.y >= HEIGHT:
            self.radius = randint(1, 3)
            self.speed = self.update_speed() / 10
            self.location.reuseVector(randint(0, WIDTH - self.radius), 0)

    def draw(self):
        px.rect(self.location.x, self.location.y, self.location.x +
                self.radius, self.location.y + self.radius, 6)


class Enemies2(Entities2):
    def __init__(self, x, y, r, delay, sprites):
        self.birth = None
        self.radius = r
        self.delay = delay
        self.sprites = sprites
        self.bullet_delay = delay + 2
        super().__init__(x, y, r)

    def spawn_bullet(self, t, birth, bullet_enemy_list, bulletloc, playerloc, second=2):
        #print(int(bullet_delay), int(t))
        if self.bullet_delay <= t:
            self.bullet_delay += second
            bullet_enemy_list.append(EnemiesBullet(
                bulletloc.x, bulletloc.y, playerloc.x, playerloc.y))

    def choose_sprite(self, t, set_time):
        """set_time is the number of second to change a frame"""
        i = t % (set_time * 2)
        if i < set_time:
            self.sprite = self.sprites[0]
        else:
            self.sprite = self.sprites[1]


class En1(Enemies2):
    def __init__(self, x, delay):
        self.startpointx = x
        super().__init__(x, 0, 8, delay, [
            (0, 48, 0, 16, 16, 0), (0, 64, 0, 16, 16, 0)])

    def update(self, dt, t, enemy_bullets, player):
        self.choose_sprite(t, 1)
        self.velocity = Vector2(math.cos((t - self.birth) * 4), 40*dt)
        self.location.add(self.velocity)
        self.spawn_bullet(t, self.birth, enemy_bullets,
                          self.location, player.location)

        if self.location.y > HEIGHT:
            self.location.y = 0

    def draw(self):
        px.blt(self.location.x - self.radius,
               self.location.y - self.radius, *self.sprite)


class En2(Enemies2):
    def __init__(self, x, delay=0, direction=1, y=0):
        self.dir = direction
        self.sprites = [(0, 16, 0, 16, 16, 0), (0, 32, 0, 16, 16, 0)]
        self.velocity = Vector2(x, -8)
        super().__init__(x, 0, 8, delay, [
            (0, 16, 0, 16, 16, 0), (0, 32, 0, 16, 16, 0)])

    def update(self, dt, t, enemy_bullets, player):

        self.choose_sprite(t, 0.5)

        self.speed = Vector2(30*dt*self.dir, 20*dt)
        self.velocity.add(self.speed)

        self.movement = Vector2(math.cos(
            (t - self.birth) * 4) * 16 * self.dir, math.sin((t - self.birth) * 4) * 16 * - 1)
        self.completemovement = Vector2(self.velocity.x + self.movement.x,
                                        self.velocity.y + self.movement.y)

        self.location.replace(self.completemovement)

        if self.location.x < 0:
            self.location.x = WIDTH
            self.velocity.x += WIDTH
        if self.location.x > WIDTH:
            self.location.x = 0
            self.velocity.x -= WIDTH
        if self.location.y < 0:
            self.location.y = HEIGHT
            self.velocity.y += HEIGHT
        if self.location.y > HEIGHT:
            self.location.y = 0
            self.velocity.y -= HEIGHT

    def draw(self):
        px.blt(self.location.x - self.radius,
               self.location.y - self.radius, *self.sprite)


class En3(Enemies2):
    def __init__(self, x=WIDTH / 2, y=HEIGHT / 2, delay=0, bullet_delay=2):
        self.distance = 100
        super().__init__(x, 0, 4, delay, [
            (0, 48, 0, 16, 16, 0), (0, 64, 0, 16, 16, 0)])

    def update(self, dt, t, enemy_bullets, player):
        modulo = (t - self.birth) % 1

        velocity = self.distance * dt

        if modulo <= 0.25:  # 1/4
            self.location.down(velocity)
        elif modulo <= 0.50:  # 1/2
            self.location.left(velocity)
        elif modulo <= 0.75:  # 1/3
            self.location.down(velocity)
        elif modulo <= 1:  # 3/1
            self.location.right(velocity)

        if self.location.x > WIDTH:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = WIDTH
        elif self.location.y > HEIGHT:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = HEIGHT

        self.spawn_bullet(t, self.birth, enemy_bullets,
                          self.location, player.location)

    def draw(self):
        px.circb(self.location.x, self.location.y, self.radius, YELLOW)
        # super().draw() # to see method heritage of Entities


class EnemiesBullet(Entities2):
    def __init__(self, x, y, playerx, playery):
        super().__init__(x, y, 1)
        self.velocity = Vector2(playerx, playery)
        self.velocity.substract(self.location)
        self.velocity.normalize()
        self.velocity.multiply(100)

    def update(self, dt):
        self.location.delta_velocity(self.velocity, dt)

    def draw(self):
        px.rect(self.location.x - self.radius, self.location.y - self.radius,
                self.location.x + self.radius, self.location.y + self.radius, RED)


class Bullet(Entities2):

    def __init__(self, x, y, col):
        super().__init__(x, y, 1)

    def update(self, dt):
        self.location.up(120 * dt)

    def draw(self):
        px.rect(self.location.x - self.radius, self.location.y - self.radius,
                self.location.x + self.radius, self.location.y + self.radius, 9)
        # super().draw() # to see method heritage of Entities


class Boss1(Enemies2):
    def idle_state(self, t, enemy_bullets):
        if self.bullet_time <= t:
            for _ in range(self.numberofbullets):
                self.bulletloc = Vector2(
                    math.cos(self.i) * 15, math.sin(self.i) * 15)
                self.bulletloc.add(self.location)

                e = EnemiesBullet(
                    self.bulletloc.x, self.bulletloc.y, self.location.x, self.location.y)
                e.velocity.reverse()
                enemy_bullets.append(e)

                self.i += math.radians(self.degreebullet)
            self.bullet_time += self.bullet_delay

    def __init__(self):
        super().__init__(WIDTH/2, HEIGHT/2, 6, 0, None)
        self.i = 0
        self.numberofbullets = 16
        self.degreebullet = 360/self.numberofbullets
        self.distance = 15
        self.bullet_delay = 0.8

    def update(self, dt, t, enemy_bullets, player):

        modulo = (t - self.birth) % 22

        velocity = self.distance * dt

        if modulo <= 3:
            self.location.right(velocity)
        elif modulo <= 6:
            self.location.left(velocity)
            self.bullet_time = t + self.bullet_delay
        elif modulo <= 11:
            self.idle_state(t, enemy_bullets)
        elif modulo <= 14:
            self.location.left(velocity)
        elif modulo <= 17:
            self.location.right(velocity)
            self.bullet_time = t + self.bullet_delay
        elif modulo <= 22:
            self.idle_state(t, enemy_bullets)

    def draw(self):
        px.rect(self.location.x - self.radius, self.location.y - self.radius,
                self.location.x + self.radius, self.location.y + self.radius, 9)


class Spacecraft(Entities2):
    def __init__(self):
        self.speed = 100
        super().__init__(WIDTH / 2, HEIGHT * 0.75, 15/2)

    def borders_collision(self):
        if self.location.x > WIDTH - self.radius - 1:
            self.location.x = WIDTH - self.radius - 1
        if self.location.x < self.radius:
            self.location.x = self.radius
        if self.location.y > HEIGHT - self.radius - 1:
            self.location.y = HEIGHT - self.radius - 1
        if self.location.y < self.radius:
            self.location.y = self.radius

    def player_movements(self, dt, player_bullets):
        velocity = self.speed * dt
        if px.btnp(px.KEY_UP, 1, 1):
            self.location.up(velocity)
        if px.btnp(px.KEY_DOWN, 1, 1):
            self.location.down(velocity)
        if px.btnp(px.KEY_LEFT, 1, 1):
            self.location.left(velocity)
        if px.btnp(px.KEY_RIGHT, 1, 1):
            self.location.right(velocity)
        if px.btnp(px.KEY_SPACE, 12, 12):
            player_bullets.append(
                Bullet(self.location.x, self.location.y - 2, 7))

    def update(self, dt, player_bullets):
        self.player_movements(dt, player_bullets)
        self.borders_collision()

    def draw(self):
        px.blt(self.location.x - self.radius, self.location.y -
               self.radius, 0, 0, 0, 16, 16, 0)

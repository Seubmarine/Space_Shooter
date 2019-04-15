import pyxel as px


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


class Bullet(Entities):

    def update(self):
        self.y -= 2
        if self.y < 0:
            del self # la bullet sort de l'écran

    def draw(self):
        px.rect(self.x, self.y, self.x + self.h, self.y + self.w, self.col)


class Spacecraft(Entities):
    def __init__(self, x, y, h, w, col):
        self.speed = 3
        super().__init__(x, y, h, w, col)

    def update(self, player_bullets):
        if px.btnp(px.KEY_UP, 1, 1):
            self.y -= self.speed
        if px.btnp(px.KEY_DOWN, 1, 1):
            self.y += self.speed
        if px.btnp(px.KEY_LEFT, 1, 1):
            self.x -= self.speed
        if px.btnp(px.KEY_RIGHT, 1, 1):
            self.x += self.speed
        if px.btnp(px.KEY_SPACE, 10, 10):
            player_bullets.append(
                Bullet(self.x + 7, self.y - 2, 2, 2, 7)
            )


    def draw(self):
        px.rect(self.x, self.y, self.x + self.h, self.y + self.w, self.col)

    def shoot(self):
        if px.btnp(px.KEY_SPACE, 1, 1):
            print("Shoot = True")
            # Spacecraft if px.btnp(px.KEY_SPACE, 10, 10): Bullet : px.rect(self.x + 7, self.y - 2, self.x + 8, self.y - 1, 7)

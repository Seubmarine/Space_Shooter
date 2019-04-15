import pyxel as px


class Entities:
    def __init__(self, x, y, h, w, col):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.col = col
        # self.list_entity = []

    def update(self):
        pass

    def draw(self):
        # self.list_entity.append([self.x, self.y, self.h, self.w, self.col])
        # for entity in self.list_entity:
        #     px.rect(*entity)
        pass


class Bullet(Entities):
    pass


class Spacecraft(Entities):
    def __init__(self, x, y, h, w, col):
        self.speed = 3
        super().__init__(x, y, h, w, col)

    def update(self):
        if px.btnp(px.KEY_UP, 1, 1):
            self.y -= self.speed
        if px.btnp(px.KEY_DOWN, 1, 1):
            self.y += self.speed
        if px.btnp(px.KEY_LEFT, 1, 1):
            self.x -= self.speed
        if px.btnp(px.KEY_RIGHT, 1, 1):
            self.x += self.speed

    def draw(self):
        px.rect(self.x, self.y, self.x + self.h, self.y + self.w, self.col)

    def shoot(self):
        if px.btnp(px.KEY_SPACE, 1, 1):
            print("Shoot = True")
            # Spacecraft if px.btnp(px.KEY_SPACE, 10, 10): Bullet : px.rect(self.x + 7, self.y - 2, self.x + 8, self.y - 1, 7)

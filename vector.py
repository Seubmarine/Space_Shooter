from math import sqrt


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector2):
        self.x = self.x + vector2.x
        self.y = self.y + vector2.y

    def substract(self, vector2):
        self.x = self.x - vector2.x
        self.y = self.y - vector2.y

    def delta_velocity(self, vector2, dt):
        self.x += vector2.x * dt
        self.y += vector2.y * dt

    def multiply(self, number):
        self.x = self.x * number
        self.y = self.y * number

    def divide(self, number):
        self.x = self.x / number
        self.y = self.y / number

    def replace(self, vector2):
        self.x = vector2.x
        self.y = vector2.y

    def reuseVector(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return self.x*self.x + self.y*self.y

    def sqrMagnitude(self):
        return sqrt(self.magnitude())

    def normalize(self):
        m = self.sqrMagnitude()
        if m != 0:
            self.divide(m)

    def reverse(self):
        self.x = self.x * -1
        self.y = self.y * -1

    def limit(self, number):
        if self.y <= number:
            self.y = number

    def distancefromvector(self, vector2):
        self.substract(vector2)
        self.normalize()

    def returned(self, vector2):
        return vector2.x, vector2.y

    def collide(self, vector2):
        return (self.x - vector2.x) ** 2 + (self.y - vector2.y)**2

    def up(self, velocity):
        self.y -= velocity

    def down(self, velocity):
        self.y += velocity

    def left(self, velocity):
        self.x -= velocity

    def right(self, velocity):
        self.x += velocity

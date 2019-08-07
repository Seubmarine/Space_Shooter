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
    
    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def normalize(self):
        m = self.magnitude()
        if m != 0:
            self.divide(m)

    def limit(self, number):
        if self.y <= number:
            self.y = number

    def distancefromvector(self,vector2):
        self.substract(vector2)
        self.normalize()

import pyxel as px

class App:
    def __init__(self):
        px.init(160, 120)
        self.x = 0
        self.y = 0
        px.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % px.width
        self.y = (self.y + 1) % px.height

    def draw(self):
        px.cls(0)
        px.rect(self.x, self.y, self.x + 7, self.y + 7, 9)

App()
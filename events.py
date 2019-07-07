import pyxel as px


class Button():
    def __init__(self, x, y, text):
        self.text = text
        self.textlenght = len(self.text) * 1.5
        self.x = x
        self.y = y
        self.sizex = 20
        self.sizey = 8
        self.col = 5

        self.do_action = False

        self.xleft = self.x - self.sizex
        self.xright = self.x + self.sizex
        self.yup = self.y - self.sizey
        self.ydown = self.y + self.sizey

    def update(self):
        if px.mouse_x > self.xleft and px.mouse_x < self.xright and px.mouse_y > self.yup and px.mouse_y < self.ydown:
            self.col = 8
            self.shadow_col = 7
            if px.btnp(px.MOUSE_LEFT_BUTTON, 10, 10):
                print(self.text)
                self.do_action = True
        else:
            self.col = 7
            self.shadow_col = 8

    def draw(self):
        px.rectb(self.xleft, self.yup, self.xright,
                 self.ydown, self.shadow_col)
        px.text(self.x - self.textlenght, self.y, self.text, self.shadow_col)
        px.text(self.x - 1 - self.textlenght, self.y-1, self.text, self.col)

# class Event():
#     def __init__(self, hotkey, gamestate, ellements):
#         self.hotkey = hotkey
#         self.gamestate = gamestate
#         self.ellements = ellements

#     def update(self):
#         for ellement in self.ellements:
#             ellement.update()

#     def draw(self):
#         for ellement in self.ellements:
#             ellement.draw()

# class Pause(Event):
#     def __init__(self):
#         super().__init__(hotkey=px.KEY_P, gamestate=Pause,)

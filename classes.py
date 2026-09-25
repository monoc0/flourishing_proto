def plch():
    print("undefined")

class Scene:
    def __init__(self):
        self.next = self

    def process(self, events, pressed_keys):
        plch()

    def upd(self):
        plch()

    def render(self, screen):
        plch()

    def switch(self, next):
        self.next = next

    def end(self):
        self.switch(None)
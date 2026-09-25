import pygame
from pygame import gfxdraw

pygame.init()

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

class Button:
    def __init__(self, image_path, position, color, text="", scale=1.0, font_name="arial", font_size=24, text_color=(0, 0, 0)):
        self.image = pygame.image.load(image_path).convert_alpha()
        original_width = self.image.get_width()
        original_height = self.image.get_height()
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect(topleft=position)
        self.pressed = False
        self.color = color

        self.font = pygame.font.SysFont(font_name, font_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, window):
        if self.is_hovered():
            image = self.image.copy()
            image.fill(tuple(min(255, int(c*0.35)) for c in self.color), special_flags=pygame.BLEND_RGB_MULT)
            window.blit(image, self.rect)
        else:
            image = self.image.copy()
            image.fill(self.color, special_flags=pygame.BLEND_RGB_MULT)
            window.blit(image, self.rect)
        window.blit(self.text_surf, self.text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos): 
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True

        if not mouse_pressed:
            self.pressed = False 

        return False 

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
        return False

class choice(Scene):
    def __init__(self, goodScene, badScene, question, on_bad=None, on_good=None):
        super().__init__()
        self.goodScene = goodScene
        self.badScene = badScene
        self.on_bad = on_bad
        self.on_good = on_good
        self.font = pygame.font.SysFont("arial", 32)
        self.text_surf = self.font.render(f"{question.question}", True, (0,0,0))
        self.choice1 = Button("btn.png", (0, 360), (128, 255, 192), f"{question.answers[0]}")
        self.choice2 = Button("btn.png", (640, 360), (255, 192, 128), f"{question.answers[1]}")

    def process(self, events, pressed_keys):
        if self.choice1.is_clicked(events):
            if self.on_good:
                self.on_good()
            self.switch(self.goodScene)
        if self.choice2.is_clicked(events):
            if self.on_bad:
                self.on_bad()
            self.switch(self.badScene)

    def upd(self):
        pass

    def render(self, screen):
        screen.fill((200, 200, 200))
        pygame.draw.circle(screen, (192, 192, 192), (screen.get_width()//3, screen.get_height()//3), 340, width=5)
        pygame.draw.circle(screen, (192, 192, 192), (screen.get_width()//3*2, screen.get_height()//4*3), 640, width=10)
        self.choice1.draw(screen)
        self.choice2.draw(screen)
        rect = self.text_surf.get_rect(center=(screen.get_width() // 2, screen.get_height()//4))
        screen.blit(self.text_surf, rect)

class cutscene(Scene):
    def __init__(self, newScene, cutscene, on_proceed=None):
        super().__init__()
        pygame.font.init()
        self.newScene = newScene
        self.on_proceed = on_proceed
        self.font = pygame.font.SysFont("arial", 16)
        self.lines = [line.strip() for line in cutscene.strip().split("\n") if line.strip()]
        self.line_surfs = [self.font.render(line, True, (0, 0, 0)) for line in self.lines]
        self.start = Button("btn.png", (490, 480), (255, 255, 255), "PROCEED", 0.5)

    def process(self, events, pressed_keys):
        if self.start.is_clicked(events):
            if self.on_proceed:
                self.switch(self.on_proceed())
            else:
                self.switch(self.newScene)

    def upd(self):
        pass

    def render(self, screen):
        screen.fill((200, 200, 200))

        pygame.draw.circle(screen, (192, 192, 192), (screen.get_width()//3, screen.get_height()//3), 340, width=5)
        pygame.draw.circle(screen, (192, 192, 192), (screen.get_width()//3*2, screen.get_height()//4*3), 640, width=10)

        start_y = screen.get_height()//2 - (len(self.line_surfs) * 20) // 2
        for i, surf in enumerate(self.line_surfs):
            rect = surf.get_rect(center=(screen.get_width() // 2, start_y + i * 20))
            screen.blit(surf, rect)
        self.start.draw(screen)
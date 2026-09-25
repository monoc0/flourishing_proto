import pygame
from pygame import gfxdraw
import classes
from time import sleep

def run(w, h, fps, start):
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    active = start

    while active != None:
        pressed = pygame.key.get_pressed()

        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active.end()
            else:
                filtered_events.append(event)

        active.process(filtered_events,pressed)
        active.upd()
        active.render(screen)

        active = active.next

        pygame.display.flip()
        clock.tick(fps)

class title(classes.Scene):
    def __init__(self, newScene):
        super().__init__()
        pygame.font.init()
        self.newScene = newScene
        self.font1 = pygame.font.SysFont("times new roman", 64)
        self.text_surf1 = self.font1.render("FLOURISHING", True, (0, 0, 0))
        self.font2 = pygame.font.SysFont("arial", 14)
        self.text_surf2 = self.font2.render("by YUMUL, CALEON, AQUINO, BOBILA, MIRANDA", True, (0, 0, 0))

    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.switch(self.newScene)

    def upd(self):
        pass

    def render(self, screen):
        screen.fill((200, 200, 200))

        pygame.draw.circle(screen, (192, 192, 192), (screen.get_width()//3, screen.get_height()//3), 340, width=5)
        pygame.draw.circle(screen, (192, 192, 192), (screen.get_width()//3*2, screen.get_height()//4*3), 640, width=10)

        rect1 = self.text_surf1.get_rect(center=(screen.get_width() // 2, screen.get_height()//2))
        screen.blit(self.text_surf1, rect1)
        rect2 = self.text_surf2.get_rect(center=(screen.get_width() // 2, screen.get_height()//2+32))
        screen.blit(self.text_surf2, rect2)



class game(classes.Scene):
    def __init__(self, newScene):
        super().__init__()
        self.newScene = newScene

    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.switch(self.newScene)

    def upd(self):
        pass

    def render(self, screen):
        screen.fill((0, 255, 255))

run(1280, 720, 60, title(game(None)))
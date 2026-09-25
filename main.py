import pygame
from pygame import gfxdraw
import classes
from time import sleep
import dialogue

pygame.init()
screen = pygame.display.set_mode((1280, 720))

badCounter = 0

def increment_bad():
    global badCounter
    badCounter += 1
    print(badCounter)  # optional, for debugging

def run(screen, fps, start):

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
        self.start = classes.Button("btn.png", (screen.get_width()//3*2-360, screen.get_height()/3*2), (255, 255, 255), "START", 0.5)

    def process(self, events, pressed_keys):
        if self.start.is_clicked(events):
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
        self.start.draw(screen)

def build_end():
    if badCounter < 1:
        return classes.cutscene(None, dialogue.e_1)
    elif badCounter < 3:
        return classes.cutscene(None, dialogue.e_2)
    else:
        return classes.cutscene(None, dialogue.e_3)

q5 = classes.cutscene(classes.choice(
    classes.cutscene(None, dialogue.q_5a, on_proceed=build_end),
    classes.cutscene(None, dialogue.q_5b, on_proceed=build_end),
    dialogue.q_5,
    on_bad=increment_bad
), dialogue.q_i5)

q4 = classes.cutscene(classes.choice(
    classes.cutscene(q5,dialogue.q_4a),
    classes.cutscene(q5,dialogue.q_4b),
    dialogue.q_4,
    on_bad=increment_bad
),dialogue.q_i4)

q3 = classes.cutscene(classes.choice(
    classes.cutscene(q4,dialogue.q_3a),
    classes.cutscene(q4,dialogue.q_3b),
    dialogue.q_3,
    on_good=increment_bad
),dialogue.q_i3)

q2 = classes.cutscene(classes.choice(
    classes.cutscene(q3,dialogue.q_2a),
    classes.cutscene(q3,dialogue.q_2b),
    dialogue.q_2,
    on_good=increment_bad
),dialogue.q_i2)

order = title(
    classes.cutscene(
        classes.choice(
            classes.cutscene(q2,dialogue.q_1a),
            classes.cutscene(q2,dialogue.q_1b),
            dialogue.q_1,
            on_bad=increment_bad
        ),dialogue.q_i
        )
        )

run(screen, 60, order) 
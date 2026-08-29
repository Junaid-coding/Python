import pygame
import random
pygame.init()
SPRITE_COLOUR = pygame.USEREVENT + 1
BG_COLOUR = pygame.USEREVENT + 2
bg_colours = [pygame.Color('blue'), pygame.Color('lightblue'), pygame.Color('darkblue')]
sprite_colours = [pygame.Color('yellow'), pygame.Color('magenta'), pygame.Color('orange'), pygame.Color('white')]
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(
            x=random.randint(0, 470),
            y=random.randint(0, 380)
        )
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        hit = (self.rect.left <= 0 or self.rect.right >= 500 or self.rect.top <= 0 or self.rect.bottom >= 400)
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] *= -1
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] *= -1
        if hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR))
            pygame.event.post(pygame.event.Event(BG_COLOUR))
    def change_color(self):
        self.image.fill(random.choice(sprite_colours))
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary sprite")
sprite = Sprite(pygame.Color('white'))
sprites = pygame.sprite.Group(sprite)
bg_color = bg_colours[0]
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOUR:
            sprite.change_color()
        elif event.type == BG_COLOUR:
            bg_color = random.choice(bg_colours)
    sprite.update()
    screen.fill(bg_color)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()
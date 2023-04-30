import pygame as pg
from random import randrange

# Assign name to 2-dimensional vectors
vec2 = pg.math.Vector2

class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)

    # WASD Movement of Snake
    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.direction = vec2(0, -self.size)

            if event.key == pg.K_s:
                self.direction = vec2(0, self.size)

            if event.key == pg.K_a:
                self.direction = vec2(-self.size, 0)

            if event.key == pg.K_d:
                self.direction = vec2(self.size, 0)

    # get random coordinates on grid to place snake
    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2

    def move(self):
        self.rect.move_ip(self.direction)

    def update(self):
        self.move()

    def draw(self):
        pg.draw.rect(self.game.screen, 'green', self.rect)

class Food:
    def __init__(self, game):
        pass

    def draw(self):
        pass
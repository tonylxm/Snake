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
        self.step_delay = 100   # Miliseconds
        self.time = 0
    
    # Fix time delay problem
    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    # Arrow Key Movement of Snake
    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.direction = vec2(0, -self.size)

            if event.key == pg.K_DOWN:
                self.direction = vec2(0, self.size)

            if event.key == pg.K_LEFT:
                self.direction = vec2(-self.size, 0)

            if event.key == pg.K_RIGHT:
                self.direction = vec2(self.size, 0)

    # get random coordinates on grid to place snake
    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2

    # Compare position of snake to position of food. If they are equal, the snake eats the food --> food goes to another random position
    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)

    def update(self):
        self.check_food()
        self.move()

    def draw(self):
        pg.draw.rect(self.game.screen, 'green', self.rect)

class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.game.snake.get_random_position()

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', self.rect)
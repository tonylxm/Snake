import pygame as pg
from game_objects import *
import sys

class Game:
    def __init__(self):
        pg.init
        self.WINDOW_SIZE = 700
        self.TILE_SIZE = 50
        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.new_game()

    def draw_grid(self):
        for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE):
            pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
        for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE):
            pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
        
    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pg.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill('black')
        self.draw_grid()
        self.snake.draw()
        self.food.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # Snake control
            self.snake.control(event)

    # Main game loop
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

# Run the game
if __name__ == '__main__':
    game = Game()
    game.run()
    
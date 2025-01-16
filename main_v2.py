from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
from alert import Alert

import time

class Game:
    def __init__(self):
        self.screen = Screen()
        self.is_on = None
        self.is_paused = False
        self.snake = None
        self.food = None
        self.scoreboard = None
        self.alert = None

    def start(self):
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.alert = Alert()
        self.is_on = True

        self.screen.update()
        self.screen.listen()

        self.screen.onkey(key="Up", fun=self.snake.move_up)
        self.screen.onkey(key="Down", fun=self.snake.move_down)
        self.screen.onkey(key="Left", fun=self.snake.move_left)
        self.screen.onkey(key="Right", fun=self.snake.move_right)
        self.screen.onkey(key="space", fun=self.pause)
        self.screen.onkey(key="Return", fun=self.restart)

        while self.is_on:
            self.play()

        self.screen.exitonclick()

    def restart(self):
        self.screen.clear()
        self.start()

    def pause(self):
        self.is_paused = not self.is_paused
        self.alert.show_pause(self.is_paused)

    def game_over(self):
        self.is_on = False
        self.alert.show_game_over()

    def play(self):
        self.screen.update()
        time.sleep(0.1)

        if not self.is_paused:
            self.snake.move()

            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.scoreboard.increase_score()
                self.snake.extend()

            if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
                self.game_over()

            for segment in self.snake.segments:
                if segment == self.snake.head:
                    pass
                elif self.snake.head.distance(segment) < 10:
                    self.game_over()


if __name__ == "__main__":
    game = Game()
    game.start()


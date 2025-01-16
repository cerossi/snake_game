from turtle import Turtle

ALIGNMENT="center"
FONT=('Courier', 16, 'normal')

class Alert(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,0)

    def show_game_over(self):
        self.show("GAME OVER", "red")
        self.show_restart()

    def show_start(self):
        self.goto(0, 0)
        self.show("PRESS ENTER TO START", "white")

    def show_restart(self):
        self.goto(0, -25)
        self.show("PRESS ENTER TO RESTART", "white")

    def show_pause(self, is_paused):
        if is_paused:
            self.show("PAUSED", "yellow")
        else:
            self.hide()

    def show(self, msg, color):
        self.color(color)
        self.write(msg, align=ALIGNMENT, font=FONT)

    def hide(self):
        self.clear()
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.highscore = 0
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def increase_points(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}",align=ALIGNMENT, font=FONT)
    # def game_over(self):
    #
    #     self.goto(0, 0)
    #     self.write("GAME OVER",align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
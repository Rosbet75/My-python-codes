from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True
screen.onkey(fun = snake.turn_left, key = "a")
screen.onkey(fun = snake.turn_right, key = "d")
while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_points()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()
# scoreboard.game_over()
scoreboard.reset()
screen.exitonclick()
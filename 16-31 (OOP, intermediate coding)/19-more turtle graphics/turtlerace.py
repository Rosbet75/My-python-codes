from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 600, height = 600)
user_color = screen.textinput("Make your bet", "Choose your turtle color: ")
turtle_list = []
coordinate_list = []
for x in range(5):
    turtle_list.append(Turtle())
    turtle_list[-1].shape("turtle")
    turtle_list[-1].penup()
    coordinate_list.append(-300)
    turtle_list[-1].goto(-300,-280 + (600/5 * x))
    if x == range(5)[-1]:
        turtle_list[-1].color(user_color)
for x in turtle_list:
    x.forward(random.randint(1,10))
reached = False
while not reached:
    for x in range(5):
        random_number = random.randint(1,10)
        coordinate_list[x] += random_number
        turtle_list[x].forward(random_number)
        if coordinate_list[x] >= 300:
            reached = True
            break

if not coordinate_list[-1] >= 300:
    print("you lose")

screen.exitonclick()
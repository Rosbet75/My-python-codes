import turtle
from unittest import skip

import pandas
screen = turtle.Screen()

screen.title("U.S. States Game")
screen.bgcolor("black")

image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)

def get_mouse_clirck_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_clirck_coor)


data = pandas.read_csv("50_states.csv")
count = 0
while count < len(data):
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name")

    if answer_state in data.state.to_list():
        x, y, state = data.loc[data["state"] == answer_state, ["x", "y", "state"]].values[0]

        cursor = turtle.Turtle()
        cursor.color("black")
        cursor.penup()
        cursor.hideturtle()
        cursor.goto(x, y)
        cursor.write(state)

    count += 1

turtle.mainloop()
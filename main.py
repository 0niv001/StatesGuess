import pandas
import turtle
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

graphic = turtle.Turtle()
graphic.penup()
graphic.hideturtle()
guessed = []


while len(guessed) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed)}/50", prompt="What's another state?").title()
    if answer_state == "Exit":
        missing = [state for state in all_states if state not in guessed]
        new_missing = pandas.DataFrame(missing)
        new_missing.to_csv("missing.csv")
        break
    if answer_state in all_states:
        guessed.append(answer_state)
        write = data[data.state == answer_state]
        graphic.goto(int(write.x), int(write.y))
        graphic.write(f"{answer_state}", font= FONT)


turtle.mainloop()
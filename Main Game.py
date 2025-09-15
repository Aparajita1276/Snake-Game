import turtle
import time
from Snake import Snake
from Food import Food

wn = turtle.Screen()
wn.title("Snake Game - Modular Version")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

snake = Snake()
food = Food()

score = 0
high_score = 0
delay = 100 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

def update_scoreboard():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}",
              align="center", font=("Courier", 24, "normal"))

def game_loop():
    global score, high_score, delay

    wn.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        if delay > 20:
            delay -= 1
        score += 10
        if score > high_score:
            high_score = score
        update_scoreboard()

    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        reset_game()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            reset_game()

    wn.ontimer(game_loop, delay)

def reset_game():
    global score, delay
    time.sleep(0.5)
    score = 0
    delay = 100
    update_scoreboard()
    snake.reset()

wn.listen()
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")

update_scoreboard()
game_loop()
wn.mainloop()
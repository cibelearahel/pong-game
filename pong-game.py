import turtle

screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("yellow")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("yellow")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

score_1 = 0
score_2 = 0

hud = turtle.Turtle()
hud.speed(0)
hud.color("blue")
hud.penup()
hud.hideturtle()
hud.goto(0, 255)
hud.write("1st Player - 0 x 0 - 2nd Player", align="center", font=("Courier", 24, "normal"))


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y -= 30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y -= 30
    else:
        y = -250
    paddle_2.sety(y)


def screen_endgame():
    hud.speed(0)
    hud.shape("square")
    hud.color("yellow")
    hud.penup()
    hud.hideturtle()


screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_1_up, "W")
screen.onkeypress(paddle_1_down, "S")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        hud.clear()
        hud.write("1st Player - {} x {} - 2nd Player".format(score_1, score_2),
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        hud.clear()
        hud.write("1st Player - {} x {} - 2nd Player".format(score_1, score_2),
                  align="center", font=("Courier", 24, "normal"))

    if (340 < ball.xcor() < 350) and (paddle_2.ycor() + 40 > ball.ycor()
                                      > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_1.ycor() + 40 > ball.ycor()
                                        > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score_1 == 10 or score_2 == 10:
        screen.reset()
        hud = turtle.Turtle()
        screen_endgame()
        hud.goto(0, 50)

        if score_1 == 10:
            hud.write("1st PLAYER VICTORY 🏆", align="center",
                      font=("Courier", 24, "normal"))
        else:
            hud.write("2nd PLAYER VICTORY 🏆", align="center",
                      font=("Courier", 24, "normal"))
        hud.goto(0, 10)
        hud.write("\nPress Esc to Exit", align="center",
                  font=("Courier", 20, "normal"))

        screen.onkeypress(screen.bye, "Escape")
        screen.listen()

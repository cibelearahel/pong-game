import turtle
import winsound

turtle.register_shape("sky.gif")
turtle.register_shape('bird_right_2.gif')
turtle.register_shape('bird_left_2.gif')
turtle.register_shape('pause.gif')

is_paused = True

screen = turtle.Screen()
screen.title('Pong Bird')
screen.setup(width=800, height=600)
screen.bgpic('sky.gif')
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

warning = turtle.Turtle()
warning.speed(0)
warning.color("#9C9C9C")
warning.penup()
warning.hideturtle()
warning.goto(0, -290)
warning.write("*press SPACE to pause/start game", align="center",
              font=("Courier", 18, "bold"))


bird = turtle.Turtle()
bird.speed(0)
bird.shape('bird_right_2.gif')
bird.penup()
bird.goto(0, 0)
bird.dx = 0.2
bird.dy = -0.2

score_1 = 0
score_2 = 0

hud = turtle.Turtle()
hud.speed(0)
hud.color("Yellow")
hud.penup()
hud.hideturtle()
hud.goto(0, 255)
hud.write("1st Player - 0 x 0 - 2nd Player", align="center", font=("Arial", 24, "bold"))

pause = turtle.Turtle()
pause.shape('pause.gif')
pause.penup()
pause.hideturtle()


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
    bird.hideturtle()
    pause.hideturtle()

    hud.speed(0)
    hud.shape("square")
    hud.color("yellow")
    hud.penup()
    hud.hideturtle()


def toggle_pause():
    global is_paused
    if is_paused is True:
        pause.hideturtle()
        is_paused = False
    else:
        pause.showturtle()
        is_paused = True


screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_1_up, "W")
screen.onkeypress(paddle_1_down, "S")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")
screen.onkeypress(toggle_pause, "space")


while True:
    if not is_paused:

        screen.update()
        bird.setx(bird.xcor() + bird.dx)
        bird.sety(bird.ycor() + bird.dy)

        if bird.ycor() > 290:
            bird.sety(290)
            bird.dy *= -1

        if bird.ycor() < -290:
            bird.sety(-290)
            bird.dy *= -1

        if bird.xcor() > 390:
            bird.goto(0, 0)
            bird.dx *= -1
            score_1 += 1
            winsound.PlaySound("bleep-sound.wav", winsound.SND_ASYNC)
            bird.shape('bird_left_2.gif')
            bird.penup()
            hud.clear()
            hud.write("1st Player - {} x {} - 2nd Player".format(score_1, score_2),
                      align="center", font=("Arial", 24, "bold"))

        if bird.xcor() < -390:
            bird.goto(0, 0)
            bird.dx *= -1
            score_2 += 1
            winsound.PlaySound("bleep-sound.wav", winsound.SND_ASYNC)
            bird.shape('bird_right_2.gif')
            bird.penup()
            hud.clear()
            hud.write("1st Player - {} x {} - 2nd Player".format(score_1, score_2),
                      align="center", font=("Arial", 24, "bold"))

        if (340 < bird.xcor() < 350) and (paddle_2.ycor() + 40 > bird.ycor()
                                          > paddle_2.ycor() - 40):
            bird.setx(340)
            bird.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            bird.shape('bird_left_2.gif')
            bird.penup()

        if (-340 > bird.xcor() > -350) and (paddle_1.ycor() + 40 > bird.ycor()
                                            > paddle_1.ycor() - 40):
            bird.setx(-340)
            bird.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            bird.shape('bird_right_2.gif')
            bird.penup()

        if score_1 == 10 or score_2 == 10:
            screen.reset()
            hud = turtle.Turtle()
            screen_endgame()
            hud.goto(0, 50)

            if score_1 == 10:
                hud.write("1st PLAYER VICTORY 🏆", align="center",
                          font=("Arial", 24, "bold"))
            else:
                hud.write("2nd PLAYER VICTORY 🏆", align="center",
                          font=("Arial", 24, "bold"))
            hud.goto(0, 10)
            hud.write("\nPress Esc to Exit", align="center",
                      font=("Arial", 24, "bold"))

            screen.onkeypress(screen.bye, "Escape")
            screen.listen()
    else:
        screen.update()

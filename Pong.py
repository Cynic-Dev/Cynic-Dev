import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Rine")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score Tracker
score_1 = 0
score_2 = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6
ball.dy = 0.6

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 25, "bold"))


# Paddle A Movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Paddle B Movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keybinds
paddle_a_up_key = input("Left Paddle Up Key: ")
paddle_a_down_key = input("Left Paddle Down Key: ")

paddle_b_up_key = input("Right Paddle Up Key: ")
paddle_b_down_key = input("Right Paddle Down Key: ")

wn.listen()
wn.onkeypress(paddle_a_up, paddle_a_up_key)
wn.onkeypress(paddle_a_down, paddle_a_down_key)
wn.onkeypress(paddle_b_up, paddle_b_up_key)
wn.onkeypress(paddle_b_down, paddle_b_down_key)

# Main Game Loop
while True:
    wn.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle Borders
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-240)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-240)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 25, "bold"))
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 25, "bold"))
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    # Paddle Collisions
    if ball.xcor() > 330 and ball.xcor() < 340 and (ball.ycor() < paddle_b.ycor() + 30 and ball.ycor() > paddle_b.ycor() - 30):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if ball.xcor() < -330 and ball.xcor() > -340 and (ball.ycor() < paddle_a.ycor() + 30 and ball.ycor() > paddle_a.ycor() - 30):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

        

        

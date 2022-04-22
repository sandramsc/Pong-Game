Designed & coded by Sandra Ashipala <https://github.com/sandramsc>
import turtle
import winsound

window = turtle.Screen()
window.title("Pong by @sandramsc")
window.bgcolor("black")
window.setup(width=850, height=620)
window.tracer(0)

###Scoring
#Score
score_a=0
score_b=0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=6, stretch_len=0.8)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=6, stretch_len=0.8)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed=(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#x is positive will move 2 diagonally
ball.dx = 1
#y is positive will move up 2
ball.dy = -1.5

###Scoring
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Roboto", 20, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard binding
#listens to keyboard inputs
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
#arrow keys
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")


#Main game loop
while True:
    window.update()

    #Move the ball
    ball.setx(ball.xcor() + (ball.dx / 4))
    ball.sety(ball.ycor() + (ball.dy / 4))

    #Border chacking
    if ball.ycor() > 300:
        #reverses the direction of the ball
        ball.sety(300)
        ball.dy *= -1
        #sound effect
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -300:
        #reverses the direction of the ball
        ball.sety(-300)
        ball.dy *= -1
        #ball comes back to center
    if ball.xcor() > 410:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a,score_b), align="center", font=("Roboto", 20, "normal"))

    if ball.xcor() < -410:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Roboto", 20, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        # sound effect
        winsound.PlaySound('paddlebounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        # sound effect
        winsound.PlaySound('paddlebounce.wav', winsound.SND_ASYNC)

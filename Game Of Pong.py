# Joconnells Game Of Pong
# Its a work in progress ok
# dont judge

import turtle

wn = turtle.Screen()
wn.title("Retarded Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Paddle L
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.penup()
paddle_l.goto(-350, 0)
paddle_l.shapesize(stretch_wid=5, stretch_len=1)

#Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.penup()
paddle_r.goto(350, 0)
paddle_r.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
#ball.shapesize(stretch_wid=1, stretch_len=1)
ball.dx = 0.1
ball.dy = 0.1

#Functions
def paddle_l_up():
    y=paddle_l.ycor()
    y = y+20
    paddle_l.sety(y)

def paddle_l_down():
    y=paddle_l.ycor()
    y = y-20
    paddle_l.sety(y)

def paddle_r_up():
    y=paddle_r.ycor()
    y = y+20
    paddle_r.sety(y)

def paddle_r_down():
    y=paddle_r.ycor()
    y = y-20
    paddle_r.sety(y)

def esc_shutdown():
    wn.bye()


#Keyboard Bindings

wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")
wn.onkeypress(esc_shutdown, "Escape")



# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1


    # Paddle Collision
 
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_r.ycor() +40 and ball.ycor() > paddle_r.ycor() -40:
        ball.setx(340)
        ball.dx = ball.dx * -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_l.ycor() +40 and ball.ycor() > paddle_l.ycor() -40:
        ball.setx(-340)
        ball.dx = ball.dx * -1

    if ball.xcor() > 341 and ball.xcor() < 360 and ball.ycor() < paddle_r.ycor() +50 and ball.ycor() > paddle_r.ycor():
        ball.sety(paddle_r.ycor() +50)
        ball.dy = ball.dy * -1

    if ball.xcor() > 341 and ball.xcor() < 360 and ball.ycor() > paddle_r.ycor() -50 and ball.ycor() < paddle_r.ycor():
        ball.sety(paddle_r.ycor() -50)
        ball.dy = ball.dy * -1

    if ball.xcor() < -341 and ball.xcor() > -360 and ball.ycor() > paddle_l.ycor() -50 and ball.ycor() < paddle_l.ycor():
        ball.sety(paddle_l.ycor() -50)
        ball.dy = ball.dy * -1

    if ball.xcor() < -341 and ball.xcor() > -360 and ball.ycor() < paddle_l.ycor() +50 and ball.ycor() > paddle_l.ycor():
        ball.sety(paddle_l.ycor() +50)
        ball.dy = ball.dy * -1



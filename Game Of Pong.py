# Joconnells Game Of Pong
# Its a work in progress ok
# dont judge
from playsound import playsound
import turtle
import winsound

wn = turtle.Screen()
wn.title("Retarded Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score

score_1 = 0
score_a = 0

# Constants

FPS = 30 # constant: refresh about 30 times per second
TIMER_VALUE = 1000//FPS # the timer value in milliseconds for timer events
music = "SFX/background.wav"  # music sound file
sfx = "SFX/pop.wav" # sfx location

# Variable

should_draw = True #to decide to draw  the turtle object, needed for fps control
xx = 0 # cordinates for ball position
yy = 0 # same as above

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
ball.penup()
ball.hideturtle()

xr = 3.0  #rate of position change for the ball
yr = 3.0  #rate of position change for the ball

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Retard 1: {}      Retard A: {}".format(score_1, score_a), align="center", font=("Courier", 18, "bold"))   # writes the score onto the screen

#Functions
def paddle_l_up():
    y=paddle_l.ycor()
    if y < 250:
        y = y+20
        paddle_l.sety(y)

def paddle_l_down():
    y=paddle_l.ycor()
    if y > -250:
        y = y-20
        paddle_l.sety(y)

def paddle_r_up():
    y=paddle_r.ycor()
    if y < 250:
        y = y+20
        paddle_r.sety(y)

def paddle_r_down():
    y=paddle_r.ycor()
    if y > -250:
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

# Main Game Physics for laggy Ball 
def move_ball():
    global score_1, score_a, should_draw, xx, yy, xr, yr # to bring in variables and or constants and edit them in a function box

    # Move the ball

    bxx = xx   # setting pre change parameter so can set should draw if changes
    byy = yy

    xx = xx + xr # changing position of the ball cor
    yy = yy + yr

    # Border Checking

    if yy > 290:
        yy = 290
        yr = yr * -1
        playsound(sfx, block=False)

    elif yy < -290:
        yy = -290
        yr = yr * -1
        playsound(sfx, block=False)

    if xx > 390:
        xx = 0
        yy = 0
        xr = xr * -1
        score_1 = score_1 + 1
        pen.clear()
        pen.write("Retard 1: {}      Retard A: {}".format(score_1, score_a), align="center", font=("Courier", 18, "bold"))

    elif xx < -390:
        xx = 0
        yy = 0
        xr = xr * -1 
        score_a = score_a +1
        pen.clear()
        pen.write("Retard 1: {}      Retard A: {}".format(score_1, score_a), align="center", font=("Courier", 18, "bold"))

    # Paddle Collision
     
    if xx > 340 and xx < 350 and yy < paddle_r.ycor() +40 and yy > paddle_r.ycor() -40:  #collision for side part of paddle
        xx = 340
        xr = xr * -1
        playsound(sfx, block=False)

    elif xx < -340 and xx > -350 and yy < paddle_l.ycor() +40 and yy > paddle_l.ycor() -40:  #collision for side part of paddle
        xx = -340
        xr = xr *-1
        playsound(sfx, block=False)

    elif xx > 341 and xx < 360 and yy < paddle_r.ycor() +50 and yy > paddle_r.ycor():    # collision for top of paddle
        yy = (paddle_r.ycor() +50)
        yr = yr * -1
        playsound(sfx, block=False)

    elif xx > 341 and xx < 360 and yy > paddle_r.ycor() -50 and yy < paddle_r.ycor():   # collision for bottom of paddle
        yy = (paddle_r.ycor() -50)
        yr = yr * -1
        playsound(sfx, block=False)

    elif xx < -341 and xx > -360 and yy > paddle_l.ycor() -50 and yy < paddle_l.ycor():   # collision for bottom of paddle
        yy = (paddle_l.ycor() -50)
        yr = yr * -1
        playsound(sfx, block=False)

    elif xx < -341 and xx > -360 and yy < paddle_l.ycor() +50 and yy > paddle_l.ycor():   # collision for top of paddle
        yy = (paddle_l.ycor() +50)
        yr = yr * -1
        playsound(sfx, block=False)
        #winsound.PlaySound("SFX/pop.wav", winsound.SND_ASYNC)

    if xx != bxx and yy != byy:  # to confirm changes to cordinates position to tell python to draw ball
        should_draw = True

    wn.ontimer(move_ball, TIMER_VALUE)


def draw_ball():    #draws ball
    global should_draw, ball
    if should_draw == False:
        return
    ball.clear()
    ball.shape("circle")
    ball.color("yellow")
    ball.goto(xx, yy)
    ball.showturtle()

    should_draw = False


wn.ontimer(move_ball, TIMER_VALUE)
#playsound(music, block=False)
winsound.PlaySound(music, winsound.SND_ASYNC + winsound.SND_LOOP)

while True:  # loops forever
    draw_ball()
    wn.update()

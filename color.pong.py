"""
Pong game

"""
import turtle
import winsound
import random
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]
ball_color = "white"

wn = turtle.Screen()
wn.title("Pong peli")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Baddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(ball_color)
ball.penup()
ball.goto(0, 0)


#Balls speed
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player 1: {score_a} Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))


#Function
#Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
    paddle_a.sety(y)

#Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
    paddle_b.sety(y)


#Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        new_bg_color = random.choice(colors)
        while (new_bg_color == ball_color or new_bg_color == paddle_a.color() or new_bg_color == paddle_b.color() or new_bg_color == wn.bgcolor()):
            new_bg_color = random.choice(colors)

        
        new_ball_color = random.choice(colors)
        while (new_ball_color == paddle_a.color() or new_ball_color == paddle_b.color() or new_ball_color == new_bg_color):
            new_ball_color = random.choice(colors)

       
        wn.bgcolor(new_bg_color)
        ball.color(new_ball_color)

            
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        
        new_bg_color = random.choice(colors)
        while (new_bg_color == ball_color or new_bg_color == paddle_a.color() or new_bg_color == paddle_b.color() or new_bg_color == wn.bgcolor()):
            new_bg_color = random.choice(colors)

        
        new_ball_color = random.choice(colors)
        while (new_ball_color == paddle_a.color() or new_ball_color == paddle_b.color() or new_ball_color == new_bg_color):
            new_ball_color = random.choice(colors)

       
        wn.bgcolor(new_bg_color)
        ball.color(new_ball_color)
   
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player 1: {score_a} Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))
        if score_a == 5:
            print("Player 1 won")
            break
        elif score_b == 5:
            print("Player 2 won")
            break


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player 1: {score_a} Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))
        if score_a == 5:
            print("Player 1 won")
            break
        elif score_b == 5:
            print("Player 2 won")
            break

        if ball.xcor() == 0 and ball.ycor() == 0:
            firstDirection = random.randint(0,3)
            if firstDirection == 1:
                ball.dx *= -1
                ball.dy *= 1
            elif firstDirection == 2:
                ball.dx *= 1
                ball.dy *= -1
            elif firstDirection == 3:
                ball.dx *= -1
                ball.dy *= -1


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        
        
        paddle_b.color(ball_color)
        ball_color = random.choice(colors)
        while new_ball_color == ball_color:
            ball_color = random.choice(colors)
        
        
        ball.color(ball_color)


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        
        paddle_a.color(ball_color)
        ball_color = random.choice(colors)
        while new_ball_color == ball_color:
            ball_color = random.choice(colors)
        
        
        ball.color(ball_color)

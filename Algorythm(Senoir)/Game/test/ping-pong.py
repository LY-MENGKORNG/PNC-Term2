
import turtle

window = turtle.Screen()
window.title("Ping Pong by Sal")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# Player-A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-380, 0)


# Player-B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(370, 0)


# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx=2              #D = Delta
ball.dy=-2

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard 
window.listen()
# paddle_a_keyboard
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
#paddle_b_keyboard
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")






# Main game
while True:
    window.update()

    #Ball move
    ball.sety(ball.ycor()+ ball.dy)
    ball.setx(ball.xcor()+ ball.dx)
    
    
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
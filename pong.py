import turtle

  # Creating window
wn = turtle.Screen()
  # Title to game
wn.title("Python Pong")
  # Color of background
wn.bgcolor("black")
  # Size of window
wn.setup(width=800, height=600)
  # Speeds up game
wn.tracer(0)

# PADDLE A - LEFT
paddle_a = turtle.Turtle()
  # Speed of animation-to the max possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
  # removes the default line while moving
paddle_a.penup()
paddle_a.goto(-350, 0)


# PADDLE B - RIGHT
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
  # d means delta or change
  # ball moves by 2px
ball.dx = 2
ball.dy = -2

# FUNCTIONS
def paddle_a_up():
  # returns y coordinate
  y = paddle_a.ycor()
  # moves paddle up 20px
  y += 20
  # resets the y coordinate
  paddle_a.sety(y)

def paddle_a_down():
  # returns y coordinate
  y = paddle_a.ycor()
  # moves paddle down 20px
  y -= 20
  # resets the y coordinate
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

# KEYBOARD BINDING
  # listen for keyboard input
wn.listen()
  # calls function when 'w' is pressed
wn.onkeypress(paddle_a_up, "w")
  # calls function when 's' is pressed
wn.onkeypress(paddle_a_down, "s")
  # calls function when the up arrow is pressed
wn.onkeypress(paddle_b_up, "Up")
  # calls function when down arrow is pressed
wn.onkeypress(paddle_b_down, "Down")


# MAIN GAME LOOP
while True:
  # Everytime loop runs it updates window
  wn.update()

  # MOVE THE BALL
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # BORDER CHECKING
  if ball.ycor() > 290:
    ball.sety(290)
    # reverse direction of the ball
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    # back to the center
    ball.goto(0, 0)
    ball.dx *= -1

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
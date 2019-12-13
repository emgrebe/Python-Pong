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

# Main game loop
while True:
  # Everytime loop runs it updates window
  wn.update()

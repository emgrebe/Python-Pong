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

# Main game loop
while True:
  # Everytime loop runs it updates window
  wn.update()

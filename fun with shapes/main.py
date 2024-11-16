import turtle

# Function to draw an equilateral triangle
def draw_triangle():
    for _ in range(3):
        turtle.forward(100)  # Move forward by 100 units
        turtle.left(120)     # Turn by 120 degrees to form a triangle

# Function to draw a rectangle
def draw_rectangle():
    for _ in range(2):
        turtle.forward(150)  # Move forward by 150 units (length of rectangle)
        turtle.left(90)      # Turn by 90 degrees
        turtle.forward(80)   # Move forward by 80 units (width of rectangle)
        turtle.left(90)      # Turn by 90 degrees again to close the rectangle

# Function to draw a hexagon
def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)  # Move forward by 100 units
        turtle.left(60)      # Turn by 60 degrees to form a hexagon

# Setup turtle window
turtle.setup(500, 500)  # Set the size of the turtle window
turtle.bgcolor("white")  # Set the background color of the window
turtle.title("Turtle Drawing Polygons")

# Draw Equilateral Triangle
turtle.penup()
turtle.goto(-200, 100)  # Move turtle to a starting position
turtle.pendown()
turtle.color("blue")
draw_triangle()

# Draw Rectangle
turtle.penup()
turtle.goto(50, 100)  # Move turtle to a different starting position
turtle.pendown()
turtle.color("green")
draw_rectangle()

# Draw Hexagon
turtle.penup()
turtle.goto(-200, -150)  # Move turtle to a different starting position
turtle.pendown()
turtle.color("red")
draw_hexagon()

# Finish drawing
turtle.done()

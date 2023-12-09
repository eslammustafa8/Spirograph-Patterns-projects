from tkinter import Tk, Entry, Button, Label, StringVar
import turtle
import math

def draw_triangle_spirograph(radius, small_radius, pen_colors, shape_params):
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(0)
    pen.width(2)

    angle = 0
    gcd = math.gcd(int(radius), int(small_radius))
    steps = int(360 / gcd)
    num_shapes = 36

    color_count = len(pen_colors)
    current_color = 0

    for _ in range(steps * num_shapes):
        pen.color(pen_colors[current_color])
        current_color = (current_color + 1) % color_count

        angle += (360 / (steps * num_shapes))
        side_length, corners = shape_params
        pen.penup()
        pen.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
        pen.pendown()
        for _ in range(corners):
            pen.forward(side_length)
            pen.left(120)

    turtle.done()

def draw_circle_spirograph(radius, small_radius, pen_colors, shape_params):
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(0)
    pen.width(2)

    angle = 0
    gcd = math.gcd(int(radius), int(small_radius))
    steps = int(360 / gcd)
    num_shapes = 36

    color_count = len(pen_colors)
    current_color = 0

    for _ in range(steps * num_shapes):
        pen.color(pen_colors[current_color])
        current_color = (current_color + 1) % color_count

        angle += (360 / (steps * num_shapes))
        inner_radius, outer_radius = shape_params
        pen.penup()
        pen.goto(inner_radius * math.cos(math.radians(angle)), inner_radius * math.sin(math.radians(angle)))
        pen.pendown()
        pen.circle(outer_radius, 360)

    turtle.done()

def draw_square_spirograph(radius, small_radius, pen_colors, shape_params):
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(0)
    pen.width(2)

    angle = 0
    gcd = math.gcd(int(radius), int(small_radius))
    steps = int(360 / gcd)
    num_shapes = 36

    color_count = len(pen_colors)
    current_color = 0

    for _ in range(steps * num_shapes):
        pen.color(pen_colors[current_color])
        current_color = (current_color + 1) % color_count

        angle += (360 / (steps * num_shapes))
        side_length = shape_params
        pen.penup()
        pen.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
        pen.pendown()
        for _ in range(4):
            pen.forward(side_length)
            pen.left(90)

    turtle.done()

def draw_spirograph_by_shape(shape):
    if shape == "triangle":
        side_length = float(input("Enter side length of the triangle: "))
        corners = 3
        shape_params = (side_length, corners)
        draw_triangle_spirograph(radius, small_radius, pen_colors, shape_params)
    elif shape == "circle":
        inner_radius = float(input("Enter inner radius for the circle: "))
        outer_radius = float(input("Enter outer radius for the circle: "))
        shape_params = (inner_radius, outer_radius)
        draw_circle_spirograph(radius, small_radius, pen_colors, shape_params)
    elif shape == "square":
        side_length = float(input("Enter side length of the square: "))
        shape_params = side_length
        draw_square_spirograph(radius, small_radius, pen_colors, shape_params)

radius = float(input("Enter radius of the Spirograph: "))
small_radius = float(input("Enter small radius of the Spirograph: "))
num_colors = int(input("Enter the number of colors: "))
pen_colors = []

for i in range(num_colors):
    color_option = input(f"Enter color {i + 1} (name, RGB values, or hexadecimal code): ")
    pen_colors.append(color_option)

shape = input("Enter shape for Spirograph (triangle, circle, square): ")
draw_spirograph_by_shape(shape)



# Function to draw star-shaped spirograph
def draw_star_spirograph():
    side_length = float(entry_star.get())
    corners = 5
    draw_triangle_spirograph(radius, small_radius, pen_colors, (side_length, corners))

# Function to draw square-shaped spirograph
def draw_square_spirograph():
    side_length = float(entry_square.get())
    draw_square_spirograph(radius, small_radius, pen_colors, side_length)

# Function to draw triangle-shaped spirograph
def draw_triangle_spirograph():
    inner_radius = float(entry_triangle_inner.get())
    outer_radius = float(entry_triangle_outer.get())
    draw_circle_spirograph(radius, small_radius, pen_colors, (inner_radius, outer_radius))

radius = 100
small_radius = 30
num_colors = 5  # Example number of colors
pen_colors = ["red", "green", "blue", "yellow", "purple"]

myview = Tk()
myview.geometry("800x500")

# Entry for star-shaped spirograph
label_star = Label(myview, text="Enter side length for star:")
entry_star = Entry(myview)
label_star.pack(pady=5)
entry_star.pack(pady=5)

# Button to draw star-shaped spirograph
button_star = Button(myview, text="Draw Star Spirograph", bg="red", fg="black", command=draw_star_spirograph)
button_star.pack(pady=10)

# Entry for square-shaped spirograph
label_square = Label(myview, text="Enter side length for square:")
entry_square = Entry(myview)
label_square.pack(pady=5)
entry_square.pack(pady=5)

# Button to draw square-shaped spirograph
button_square = Button(myview, text="Draw Square Spirograph", bg="yellow", fg="black", command=draw_square_spirograph)
button_square.pack(pady=10)

# Entry for triangle-shaped spirograph
label_triangle_inner = Label(myview, text="Enter inner radius for triangle:")
entry_triangle_inner = Entry(myview)
label_triangle_inner.pack(pady=5)
entry_triangle_inner.pack(pady=5)

label_triangle_outer = Label(myview, text="Enter outer radius for triangle:")
entry_triangle_outer = Entry(myview)
label_triangle_outer.pack(pady=5)
entry_triangle_outer.pack(pady=5)

# Button to draw triangle-shaped spirograph
button_triangle = Button(myview, text="Draw Triangle Spirograph", bg="blue", fg="black", command=draw_triangle_spirograph)
button_triangle.pack(pady=10)

myview.mainloop()

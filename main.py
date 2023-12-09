import turtle
import math
import tkinter as tk

# Function to draw a Spirograph pattern based on the selected shape and colors
def draw_spirograph(radius, small_radius, colors, shape, side_length, inner_radius, outer_radius):
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Spirograph Pattern")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(0)
    pen.width(2)

    angle = 0
    gcd = math.gcd(int(radius), int(small_radius))
    steps = int(360 / gcd)
    num_shapes = 36

    color_count = len(colors)
    current_color = 0

    for _ in range(steps * num_shapes):
        pen.color(colors[current_color])
        current_color = (current_color + 1) % color_count

        pen.penup()
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        pen.goto(x, y)
        pen.pendown()
        
        if shape == "triangle":
            for _ in range(3):
                pen.forward(side_length)
                pen.left(120)
        elif shape == "circle":
            pen.circle(outer_radius)
        elif shape == "square":
            for _ in range(4):
                pen.forward(side_length)
                pen.left(90)

        angle += 360 / (steps * num_shapes)

    pen.hideturtle()
    window.mainloop()

# Function to update the GUI when the number of colors is changed
def on_color_count_change(*args):
    for widget in color_frame.winfo_children():
        widget.destroy()

    try:
        for i in range(color_count.get()):
            tk.Label(color_frame, text=f"Color {i + 1}:", bg='black', fg='white').pack()
            color_input = tk.Entry(color_frame, bg='sky blue', fg='black', textvariable=colors_vars[i])
            color_input.pack()
    except tk.TclError:
        pass

# Function to gather input and initiate drawing
def on_submit():
    colors = [var.get() for var in colors_vars[:color_count.get()]]
    draw_spirograph(radius_var.get(), small_radius_var.get(), colors, shape_var.get(),
                    side_length_var.get(), inner_radius_var.get(), outer_radius_var.get())
    root.quit()

# Main Tkinter window configuration
root = tk.Tk()
root.title("Spirograph Parameters")
root.config(bg='black')
root.geometry("400x600")

# Variable definitions
shape_var = tk.StringVar(value="triangle")
radius_var = tk.DoubleVar(value=150)
small_radius_var = tk.DoubleVar(value=50)
color_count = tk.IntVar(value=2)
colors_vars = [tk.StringVar(value="black") for _ in range(10)]
side_length_var = tk.DoubleVar(value=100)
inner_radius_var = tk.DoubleVar(value=50)
outer_radius_var = tk.DoubleVar(value=50)

# Number of Colors input
tk.Label(root, text="Number of Colors:", bg='black', fg='white').pack()
color_count_entry = tk.Entry(root, bg='sky blue', fg='black', textvariable=color_count)
color_count_entry.pack()
color_count.trace('w', on_color_count_change)

# Color input frame setup
color_frame = tk.Frame(root, bg='black')
color_frame.pack()

# Shape selection dropdown
tk.Label(root, text="Shape:", bg='black', fg='white').pack()
shape_menu = tk.OptionMenu(root, shape_var, "triangle", "circle", "square")
shape_menu.config(bg='blue', fg='white', activebackground='light blue')
shape_menu["menu"].config(bg='black', fg='white')
shape_menu.pack()

# Radius input field
tk.Label(root, text="Radius:", bg='black', fg='white').pack()
radius_entry = tk.Entry(root, bg='sky blue', fg='black', textvariable=radius_var)
radius_entry.pack()

# Small Radius input field
tk.Label(root, text="Small Radius:", bg='black', fg='white').pack()
small_radius_entry = tk.Entry(root, bg='sky blue', fg='black', textvariable=small_radius_var)
small_radius_entry.pack()

# Side Length input field
tk.Label(root, text="Side Length (for triangle and square):", bg='black', fg='white').pack()
side_length_entry = tk.Entry(root, bg='sky blue', fg='black', textvariable=side_length_var)
side_length_entry.pack()

# Inner Radius input field
tk.Label(root, text="Inner Radius (for circle):", bg='black', fg='white').pack()
inner_radius_entry = tk.Entry(root, bg='sky blue', fg='black', textvariable=inner_radius_var)
inner_radius_entry.pack()

# Outer Radius input field
tk.Label(root, text="Outer Radius (for circle):", bg='black', fg='white').pack()
outer_radius_entry = tk.Entry(root, bg='sky blue', fg='black', textvariable=outer_radius_var)
outer_radius_entry.pack()

# Initial color fields setup
on_color_count_change()

# Draw button
submit_button = tk.Button(root, text="Draw Spirograph", command=on_submit, bg='blue', fg='white')
submit_button.pack()

# Start the Tkinter event loop
root.mainloop()
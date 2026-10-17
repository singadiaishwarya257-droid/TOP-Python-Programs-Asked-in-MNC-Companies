import turtle
import math
import colorsys

# Create the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🦋 Neon Butterfly Animation")
screen.setup(width=800, height=700)
screen.tracer(0)

# Create the drawing turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Draw a butterfly using a mathematical curve
def draw_butterfly(phase):
    t.clear()

    # Draw colorful wings
    for i in range(1800):
        angle = i * 0.025

        # Butterfly curve
        r = math.exp(math.cos(angle)) - 2 * math.cos(4 * angle)
        r = r * 35

        # Animate wing movement
        x = r * math.sin(angle + phase)
        y = r * math.cos(angle)

        # Rainbow neon colors
        hue = (i / 1800 + phase / 10) % 1
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)

        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(3, rgb)

    # Draw the butterfly's body
    t.penup()
    t.goto(0, -65)
    t.setheading(90)
    t.pensize(8)
    t.pencolor("white")
    t.pendown()
    t.forward(130)
    t.penup()

    # Draw antennae
    t.pensize(3)
    t.pencolor("cyan")

    for direction in [35, 145]:
        t.goto(0, 60)
        t.setheading(direction)
        t.pendown()
        t.circle(35, 60)
        t.penup()

# Animate the butterfly
phase = 0

def animate():
    global phase

    draw_butterfly(phase)
    screen.update()

    phase += 0.12
    screen.ontimer(animate, 50)

animate()
screen.mainloop()
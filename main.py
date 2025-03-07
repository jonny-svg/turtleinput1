import turtle

def draw_ring(x, y, color):
    turtle.penup()
    turtle.goto(x, y - 35)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.circle(35)

turtle.speed(0)
turtle.bgcolor("#F5DEB3")  # Light brown background
turtle.penup()
turtle.goto(-100, 80)
turtle.pencolor("black")
turtle.write("Winter Olympics 2026", font=("Arial", 16, "bold"))
turtle.pendown()

colors = ['blue', 'black', 'red', 'yellow', 'green']
positions = [(-80, 15), (0, 15), (80, 15), (-40, -20), (40, -20)]

for (x, y), color in zip(positions, colors):
    draw_ring(x, y, color)

turtle.done()

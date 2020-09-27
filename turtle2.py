from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
#screen.colormode(255)

R = 255
G = 0
B = 0

screen.bgcolor((0, 0, 255))

turtle.speed(0)

colours = []

while G <= 255:
    colours.append((R, G, B))
    G += 1

while R >= 0:
    colours.append((R, G, B))
    R -= 1

while B < 255:
    colours.append((R, G, B))
    B += 1

while G > 0:
    colours.append((R, G, B))
    G -= 1

while R < 255:
    colours.append((R, G, B))
    R += 1
  

for i in range(3000):
  # The line below keeps changing the colour, even if i
  # is bigger than the list of colours
  turtle.color(colours[i % len(colours)])
  turtle.forward(i/3)
  turtle.right(119)

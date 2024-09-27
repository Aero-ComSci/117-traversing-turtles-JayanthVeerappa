from code import Tortle

#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

startx = 0
starty = 0
direction = 90

turtle = Tortle(turtle_shapes, turtle_colors, my_turtles, startx, starty, direction)
turtle.setShapeColor()
turtle.move_turtle()
#

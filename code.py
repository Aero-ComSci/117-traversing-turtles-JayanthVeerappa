#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors

class tortle():
    def __init__(self, shapes, colors, direction, startx , starty ):
        self.shape = shapes
        self.colors = colors
        self.direction = direction
        self.startx = startx
        self.starty = starty
        
    def attribute(self):
        for s in turtle_shapes:
            t = trtl.Turtle(shape=s)
            my_turtles.append(t)
            new_color = self.color.pop()
            t.color(new_color)
            t.penup()








for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)
    new_color = turtle_colors.pop()
    t.color(new_color)
    t.penup()







#setting intital position
startx = 0
starty = 0

#

direction = 90
for t in my_turtles:
    t.goto(startx, starty)
    t.pendown()
    t.setheading(direction)
    t.right(45)     
    t.forward(50)
    direction = t.heading()



#	
startx = t.xcor()
starty = t.ycor()
 
wn = trtl.Screen()
wn.mainloop()

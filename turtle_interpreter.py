'''
Interpretes strings from txt files into turtle commands
'''

import turtle


class TurtleInterpreter:
    def __init__(self,dx = 800, dy =800):
        turtle.setup(dx,dy)
        turtle.tracer(False)


    def drawString(self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list   
        of turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position
        < : save current color of the turtle
        g : sets turtle's color to green
        r : sets turtle's color to red
        y : sets turtle's color to yellow
        """
        stack = []
        colorstack = []

# base XY
# rule X F[@[-X]+X]



        for char in dstring:
            if char == 'F' or char == 'X':
                turtle.forward(distance)
            elif char == '-':
                turtle.right(angle)
            elif char == '+':
                turtle.left(angle)
            elif char == '[':
                stack.append(turtle.position())
                stack.append(turtle.heading())
            elif char == ']':
                turtle.penup()
                turtle.setheading(stack.pop())
                turtle.goto(stack.pop())
                turtle.pendown()                
            elif char == '<':
                colorstack.append(turtle.color()[0])
            elif char == '>':
                turtle.color(colorstack.pop())
            elif char == 'g':
                turtle.color((0.15, 0.5, 0.2))
            elif char == 'y':
                turtle.color((0.8, 0.8, 0.3))
            elif char == 'r':
                turtle.color((0.7, 0.2, 0.3))
            elif char == 'B':
                turtle.color((0.58, 0.29, 0))
                turtle.begin_fill()
                turtle.circle(5,180)
                turtle.end_fill()
                turtle.color((0.15, 0.5, 0.2))
            elif char == 'L':
                turtle.color((0.15, 0.5, 0.2))
                turtle.begin_fill()
                turtle.circle(5,180)
                turtle.end_fill()
        turtle.update()


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' 
        key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()
        turtle.update()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a click
        turtle.exitonclick()


    def place(self, xpos, ypos, angle = None):

        turtle.penup()
        turtle.goto(xpos, ypos)
        if angle != None:
            turtle.setheading(angle)
        turtle.pendown()

    
    def orient(self, angle):
        turtle.setheading(angle)

    def goto(self, xpos, ypos):

        turtle.up()
        turtle.goto(xpos, ypos)
        turtle.down()

    def setColor(self, c):
        turtle.color(c)

    def setWidth(self, w):
        turtle.width
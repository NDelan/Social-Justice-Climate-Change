'''
Draws a system of lsystem plants.
The change in color of the leaves 
represent how adverse climate conditions
affect plant growth.
'''

import turtle
import turtle_interpreter
import lsystem
import random


def main():
    '''
    Draws a spiral of Lsystem file passed as command line argument
    '''
    # s = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    # stores turtle positions
    turtle_positions = []                     
    t.speed(0)

    # stores positions of 120 turtle movements
    x_start = -390           #initial x position
    y_start = 200            #initial y position
    
    # stores what the Lsystem class returns
    tree = []

    # Screen size
    sx = 800
    sy = 450
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    N = len(turtle_positions)

    # for i in range(N):
    tree.append(lsystem.Lsystem('file1.txt'))
    tree.append(lsystem.Lsystem('file2.txt'))
    tree.append(lsystem.Lsystem('file3.txt'))


    while y_start > -250:
        for i in range( 30 ):

            # performs 4 iterations of Lsystem structure
            tstr = tree[i//10].buildString(4)

            terp.setColor( (0, 0.4, 0.005*i ) )
            terp.place( x_start, y_start, random.randint( 85, 95 ) )
            terp.drawString(tstr, random.randint( 2, 4 ) , random.randint( 18, 30 ) * random.choice( [1, -1] ) )
            x_start += 20
        y_start -= 50
        x_start -= 20*30
        # quits the screen when 'q' is pressed or a point on the screen is clicked
    # terp.hold()


if __name__ == "__main__":
    main()



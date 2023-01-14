'''
Display Graph of dataset on screen
'''

import turtle

t = turtle.Screen()
def run():
    image = "dataset.GIF"
    screen = turtle.Screen()

    screen.addshape(image)
    turtle.shape(image)

 
if __name__ == '__main__':
    run()



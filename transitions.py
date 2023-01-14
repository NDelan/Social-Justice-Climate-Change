'''
Displays tkinter messagebox to allow user interactions.
'''

import turtle
import tkinter.messagebox
import firstScene
import lsystem_scene
import realism

'''imports tkinter to implement message box for user input'''
# --- functions ---


def stop(callback):
    '''this uses a message box for user input'''
    answer = tkinter.messagebox.askyesno('More?', "Show more images?")
    print('answer:', answer)

    if answer:
        callback()
    else:
        turtle.exitonclick()


def stop(callback):
    '''this uses a message box for user input'''
    answer = tkinter.messagebox.askyesno('More?', "Would You Like to learn about the effects of the increase of earth surface temperature on vegetation?")
    print('answer:', answer)

    if answer:
        callback()
    else:
        turtle.exitonclick()


def stop2(callback):
    '''this uses a message box for user input'''
    answer = tkinter.messagebox.askyesno('More?', "Would you like to learn about a major cause of the increase of earth surface temperature on vegetation?")
    print('answer:', answer)

    if answer:
        callback()
    else:
        turtle.exitonclick()
        

def first(x=0, y=0):

    firstScene.run()

    # assign function to click on screen
    #lambda is an abstract built-in function that computes the value of
    #the expression (stop(second))
    turtle.onscreenclick(lambda x,y:stop(second))


def second(x=0, y=0):
    # clear screen
    turtle.clearscreen()
    turtle.reset()

    lsystem_scene.main()                        #Calls the third Image

    turtle.onscreenclick(lambda x,y:stop2(third))


def third(x=0, y=0):
    # clear screen
    turtle.clearscreen()
    turtle.reset()

    realism.main()                     #Call Third Scene

    # end program on click
    turtle.exitonclick()


# --- main ---

if __name__ == "__main__":
    first()
    turtle.mainloop()
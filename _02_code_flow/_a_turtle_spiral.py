import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # Make a new turtle
    turtle_1=turtle.Turtle()
    # This code sets our shape to a turtle
    turtle_1.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    turtle_1.speed(10)
    # Set your turtle's color using .color('green')
    turtle_1.color('green')
    # Use a loop to repeat a the code below 50 times

    for i in range(100):
        turtle_1.forward(5*i)
        turtle_1.right(360/7)
        turtle.turtlesize(5, 5, 10)
        turtle_1.pencolor(get_random_color())
        turtle_1.width(i)




    # Set the turtle color to a random color

    turtle_1.color('green')

        # Move the turtle (5*i) pixels. 'i' is the loop variable

        # Turn the turtle (360/7) degrees to the right

        # Change the turtle width to 'i' (the loop variable)

        # Check the pattern against the picture in the recipe. If it matches, you are donepass
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()

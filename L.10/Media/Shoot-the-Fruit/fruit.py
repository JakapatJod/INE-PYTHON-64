# Game Shoot the fruit.
import pgzrun

# define size of the windowns
WIDTH = 640
HEIGHT = 480

# create object
apple = Actor('apple')

# function for display
def draw():
    screen.clear()
    apple.draw()

pgzrun.go()
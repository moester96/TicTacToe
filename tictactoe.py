import turtle
import math
import tkinter


class TicTacToe:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()

    def drawBoard(self):
        self.screen.title("TicTacToe")
        self.turtle.pensize(10)
        self.turtle.hideturtle()
        self.screen.tracer(0)

        self.turtle.penup()
        # Center the outside box being drawn
        self.turtle.goto(-300, -300)
        self.turtle.pendown()

        # Draws the outside box
        for i in range(4):
            self.turtle.forward(600)
            self.turtle.left(90)

        self.turtle.penup()
        # Moves turtle back to the origin of (0, 0)
        self.turtle.home()

        # Draws the vertical lines
        self.turtle.left(90)
        self.turtle.goto(-100, -300)
        self.turtle.pendown()
        self.turtle.forward(600)

        self.turtle.penup()
        self.turtle.home()

        self.turtle.left(90)
        self.turtle.goto(100, -300)
        self.turtle.pendown()
        self.turtle.forward(600)

        self.turtle.penup()
        self.turtle.home()

        # Draws the horizontal lines
        self.turtle.goto(-300, 100)
        self.turtle.pendown()
        self.turtle.forward(600)

        self.turtle.penup()
        self.turtle.home()

        self.turtle.goto(-300, -100)
        self.turtle.pendown()
        self.turtle.forward(600)

        self.screen.update()
        tkinter.mainloop()

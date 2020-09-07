import turtle
import tkinter


class TicTacToe:
    square_mid_points = {'0': (-200, 200), '1': (0, 200), '2': (200, 200),
                         '3': (-200, 0), '4': (0, 0), '5': (200, 0),
                         '6': (-200, -200), '7': (0, -200), '8': (200, -200)}

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.square = 0

    def getMouseClick(self, x, y):
        column = (x + 300) // 200
        row = (-y + 300) // 200
        square = column + row*3
        square = int(square)
        self.square = square

    def drawX(self):
        square = str(self.square)
        mid_point = TicTacToe.square_mid_points.get(square)

        self.turtle.penup()
        self.turtle.goto(mid_point)

    def drawO(self):
        square = str(self.square)
        mid_point = TicTacToe.square_mid_points.get(square)

        self.turtle.penup()
        self.turtle.goto(mid_point[0], mid_point[1] - 80)
        self.turtle.pendown()
        self.turtle.circle(80)

    def drawBoard(self):
        self.screen.title("TicTacToe")
        self.screen.setup(660, 640)
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

        # Listens for left mouse button click
        self.screen.onscreenclick(self.getMouseClick)

        self.screen.update()
        tkinter.mainloop()

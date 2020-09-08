import turtle
import tkinter


class TicTacToe:
    square_mid_points = {'0': (-200, 200), '1': (0, 200), '2': (200, 200),
                         '3': (-200, 0), '4': (0, 0), '5': (200, 0),
                         '6': (-200, -200), '7': (0, -200), '8': (200, -200)}

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.board = [['' for i in range(3)] for j in range(3)]
        self.next_turn = ''
        self.num_turns = 0
        self.square = 0
        self.isWinner = False

    def chooseLetter(self):
        letter = input('Please select your letter of choice: X or O\n')
        self.next_turn = letter.lower()

    def drawX(self):
        square = str(self.square)
        mid_point = TicTacToe.square_mid_points.get(square)

        self.turtle.penup()
        self.turtle.goto(mid_point)
        self.turtle.pendown()
        self.turtle.setheading(135)

        for i in range(2):
            self.turtle.forward(90)
            self.turtle.backward(180)
            self.turtle.goto(mid_point)
            self.turtle.left(270)

        self.turtle.penup()
        self.turtle.home()

    def drawO(self):
        square = str(self.square)
        mid_point = TicTacToe.square_mid_points.get(square)

        self.turtle.penup()
        self.turtle.goto(mid_point[0], mid_point[1] - 80)
        self.turtle.pendown()
        self.turtle.circle(80)

        self.turtle.penup()

    def checkWinner(self):
        first_diagonal = []
        second_diagonal = []

        # Checks rows
        for i in range(3):
            if set(self.board[i]) == 1:
                print('Winner')
                return True

        # Checks columns
        for i in range(3):
            if set(self.board[0][i]) == 1:
                print('Winner')
                return True

        # Checks first diagonal
        for i in range(3):
            first_diagonal.append(self.board[i][i])

        if set(first_diagonal) == 1:
            print('Winner')
            return True
        else:
            first_diagonal = []

        # Checks second diagonal
        for i in range(3):
            if i != 1:
                second_diagonal.append(self.board[i][2])
            else:
                second_diagonal.append(self.board[i][i])

        if set(second_diagonal) == 1:
            print('Winner')
            return True
        else:
            first_diagonal = []

        print('No winner')
        return False

    def checkDraw(self):
        if self.checkWinner() == False:
            print('Draw')

    def getMouseClick(self, x, y):
        column = (x + 300) // 200
        row = (-y + 300) // 200
        square = column + row*3
        self.square = int(square)

        if self.board[self.square] == '' and self.next_turn == 'x':
            self.drawX()
            self.board[self.square] = self.next_turn
            self.next_turn = 'o'
            self.num_turns += 1
            if self.num_turns >= 5:
                self.isWinner = self.checkWinner()

        elif self.board[self.square] == '' and self.next_turn == 'o':
            self.drawO()
            self.board[self.square] = self.next_turn
            self.next_turn = 'x'
            self.num_turns += 1
            if self.num_turns >= 5:
                self.isWinner = self.checkWinner()

        if self.num_turns == 9:
            self.checkDraw()

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

import turtle
import tkinter
import sys


class TicTacToe:
    square_mid_points = {'0': (-200, 200), '1': (0, 200), '2': (200, 200),
                         '3': (-200, 0), '4': (0, 0), '5': (200, 0),
                         '6': (-200, -200), '7': (0, -200), '8': (200, -200)}

    square_coordinates = {'0': (0, 0), '1': (0, 1), '2': (0, 2),
                          '3': (1, 0), '4': (1, 1), '5': (1, 2),
                          '6': (2, 0), '7': (2, 1), '8': (2, 2)}

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.board = [['' for i in range(3)] for j in range(3)]
        self.next_turn = ''
        self.num_turns = 0
        self.square = 0
        self.row = 0
        self.col = 0

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
        square = self.square
        mid_point = TicTacToe.square_mid_points.get(square)

        self.turtle.penup()
        self.turtle.goto(mid_point[0], mid_point[1] - 80)
        self.turtle.pendown()
        self.turtle.circle(80)

        self.turtle.penup()

    def checkWinner(self):
        column = []
        first_diagonal = []
        second_diagonal = []

        # Checks rows
        for i in range(3):
            if len(set(self.board[i])) == 1 and self.board[i].count('') == 0:
                return True

        # Checks columns
        for i in range(3):
            column = [col[i] for col in self.board]
            if len(set(column)) == 1 and column.count('') == 0:
                return True

        # Checks first diagonal
        for i in range(3):
            first_diagonal.append(self.board[i][i])

        if len(set(first_diagonal)) == 1 and first_diagonal.count('') == 0:
            return True
        else:
            first_diagonal = []

        # Checks second diagonal
        for i in range(3):
            if i == 0:
                second_diagonal.append(self.board[i][2])
            elif i == 1:
                second_diagonal.append(self.board[i][i])
            else:
                second_diagonal.append(self.board[i][0])

        if len(set(second_diagonal)) == 1 and second_diagonal.count('') == 0:
            return True
        else:
            second_diagonal = []

        return False

    def checkDraw(self):
        if self.checkWinner() == False:
            self.turtle.home()
            self.turtle.goto(-80, 325)
            self.turtle.write('Draw', font=('Arial', 50, 'normal'))

    def getMouseClick(self, x, y):
        column = (x + 300) // 200
        row = (-y + 300) // 200
        self.square = str(int(column + row*3))
        self.row, self.col = TicTacToe.square_coordinates.get(self.square)

        if self.board[self.row][self.col] == '' and self.next_turn == 'x':
            self.drawX()
            self.board[self.row][self.col] = self.next_turn
            self.next_turn = 'o'
            self.num_turns += 1
            if self.num_turns >= 5:
                if self.checkWinner():
                    self.turtle.home()
                    self.turtle.goto(-100, 325)
                    self.turtle.write('Winner', font=('Arial', 50, 'normal'))
                    self.screen._onscreenclick(None)
                    self.playAgain()

        elif self.board[self.row][self.col] == '' and self.next_turn == 'o':
            self.drawO()
            self.board[self.row][self.col] = self.next_turn
            self.next_turn = 'x'
            self.num_turns += 1
            if self.num_turns >= 5:
                if self.checkWinner():
                    self.turtle.home()
                    self.turtle.goto(-100, 325)
                    self.turtle.write('Winner', font=('Arial', 50, 'normal'))
                    self.screen._onscreenclick(None)
                    self.playAgain()

        if self.num_turns == 9:
            self.checkDraw()
            self.screen._onscreenclick(None)
            self.playAgain()

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

    def playAgain(self):
        replay = input('Play Again? y/n\n')
        replay = replay.lower()
        if replay == 'y':
            self.screen.clearscreen()
            self.board = [['' for i in range(3)] for j in range(3)]
            self.num_turns = 0
            self.chooseLetter()
            self.drawBoard()
        else:
            sys.exit()

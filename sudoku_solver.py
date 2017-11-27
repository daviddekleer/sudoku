from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys

import sudoku_ui


class ExampleApp(QtGui.QMainWindow, sudoku_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # initialize the 9x9 sudoku grid
        self.s = [
            [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8, self.cell9],
            [self.cell10, self.cell11, self.cell12, self.cell13, self.cell14, self.cell15, self.cell16, self.cell17, self.cell18],
            [self.cell19, self.cell20, self.cell21, self.cell22, self.cell23, self.cell24, self.cell25, self.cell26, self.cell27],
            [self.cell28, self.cell29, self.cell30, self.cell31, self.cell32, self.cell33, self.cell34, self.cell35, self.cell36],
            [self.cell37, self.cell38, self.cell39, self.cell40, self.cell41, self.cell42, self.cell43, self.cell44, self.cell45],
            [self.cell46, self.cell47, self.cell48, self.cell49, self.cell50, self.cell51, self.cell52, self.cell53, self.cell54],
            [self.cell55, self.cell56, self.cell57, self.cell58, self.cell59, self.cell60, self.cell61, self.cell62, self.cell63],
            [self.cell64, self.cell65, self.cell66, self.cell67, self.cell68, self.cell69, self.cell70, self.cell71, self.cell72],
            [self.cell73, self.cell74, self.cell75, self.cell76, self.cell77, self.cell78, self.cell79, self.cell80, self.cell81]
        ]
        self.pushButton.clicked.connect(self.reset)    # reset button
        self.pushButton_2.clicked.connect(self.solve)  # solve button
        for i in range(9):
            for j in range(9):
                self.s[i][j].textChanged.connect(self.cell_input)

    def cell_input(self, text):
        if text:
            self.sender().setStyleSheet("QLineEdit { background-color: #ddd; }")
        else:
            self.sender().setStyleSheet("QLineEdit { background-color: #fff; }")

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.s[i][j].setText('')
                self.s[i][j].setStyleSheet("QLineEdit { background-color: #fff; }")

    def to_int(self, cell):
        num = cell.text()
        if not num:
            return None
        return int(cell.text())

    def next_pos(self, pos=[0, 0]):
        if pos == (8, 8):  # solved
            return True

        x = pos[0]
        y = pos[1]
        while self.to_int(self.s[y][x]):  # as long as there are predefined numbers
            if x == 8 and y == 8:         # stop if it's the last number
                break
            if x == 8:  # next row
                y += 1
                x = 0
            else:  # next column
                x += 1

        return (x, y)

    def allowed_numbers_for_pos(self, pos):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = pos[0]
        y = pos[1]

        # find left top postion of square
        x_square_start = (x // 3) * 3
        y_square_start = (y // 3) * 3
        # remove already filled in nrs from numbers
        for ys in range(y_square_start, y_square_start + 3):
            for xs in range(x_square_start, x_square_start + 3):
                number = self.to_int(self.s[ys][xs])
                if number in numbers:
                    numbers.remove(number)

        # check column
        for ys in range(9):
            number = self.to_int(self.s[ys][x])
            if number in numbers:
                numbers.remove(number)

        # check row
        for xs in range(9):
            number = self.to_int(self.s[y][xs])
            if number in numbers:
                numbers.remove(number)

        return numbers

    def solve(self, pos=None):
        if pos is True:  # solved
            return True

        if not pos:  # initialize pos
            pos = self.next_pos()

        x = pos[0]
        y = pos[1]
        allowed_numbers = self.allowed_numbers_for_pos(pos)
        for number in allowed_numbers:
            # try the allowed numbers and continue with next pos
            self.s[y][x].setText(str(number))
            self.s[y][x].setStyleSheet("QLineEdit { background-color: #fff; }")
            if self.solve(self.next_pos(pos)):
                return True
        self.s[y][x].setText('')  # backtrack, reset cell to empty
        return False  # stop searching this recursion tree: no solution


def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
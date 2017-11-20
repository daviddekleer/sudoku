def next_pos(s, pos=[0, 0]):
    if pos == (8, 8):  # solved
        return True

    x = pos[0]
    y = pos[1]
    while s[y][x]:  # as long as there are predefined numbers
        if x == 8 and y == 8:  # stop if it's the last number
            break
        if x == 8:  # next row
            y += 1
            x = 0
        else:  # next column
            x += 1

    return (x, y)


def allowed_numbers_for_pos(s, pos):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = pos[0]
    y = pos[1]
    s[y][x] = 0

    # find left top postion of square
    x_square_start = (x // 3) * 3
    y_square_start = (y // 3) * 3
    # remove already filled in nrs from numbers
    for ys in range(y_square_start, y_square_start + 3):
        for xs in range(x_square_start, x_square_start + 3):
            number = s[ys][xs]
            if number in numbers:
                numbers.remove(number)

    # check column
    for ys in range(9):
        number = s[ys][x]
        if number in numbers:
            numbers.remove(number)

    # check row
    for xs in range(9):
        number = s[y][xs]
        if number in numbers:
            numbers.remove(number)

    return numbers


def backtrack(s, pos, predefined):
    # set positions to 0, starting from pos
    for y in range(pos[1], 9):
        for x in range(pos[0], 9):
            if (x, y) in predefined:  # don't alter predefined numbers
                continue
            s[y][x] = 0
    return s


def predefined_numbers(s):
    predefined = []
    for y in range(9):
        for x in range(9):
            if s[y][x]:
                predefined.append((x, y))
    return predefined


def sudoku_solver(s, pos=None, predefined=None):
    if pos is True:  # solved
        return s

    if not pos:  # initialize pos and predefined numbers
        pos = next_pos(s)
        predefined = predefined_numbers(s)

    allowed_numbers = allowed_numbers_for_pos(s, pos)
    for number in allowed_numbers:
        # try the allowed numbers and continue with next pos
        s[pos[1]][pos[0]] = number
        if sudoku_solver(s, next_pos(s, pos), predefined):
            return s
    s = backtrack(s, pos, predefined)
    return False  # stop searching this recursion tree: no solution


if __name__ == '__main__':
    # "World's hardest sudoku"
    solution = sudoku_solver([[8, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 3, 6, 0, 0, 0, 0, 0],
                              [0, 7, 0, 0, 9, 0, 2, 0, 0],
                              [0, 5, 0, 0, 0, 7, 0, 0, 0],
                              [0, 0, 0, 0, 4, 5, 7, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0, 3, 0],
                              [0, 0, 1, 0, 0, 0, 0, 6, 8],
                              [0, 0, 8, 5, 0, 0, 0, 1, 0],
                              [0, 9, 0, 0, 0, 0, 4, 0, 0]])
    for row in solution:
        print(row)

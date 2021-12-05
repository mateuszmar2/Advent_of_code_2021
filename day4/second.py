# nadpisuje całą tablicę -2 żeby przestać z niej korzystać
def clearBoard(board):
    for x in range(5):
        for y in range(5):
            board[x][y] = -2


# zaznacza w danej planszy podaną liczbę
def mark(board, digit):
    for x in range(5):
        for y in range(5):
            if board[x][y] == digit:
                board[x][y] = -1


# sprawdza, czy w danej planszy można coś skreślić
def check(board):
    # sprawdza wiersze i kolumny
    for x in range(5):
        sum_row = 0
        sum_col = 0
        for y in range(5):
            sum_row += int(board[x][y])
            sum_col += int(board[y][x])
        if sum_row == -5 or sum_col == -5:
            return True

    return False


# zwraca sumę liczb, które nie są zaznaczone w danej planszy
def sumUnmarked(board):
    sum = 0
    for row in board:
        for value in row:
            if value != -1:
                sum += int(value)
    return sum


# zwraca pierwszą skreśloną planszę
def calculateResult(bingo, digits):
    result = -1
    for digit in digits:
        for board in bingo:
            mark(board, digit)
            if check(board):
                result = sumUnmarked(board) * int(digit)
                clearBoard(board)
    return result


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    digits = lines[0].split(",")

    bingo = []
    for line in lines[2:]:
        if line:
            bingo.append(line.split())

    temp = []
    for x in range(0, len(bingo) - 1, 5):
        temp.append([bingo[y + x] for y in range(5)])

    bingo = temp

    print(calculateResult(bingo, digits))


if __name__ == "__main__":
    main()

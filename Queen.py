BOARD = [[0] * 8 for i in range(8)]

coordinates = ((1, 1), (7, 0), (2, 3), (6, 7), (4, 7), (3, 5), (3, 7), (2, 4))
for i in coordinates:
    BOARD[i[0]][i[1]] = 1


def check_position(board, row, column):
    queens = 0
    for i in range(8):
        queens = queens + board[row][i]
        if queens > 1:
            return False
    queens = 0
    for i in range(8):
        queens = queens + board[i][column]
        if queens > 1:
            return False
    queens = 0
    for i in range(8):
        queens = queens + board[i][i]
        if queens > 1:
            return False
    return True


def put_the_figure():
    x = int(input("x = ")) - 1
    y = int(input("y = ")) - 1
    BOARD[x][y] = 1
    if check_position(BOARD, x, y):
        print(f" {x}, {y} ферзь находится в безопасности")
        print_board(BOARD)
    else:
        print(f"По координатам {x}, {y} ферзь под ударом")
        print_board(BOARD)


def print_board(board):
    l = len(board)
    for i in range(l):
        print("|", end="")
        for j in range(l):
            if board[j][i] == 1:
                print("#", end="|")
            else:
                print(" ", end="|")
        print()

if __name__ == "__main__":
    print_board(BOARD)
    for i in coordinates:
        if check_position(BOARD, i[0], i[1]):
            print(f"По координатам {i[0]}, {i[1]} ферзь находится в безопасности")
# put_the_figure()

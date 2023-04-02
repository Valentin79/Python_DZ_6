from Queen import check_position, print_board
from random import randint


QUEENS = 8
BOARD_SIZE = 8
available_placement = []
available_placement_count = 0
total_iteration = 0

while available_placement_count < 4:
    BOARD = [[0] * 8 for i in range(BOARD_SIZE)]
    total_iteration += 1
    # coordinates = [(randint(0, 7), randint(0, 7)) for i in range(8)]
    # ^ генератор сверху давал повторы. Сделал так, что бы всегда было 8 ферзей
    coordinates = []
    while len(coordinates) < QUEENS:
        x = (randint(0, 7), randint(0, 7))
        if x not in coordinates:
            coordinates.append(x)

    for i in coordinates: # Расстанавливаем фигуры на доске
        BOARD[i[0]][i[1]] = 1


    def check_placement(): #  Проверка расстановки
        for i in coordinates:
            x, y = i[0], i[1]
            if check_position(BOARD, x, y) == False:
                return False
        return True


    if check_placement(): # если проверка пройдена - добавляем коомбинацию в список
        available_placement_count += 1
        available_placement.append(coordinates)


print(f"Возможные расстановки: \n(Всего итераций потрачено: {total_iteration})")
for placement in available_placement:
    BOARD = [[0] * 8 for i in range(8)]
    for i in placement:
        BOARD[i[0]][i[1]] = 1
    print(placement)
    print_board(BOARD)
    print()

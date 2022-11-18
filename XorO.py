pole = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]


def process():
    return print(str(pole[0]) + "\n" + str(pole[1]) + "\n" + str(pole[2]))


def data():
    while True:

        result = input("Выберите клетку (например: 1 1): ").split()

        if len(result) < 2:
            print('Введите через пробел!')
            return data()

        if not ''.join(result).isdigit():
            print('Используйте только цифры!')
            return data()

        x = int(result[0])
        y = int(result[1])

        if 1 <= x <= 3 and 1 <= y <= 3:
            if pole[x-1][y-1] == '-':
                return x, y
            else:
                print('Ячейка занята!')
        else:
            print('Вне диапазана! Диапазон от 1 до 3')


def check():
    diag1 = pole[0][0]+pole[1][1]+pole[2][2]
    diag2 = pole[2][0]+pole[1][1]+pole[0][2]
    for i in pole:
        if i == ['x', 'x', 'x']:
            print('Выиграл X')
            return True
        if i == ['O', 'O', 'O']:
            print('Выиграл O')
            return True
    for i in zip(pole[0], pole[1], pole[2]):
        if i == ('x', 'x', 'x'):
            print('Выиграл X')
            return True
        if i == ('O', 'O', 'O'):
            print('Выиграл O')
            return True
    if diag1 == "xxx" or diag2 == "xxx":
            print('Выиграл X')
            return True
    if diag1 == "OOO" or diag2 == "OOO":
            print('Выиграл O')
            return True
count = 0
while True:
    process()
    if count % 2 == 0:
        print('Рисуем крестик x')
    else:
        print('Рисуем нолик O')

    x, y = data()

    if count % 2 == 0:
        pole[x-1][y-1] = 'x'
    else:
        pole[x-1][y-1] = 'O'

    count += 1

    if check():
        process()
        break

    if count == 9:
        print('Ничья!')
        process()
        break









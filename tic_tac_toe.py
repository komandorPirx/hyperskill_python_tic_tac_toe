# write your code here
def check_draw(lista):
    X_counter = 0
    O_counter = 0
    for i in lista:
        if i == 'X':
            X_counter += 1
        elif i == 'O':
            O_counter += 1
    return X_counter, O_counter


def check(lista):
    lista2 = [lista[x: x + 3] for x in range(0, len(lista), 3)]
    win_X = False
    win_O = False

    if lista2[0][1] == lista2[1][1] == lista2[2][1] == 'X':
        win_X = True
    if lista2[0][1] == lista2[1][1] == lista2[2][1] == 'O':
        win_O = True
    if lista2[0][0] == lista2[0][1] == lista2[0][2] == 'X':
        win_X = True
    if lista2[0][0] == lista2[0][1] == lista2[0][2] == 'O':
        win_O = True
    if lista2[0][0] == lista2[1][0] == lista2[2][0] == 'X':
        win_X = True
    if lista2[0][0] == lista2[1][0] == lista2[2][0] == 'O':
        win_O = True
    if lista2[1][0] == lista2[1][1] == lista2[1][2] == 'X':
        win_X = True
    if lista2[1][0] == lista2[1][1] == lista2[1][2] == 'O':
        win_O = True
    if lista2[2][0] == lista2[2][1] == lista2[2][2] == 'X':
        win_X = True
    if lista2[2][0] == lista2[2][1] == lista2[2][2] == 'O':
        win_O = True
    if lista2[0][0] == lista2[1][1] == lista2[2][2] == 'X':
        win_X = True
    if lista2[0][0] == lista2[1][1] == lista2[2][2] == 'O':
        win_O = True
    if lista2[0][2] == lista2[1][2] == lista2[2][2] == 'X':
        win_X = True
    if lista2[0][2] == lista2[1][2] == lista2[2][2] == 'O':
        win_O = True
    if lista2[0][2] == lista2[1][1] == lista2[2][0] == 'X':
        win_X = True
    if lista2[0][2] == lista2[1][1] == lista2[2][0] == 'O':
        win_O = True

    return win_X, win_O

    # print(lista2)


def check_winer(lista):
    win_X, win_O = check(lista)
    X_nb, O_nb = check_draw(lista)
    X_number = 5
    O_number = 4
    draw = False
    X_counter, O_counter = check_draw(lista)

    if win_X and win_O == False:
        print("X wins")
    elif win_O and win_X == False:
        print("O wins")
    elif X_nb is X_number and O_nb is O_number:
        print("Draw")
    elif win_X is False and win_O is False and (X_nb - O_nb) == 1 or (X_nb - O_nb) == 0:
        print("Game not finished")
    elif (win_X and win_O) or X_nb < O_nb or (X_nb - O_nb) > 1:
        print("Impossible")


def display(lista):
    print("---------")
    for i in range(len(lista)):
        if i % 3 == 0:
            print("| ", end="")
        print(lista[i] + " ", end="")
        if (i + 1) % 3 == 0:
            print("|", end="\n")
    print("---------")
def input_coords(x):
    d = {1: x[0:3], 2: x[3:6], 3: x[6:9]}
    while True:
        coords = str(input()).replace(" ", "")
        if not coords.isdigit():
            print("You should enter numbers!")
            continue

        X_coord = int(coords[0])
        Y_coord = int(coords[1])
        if (1 > X_coord or X_coord > 3) or (Y_coord < 1 or Y_coord > 3):
            print("Coordinates should be from 1 to 3!")
            continue
        elif d[X_coord][Y_coord - 1] == 'X' or d[X_coord][Y_coord - 1] == 'O':
            print("This cell is occupied! Choose another one!")
            continue
        else:
            break
    return X_coord, Y_coord

def add_X_to_list(x, lista):
    X_coord = lista[0]
    Y_coord = lista[1]
    d = {1:x[0:3], 2:x[3:6], 3:x[6:9]}
    value = d[X_coord][Y_coord - 1]
    if value == '_':
        d[X_coord][Y_coord - 1] = 'X'
    lista_out = list()
    i = 0
    for val in d.values():
        for val1 in val:
            lista_out.append(val1)

    return lista_out


list1 = []
list1[:0] = input()
display(list1)
check_winer(list1)
coords = input_coords(list1)
new_list = add_X_to_list(list1, coords)
display(new_list)



# Advent of Code - day3 (part II)
import numpy as np


def find_puzzle(input_n, init_level):
    current_value = init_level[0][0]
    current_level = init_level[0][1]
    size_matrix = np.square(current_level)
    while input_n > size_matrix:
        current_value += 1
        current_level += 2
        init_level.append([current_value, current_level])
        size_matrix = np.square(init_level[current_value][1])
    return init_level


def move_right_one(i, j, puzzle, num):
    print('RIGHT')
    i = i
    j += 1
    print([int(num), i, j])
    puzzle.append([int(num), i, j])
    return puzzle, i , j


def move_right(i, j, puzzle, num):
    for t in num:
        print('RIGHT')
        i = i
        j += 1
        print([int(t), i, j])
        puzzle.append([int(t), i, j])
    return puzzle, i , j


def move_up(i, j, puzzle, num):

    for t in num:
        print('UP')
        i -= 1
        j = j
        print([int(t), i, j])
        puzzle.append([int(t), i, j])
    return puzzle, i, j


def move_left(i, j, puzzle, num):

    for t in num:
        print('LEFT')
        i = i
        j -= 1
        print([int(t), i, j])
        puzzle.append([int(t), i, j])
    return puzzle, i, j


def move_down(i, j, puzzle, num):

    for t in num:
        print('DOWN')
        i += 1
        j = j
        print([int(t), i, j])
        puzzle.append([int(t), i, j])
    return puzzle, i, j


def create_puzzle(max_level, check_value):
    if max_level == 1:
        i = 0
        j = 0
        puzzle_ref = [[1, i, j]]
        puzzle_matrix = [[1, i, j]]
        result_value = 1
    else:
        max_size = len(max_level)
        print(max_size)
        max_n_list = np.square(max_level[max_size - 1][1])
        print(max_n_list)

        num = np.arange(1, max_n_list + 1)
        print(num)

        step_max = max_level[max_size - 1][0]
        i = step_max
        j = step_max
        step = 1
        puzzle_ref = []
        puzzle_ref.append([1, i, j])
        print()
        print('START')
        print([1, i, j])
        counter = 1
        puzzle_matrix = np.zeros((int(np.sqrt(max_n_list)), (int(np.sqrt(max_n_list)))))
        sum_all = 1
        while step <= step_max:
            print('--------------')
            print('Step:', step)
            print('Min pointer:', max_level[step - 1][1])
            print('Max pointer:', max_level[step][1])
            range_values = np.arange(np.square(max_level[step - 1][1]), np.square(max_level[step][1]) + 1)
            print(range_values)

            # First step
            t = 1
            puzzle_ref1, i, j = move_right_one(i, j, puzzle_ref, num[counter])
            counter = counter + t

            # Second step
            t = max_level[step - 1][1]
            puzzle_ref2, i, j = move_up(i, j, puzzle_ref1, num[counter: counter + t])
            counter = counter + t

            # third step
            t = max_level[step][1] - 1
            puzzle_ref3, i, j = move_left(i, j, puzzle_ref2, num[counter: counter + t])
            counter = counter + t

            # fourth step
            t = max_level[step][1] - 1
            puzzle_ref4, i, j = move_down(i, j, puzzle_ref3, num[counter: counter + t])
            counter = counter + t

            # last step
            t = max_level[step][1] - 1
            puzzle_ref, i, j = move_right(i, j, puzzle_ref4, num[counter: counter + t])
            counter = counter + t



            cont = 0
            print(puzzle_ref[np.square(max_level[step - 1][1]) - 1: np.square(max_level[step][1]) + 1])
            elements = puzzle_ref[np.square(max_level[step - 1][1]) - 1: np.square(max_level[step][1]) + 1]
            for element in elements:
                if cont < len(elements) - 1:
                    print('\nBuild matrix')
                    print(element)

                    puzzle_matrix[element[1]][element[2]] = sum_all
                    print(puzzle_matrix)

                    print()
                    print('next element')
                    print(elements[cont + 1])

                    i_min = int(elements[cont + 1][1]) - 1
                    i_max = (int(elements[cont + 1][1]) + 2)
                    j_min = elements[cont + 1][2] - 1
                    j_max = (elements[cont + 1][2] + 2)

                    if i_min >= 0 and j_min >= 0:
                        print('Case 1')
                        print('Imin,Imax', i_min, i_max - 1, '\nJmin,Jmax', j_min, j_max - 1)
                        submatrix = puzzle_matrix[i_min:i_max, j_min:j_max]
                    elif i_min < 0 and j_min >= 0:
                        print('Case 2')
                        i_min = 0
                        print('Imin,Imax', i_min, i_max - 1, '\nJmin,Jmax', j_min, j_max - 1)
                        submatrix = puzzle_matrix[i_min:i_max, j_min:j_max]
                    elif i_min >= 0 and j_min < 0:
                        print('Case 3')
                        j_min = 0
                        print('Imin,Imax', i_min, i_max - 1, '\nJmin,Jmax', j_min, j_max - 1)
                        submatrix = puzzle_matrix[i_min:i_max, j_min:j_max]
                    elif i_min < 0 and j_min < 0:
                        print('Case 4')
                        i_min = 0
                        j_min = 0
                        print('Imin,Imax', i_min, i_max - 1, '\nJmin,Jmax', j_min, j_max - 1)
                        submatrix = puzzle_matrix[i_min:i_max, j_min:j_max]

                    print(submatrix)
                    sum_all = sum(map(sum, submatrix))
                    print(sum_all)
                    if sum_all > check_value:
                        result_value = sum_all
                        break
                    else:
                        result_value = 0

                    cont += 1
            puzzle_matrix[element[1]][element[2]] = sum_all
            print()
            print(puzzle_matrix)
            step += 1

    return puzzle_ref, puzzle_matrix, result_value


check_value = 277678
puzzle_input = 50
init = [[0, 1]]
size_puzzle = find_puzzle(puzzle_input, init)
max_size = len(size_puzzle)
print('Size of the puzzle is:', int(size_puzzle[max_size - 1][1]), ' x ', int(size_puzzle[max_size - 1][1]))


puzzle_ref, puzzle_matrix, result_value = create_puzzle(size_puzzle, check_value)
print()

puzzle_mat = np.zeros((int(size_puzzle[max_size - 1][1]), int(size_puzzle[max_size - 1][1])))
for element in puzzle_ref:
    puzzle_mat[element[1]][element[2]] = element[0]
print(puzzle_mat)

move_x = abs(puzzle_ref[puzzle_input - 1][1] - puzzle_ref[1 - 1][1])
move_y = abs(puzzle_ref[puzzle_input - 1][2] - puzzle_ref[1 - 1][2])
print()
print('Move along x:', move_x)
print('Move along y:', move_y)
print('Data from square # ', puzzle_input, ' # is carried in ----> ', move_x + move_y, 'steps')


print()
if result_value > 0:
    print('The first value written that is larger than the check_value is:', result_value)
else:
    print('NOT FOUND!!! You need to increase the puzzle_input')

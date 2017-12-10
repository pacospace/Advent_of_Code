# Advent of Code - day 10 (Part I) of Knot Hash algorithm
import math


def current_c(c_list, c_counter):

    d = math.floor(c_counter / len(c_list))
    c_new = c_counter - len(c_list) * d

    return c_new


def main():

    circular_list = []
    el = 0

    while el < 256:
        circular_list.append(el)
        el += 1

    input_lengths = [197, 97, 204, 108, 1, 29, 5, 71, 0, 50, 2, 255, 248, 78, 254, 63]

    c = 0
    skip_size = 0
    for il in input_lengths:

        c = current_c(circular_list, c)

        if c + il <= len(circular_list) - 1:

            sublist = circular_list[c:c + il]
            rev_sublist = list(sublist[::-1])
            circular_list[c:c + il] = rev_sublist

        elif c + il > len(circular_list) - 1:

            diff = c + il - len(circular_list)
            sublist = circular_list[c:len(circular_list)] + circular_list[0: diff]
            rev_sublist = list(sublist[::-1])
            circular_list[c:len(circular_list)] = rev_sublist[0:len(circular_list) - c]
            circular_list[0: diff] = rev_sublist[len(circular_list) - c: len(rev_sublist)]

        c = c + il + skip_size
        skip_size += 1

    solution = circular_list[0]*circular_list[1]
    print('\n------------------------------------------------------------------------------------'
          f'\nThe result of multiplying the first two numbers in the list is ---->  {solution}',
          '\n------------------------------------------------------------------------------------')


if __name__ == '__main__':
    main()

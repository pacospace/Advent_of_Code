# Advent of Code - Day 2 (Part II)
import re


def divisible_values(row):
    j = 0
    rest = []
    for el in row:
        for i in row:
            if j <= len(row) - 1:
                if row[j] != i:
                    rest.append([row[j], i, float(row[j]) / i])
        j += 1
    return rest


def main():
    file = open('spreadshit.txt')

    spreadshit = file.read()
    list_row = re.split('\n', spreadshit)

    list_divisible = []
    n_element = 1
    for row in list_row:
        element = [int(c) for c in row.split()]
        print('---------------------')
        print('Line number:', n_element)
        print()
        print('Row:', element)
        print('-----------------------')
        rest = divisible_values(element)
        for triple in rest:
            if triple[2].is_integer() is True:
                print(triple)
                list_divisible.append(triple[2])
        print()
        n_element += 1

    print()
    print('The checksum for the spreadshit is:', int(sum(list_divisible)))


if __name__ == '__main__':
    main()




# Advent of Code - Day 1 (Part 2)
import sys


def check_match(current_element, next_element, list_matches):
    print()
    print('---------------------------')
    print('Element number:', current_element[1] + 1)
    print('Current element is:', current_element[0])
    print('Next element is:   ', next_element[0])
    if current_element[0] == next_element[0]:
        print('\n ---> Match')
        list_matches.append(current_element[0])
    else:
        print('\n ---> No Match')
        pass
    return list_matches


def main():
    captcha = open('captchaday1.txt')

    elements = captcha.read()

    list_elements = []
    element_n = 0
    for element in elements:
        list_elements.append([int(element), element_n])
        element_n += 1

    print('The list of elements is:\n', list_elements)
    length_list = len(list_elements)
    print('\nLength of the list is:', length_list, '\n')

    if (length_list % 2) == 0:
        print('The list has even number of elements')
        pass
    else:
        print("Error: The list has odd number.\n")
        sys.exit(1)

    it = 0
    list_matches = []
    step = length_list / 2
    for element in list_elements:
        next_it = (it + int(step))

        if it < length_list - 1 and next_it < length_list - 1:
            list_matches = check_match(list_elements[it], list_elements[next_it], list_matches)

        elif it < length_list - 1 <= next_it:
            difference = next_it - (length_list - 1)
            print('difference is:', difference)
            list_matches = check_match(list_elements[it], list_elements[difference - 1], list_matches)

        elif it == length_list - 1:
            print()
            print('---------------------------')
            print('---------------------------')
            print('LAST ELEMENT OF THE LIST')
            list_matches = check_match(list_elements[it], list_elements[0 + int(step) - 1], list_matches)

        else:
            break
        it += 1

    print('\n\nThe solution of the chaptcha is:', sum(list_matches))


if __name__ == '__main__':
    main()
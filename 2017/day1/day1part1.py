# Advent of Code - Day 1 (Part 1)

captcha = open('captchaday1.txt')

elements = captcha.read()

list_elements = []
element_n = 0
for element in elements:
    list_elements.append([int(element), element_n])
    element_n += 1
print('The list of elements is:\n', list_elements)


def check_match(current_element, next_element):
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


it = 0
list_matches = []
for element in list_elements:
    if it < len(list_elements) - 1:
        list_matches = check_match(list_elements[it], list_elements[it + 1])

    elif it == len(list_elements) - 1:
        print()
        print()
        print('Last element of the list')
        list_matches = check_match(list_elements[it], list_elements[0])

    else:
        break
    it += 1

print('\n\nThe solution of the chaptcha is:', sum(list_matches))

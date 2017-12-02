# Advent of Code - Day 2 (Part I)
import re

file = open('spreadshit.txt')

spreadshit = file.read()
list_row = re.split('\n', spreadshit)

list_difference = []
n_element = 1
for row in list_row:
    element = [int(c) for c in row.split()]
    print('---------------------')
    print('Line number:', n_element)
    print()
    print(element)
    max_value = max(element)
    print('Max value is:', max_value)
    min_value = min(element)
    print('Min value is:', min_value)
    difference = max_value - min_value
    print('The difference is:', difference)
    list_difference.append(difference)
    print()
    n_element += 1

print()
print('The checksum for the spreadshit is:', sum(list_difference))
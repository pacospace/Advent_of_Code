# Advent of Code - day 13 (Part I)
import re
import numpy as np


def scanners_move(position_scanner):
    for s in position_scanner:
        if s[2] == 2:
            pass
        elif s[2] == 1 and configuration[s[0] + 1, s[1]] == 1:
            position_scanner[s[1]] = [s[0] + 1, s[1], 1]
        elif s[2] == 1 and configuration[s[0] + 1, s[1]] == 0:
            position_scanner[s[1]] = [s[0] - 1, s[1], 0]
        elif s[2] == 0 and configuration[s[0] - 1, s[1]] == 1:
            position_scanner[s[1]] = [s[0] - 1, s[1], 0]
        elif s[2] == 0 and configuration[s[0] - 1, s[1]] == 0:
            position_scanner[s[1]] = [s[0] + 1, s[1], 1]

    return position_scanner


def main():

    f = open('firewall.txt').read().split('\n')
    regex = r"(\d+): (\d+)"
    firewall = list()
    for el in f:
        s = re.findall(regex, el)
        firewall.append([int(s[0][0]), int(s[0][1])])

    print('\n', firewall)
    max_layer = firewall[len(firewall) - 1][0]
    max_range = firewall[len(firewall) - 1][1]
    print('\nMax layer is:', max_layer)
    print('\nMax range is:', max_range)

    print()
    layers = []
    ranges = []
    for i in range(0, max_layer + 1):
        layers.append([i, 1])
        ranges.append(0)
    valid_layers = set([m[0] for m in firewall])
    print(ranges)
    for j in firewall:
        y = j[1]
        x = j[0]
        layers[x] = j
        ranges[x] = y
    print(layers)
    print(ranges)
    global configuration
    configuration = np.zeros((max_layer + 1, max_layer + 1))
    print()
    for l in layers:
        configuration[0:l[1], l[0]] = np.ones(l[1])
    print(configuration)

    scanners_init_position = []
    n = 0
    for el in configuration:
        if n not in valid_layers:
            scanners_init_position.append([0, n, 2])
        else:
            scanners_init_position.append([0, n, 1])
        n += 1

    print(valid_layers)
    c = 0
    caught = []
    for nn in range(0, max_layer + 1):
        print('\nlayer n.', nn)

        mouse = [0, nn]
        print(scanners_init_position)
        print(mouse)
        if scanners_init_position[nn][0:2] == mouse:
            if mouse[1] in valid_layers:
                print('caught')
                caught.append([c + 1, nn, ranges[nn]])
                c += 1
            else:
                print('skip')
        else:
            print('not caught')
        scanners_positions = scanners_move(scanners_init_position)

        scanners_init_position = scanners_positions
    print(caught)
    solution = []
    for e in caught:
        solution.append(e[1]*e[2])
    print('\nGot caught {} times:'.format(len(caught)))
    for ee in caught:
        print('N. {} in layer {}'.format(ee[0], ee[1]))
    print('The severity of the whole trip is: {}'.format(sum(solution)))


if __name__ == '__main__':
    main()
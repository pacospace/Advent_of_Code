# Advent of Code - day 13 (Part II)
import re
import numpy as np
import time


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


def not_caught_config(scanners_positions):

    init = list(scanners_positions)
    c = 0
    for nn in range(0, max_layer + 1):
        mouse = [0, nn]
        if scanners_positions[nn][0:2] == mouse and mouse[1] in valid_layers:
            c = 1
            break
        else:
            pass
            scanners_positions = scanners_move(scanners_positions)

    return scanners_move(init), c


def main():

    f = open('firewall.txt').read().split('\n')
    regex = r"(\d+): (\d+)"
    firewall = list()
    for el in f:
        s = re.findall(regex, el)
        firewall.append([int(s[0][0]), int(s[0][1])])

    print('\n', firewall)
    global max_layer
    max_layer = firewall[len(firewall) - 1][0]
    max_range = firewall[len(firewall) - 1][1]
    print('\nMax layer is:', max_layer)
    print('\nMax range is:', max_range)

    print()
    global ranges
    layers = []
    ranges = []
    for i in range(0, max_layer + 1):
        layers.append([i, 1])
        ranges.append(0)

    global valid_layers

    valid_layers = set([m[0] for m in firewall])

    for j in firewall:
        y = j[1]
        x = j[0]
        layers[x] = j
        ranges[x] = y

    global configuration

    configuration = np.zeros((max_layer + 1, max_layer + 1))
    for l in layers:
        configuration[0:l[1], l[0]] = np.ones(l[1])

    scanners_init_position = []
    n = 0
    for el in configuration:
        if n not in valid_layers:
            scanners_init_position.append([0, n, 2])
        else:
            scanners_init_position.append([0, n, 1])
        n += 1

    picos = 0
    start = time.time()
    maxx = 5000000
    for picos in range(1, maxx):
        scanners_init_position, c = not_caught_config(scanners_init_position)
        if c == 0:
            break

    stop = time.time()
    duration = stop - start
    print('\nTime to find the solution is:', duration, ' [s]')
    print('\nThe fewest number of picoseconds that you need to delay the packet'
          ' to pass through the firewall without being caught is ---> {}'.format(picos))


if __name__ == '__main__':
    main()
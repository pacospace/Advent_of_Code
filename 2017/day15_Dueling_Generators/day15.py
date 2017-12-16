# Advent of Code - day15 (Part I)
import time


def generator(value, constant):
    m = value*constant
    fix_value = 2147483647
    d = m % fix_value
    return d


def main():
    iteration_n = 1058
    counter = 0
    v_A = 883
    v_B = 879
    start = time.time()
    for i in range(0, iteration_n):
        print('\nIteration n.', i + 1)
        v_A = generator(v_A, 16807)
        v_B = generator(v_B, 48271)
        print(v_A, v_B)
        a = bin(v_A)[2:]
        b = bin(v_B)[2:]
        if a[len(a) - 16:] == b[len(b) - 16:]:
            counter += 1
    stop = time.time()
    duration = stop - start
    print('\nTime to find the solution is:', duration, ' [s]')
    print('\nThe judge final count is ----->', counter)


if __name__ == '__main__':
    main()
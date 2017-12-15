# Advent of Code - day15 (Part II)
import time


def generator(value, constant):
    m = value*constant
    fix_value = 2147483647
    d = m % fix_value
    return d


def main():
    iteration_n = 40000000
    counter = 0
    v_A = 883
    v_B = 879
    generator_A = []
    generator_B = []
    start = time.time()
    for i in range(0, iteration_n):
        print('\nIteration n.', i + 1)
        v_A = generator(v_A, 16807)
        v_B = generator(v_B, 48271)

        if v_A % 4 == 0:
            generator_A.append(v_A)
        if v_B % 8 == 0:
            generator_B.append(v_B)

    print()
    n = 0
    for el in range(0, min([len(generator_A), len(generator_B)])):
        a = bin(generator_A[n])[2:]
        b = bin(generator_B[n])[2:]
        if a[len(a) - 16:] == b[len(b) - 16:]:
            print('n', n + 1)
            print(generator_A[n], generator_B[n])
            print('check 1')
            counter += 1
        n += 1

    stop = time.time()
    duration = stop - start
    print('\nTime to find the solution is:', duration, ' [s]')
    print('\nThe judge final count is ----->', counter)


if __name__ == '__main__':
    main()
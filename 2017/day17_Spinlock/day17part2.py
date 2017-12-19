# Advent of Code - day 17 (Part II)
import time


def spinlock():
    max_value = 50000000
    last_value = 0
    step = 329
    b = [0]
    current_index = 0
    start = time.time()

    for i in range(1, max_value + 1):
        print(i)
        if current_index + step < i - 1:
            current_index = current_index + step
        else:
            current_index = (current_index + step) % i
        b.insert(current_index + 1, i)
        current_index = b.index(i)

    stop = time.time()
    duration = stop - start
    print('\nTime to find the solution is:', duration, ' [s]')
    print(f'The value after {last_value} in the completed circular buffer is {b[b.index(last_value) + 1]}')


if __name__ == '__main__':
    spinlock()
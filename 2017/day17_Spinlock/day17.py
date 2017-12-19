# Advent of Code - day 17 (Part I)
import time


class CircularBuffer:

    def __init__(self, capacity):
        self.buffer = [0]
        self.max_index = len(self.buffer) - 1
        self.capacity = capacity
        self.current_index = 0

    def push_element(self, value, new_index):
        if len(self.buffer) == self.capacity:
            raise Exception('The circular buffer is full.')
        self.buffer.insert(new_index, value)
        self.max_index = len(self.buffer) - 1
        self.current_index = self.buffer.index(value)


def index_element(max_i, current_i):
    si = current_i
    step = 329
    if si + step < max_i:
        si = si + step
    else:
        si = (si + step) % (max_i + 1)
    return si


def spinlock():
    max_value = 2017
    last_value = 2017
    b = CircularBuffer(max_value + 1)

    start = time.time()
    for i in range(1, max_value + 1):
        index = index_element(b.max_index, b.current_index)
        new_index = index + 1
        b.push_element(i, new_index)
    sol = b.buffer.index(last_value)
    stop = time.time()
    duration = stop - start
    print('\nTime to find the solution is:', duration, ' [s]')
    print(f'The value after {last_value} in the completed circular buffer is {b.buffer[sol + 1]}')


if __name__ == '__main__':
    spinlock()
# Advent of Code - day 17 (Part I)


class CircularBuffer:

    def __init__(self, capacity):
        self.buffer = [0]
        self.max_index = len(self.buffer) - 1
        self.capacity = capacity
        self.current_index = 0

    def push_element(self, value):
        if len(self.buffer) == self.capacity:
            raise Exception('The circular buffer is full.')
        self.buffer.append(value)
        self.max_index = len(self.buffer) - 1
        self.current_index += 1


def spinlock():
    step = 3
    b = CircularBuffer(2018)

    index = b.current_index

    index = index + step
    print('Trial index is:', index)

    print('Actual index is:', index)


if __name__ == '__main__':
    spinlock()
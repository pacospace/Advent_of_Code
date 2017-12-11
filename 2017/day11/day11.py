# Advent of Code - day 11 (Part I)


def next_step(position, direction):

    x = position[0]
    y = position[1]

    if direction == 'n':
        print('North')
        x = x
        y += 1
    elif direction == 's':
        print('South')
        x = x
        y -= 1
    elif direction == 'ne':
        print('North East')
        x += 0.5
        y += 0.5
    elif direction == 'nw':
        print('North West')
        x -= 0.5
        y += 0.5
    elif direction == 'se':
        print('South East')
        x += 0.5
        y -= 0.5
    elif direction == 'sw':
        print('South West')
        x -= 0.5
        y -= 0.5
    return x, y


def main():
    inputs = open('input.txt').read().split(',')
    print(inputs)
    n = 0
    s_pos = [0, 0]
    print(len(inputs))
    path = [s_pos]
    for i in inputs:
        print('----------------------------')
        print('Step n.{}, direction {}'.format(n + 1, i))
        pos = path[n]
        print(pos)
        print('Current position x = {}, y = {}'.format(pos[0], pos[1]))
        x, y = next_step(pos, i)
        print('New position x = {}, y = {} '.format(x, y))
        path.append([x, y])

        n += 1
    last_pos = abs(path[len(path) - 1][0]) + abs(path[len(path) - 1][1])
    print('\n\nPart 1: The fewest number of steps required to reach the child are {}'.format(last_pos))

    steps_path = []
    for p in path:
        steps_path.append(abs(p[0]) + abs(p[1]))
    step_max = max(steps_path)
    print('\n\nPart 2: The furthest the child ever got from his starting position is {} steps'.format(step_max))


if __name__ == '__main__':
    main()
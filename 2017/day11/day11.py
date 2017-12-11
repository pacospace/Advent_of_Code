# Advent of Code - day 11 (Part I)


def next_step(position, direction):
    directions = {'n': [0, 1, 'North'], 's': [0, -1, 'South'],
                  'ne': [0.5, 0.5, 'North East'], 'nw': [-0.5, 0.5, 'Nort West'],
                  'se': [0.5, -0.5, 'South East'], 'sw': [-0.5, -0.5, 'South West']}

    x = position[0] + directions[direction][0]
    y = position[1] + directions[direction][1]
    print('Direction ---> {}'.format(directions[direction][2]))

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
        print('Step n.{}'.format(n + 1))
        print('Current position x = {}, y = {}'.format(path[n][0], path[n][1]))
        x, y = next_step(path[n], i)
        print('New position x = {}, y = {} '.format(x, y))
        path.append([x, y])

        n += 1
    last_pos = abs(path[len(path) - 1][0]) + abs(path[len(path) - 1][1])
    print('\n\nPart 1: The fewest number of steps required to reach the child is {}'.format(last_pos))

    steps_path = []
    for p in path:
        steps_path.append(abs(p[0]) + abs(p[1]))
    step_max = max(steps_path)
    print('\n\nPart 2: The furthest the child ever got from his starting position is {} steps'.format(step_max))


if __name__ == '__main__':
    main()
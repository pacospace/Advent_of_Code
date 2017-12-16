# Advent of Code - day 16 (Part I)
import re
import time


def dance_moves(line, move):
    if move[0] == 's':

        line = line[len(line) - move[1]:] + line[:len(line) - move[1]]
    else:

        if move[0] == 'x':

            first_ind = int(move[1][0])
            second_ind = int(move[1][1])

            first_prog = line[first_ind]
            second_prog = line[second_ind]

            line[first_ind] = second_prog
            line[second_ind] = first_prog

        if move[0] == 'p':

            first_p_ind = line.index(move[1][0])
            second_p_ind = line.index(move[1][1])

            first_p = line[first_p_ind]
            second_p = line[second_p_ind]

            line[first_p_ind] = second_p
            line[second_p_ind] = first_p

    return line


def main():
    programs = [chr(i) for i in range(97, 113)]
    f = [i.strip(' ') for i in open('dance_moves.txt').read().split(',')]

    moves = {}
    it = 1

    for w in f:
        if w[0] == 's':
            # print('Spin')
            re_s = r"(\d+)"
            m = int(re.findall(re_s, w)[0])
            moves[it] = [w[0], m]
            it += 1
        if w[0] == 'x':
            # print('Exchange')
            re_s = r"(\d+)/(\d+)"
            m = re.findall(re_s, w)
            moves[it] = [w[0], m[0]]
            it += 1
        if w[0] == 'p':
            # print('Partner')
            re_s = r"\w(\w+)/(\w+)"
            m = re.findall(re_s, w)
            moves[it] = [w[0], m[0]]
            it += 1

    n_iterations = 1000000000
    trace = []
    start = time.time()
    for j in range(1, n_iterations + 1):
        for el in range(1, len(moves) + 1):
            programs = dance_moves(programs, moves[el])
        s = ''.join(programs)

        if s in trace:
            break
        trace.append(s)
    stop = time.time()
    duration = stop - start
    print('\n\nTime to find the solution is:', duration, ' [s]')
    print('\nAfter their dance the programs are in the following order:\n\n-----> ', trace[n_iterations % len(trace) - 1])


if __name__ == '__main__':
    main()
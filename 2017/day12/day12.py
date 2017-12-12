# Advent of Code - day 21 (Part I)
import re


def parse_pipes(p_dict, p_trace, prog_id, l, trace_l):

    trace_l.append([prog_id, l])
    l += 1
    p_trace.add(prog_id)

    for q in p_dict[prog_id]:

        if q not in p_trace:

            parse_pipes(p_dict, p_trace, q, l, trace_l)

        else:

            trace_l.append([q, l])
            pass

    return p_trace, trace_l


def main():

    f = open('input12.txt').read()
    regex_pipes = "(\d+) <-> (.+)"
    data = re.findall(regex_pipes, f)
    pipes = []
    pipes_dict = {}
    programs = set()

    for d in data:
        pipes.append([d[0], d[1].split(', ')])
        pipes_dict[str(d[0])] = d[1].split(', ')
        programs.add(d[0])

    trace_pipe = set()
    program_id = '0'
    level = 0
    trace_list = []
    result, trace = parse_pipes(pipes_dict, trace_pipe, program_id, level, trace_list)
    print('\nThe programs that are in the group that contains program ID 0 are {}'.format(len(result)))
    print(trace)


if __name__ == '__main__':
    main()
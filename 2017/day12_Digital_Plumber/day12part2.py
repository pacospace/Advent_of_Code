# Advent of Code - day 21 (Part II)
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

    collections = set()
    check = set()
    collection = []
    n_counter = 1

    for p in pipes:

        program_id = p[0]

        if program_id not in check:

            level = 0
            trace_list = []
            result, trace = parse_pipes(pipes_dict, set(), program_id, level, trace_list)
            collections.add(frozenset(result))
            collection.append([n_counter, program_id, sorted(frozenset(result)), len(result)])

            for r in result:
                check.add(r)

            n_counter += 1

        else:

            pass

    file = open('r_day12.txt', 'w')
    file.write('The number of groups is --> {} \n'.format(len(collections)))
    file.write('{:9} | {:9} | {:<15}  ---->  {}'.format('Group N', 'Group ID', 'N of programs', 'Programs'))
    file.write('\n-----------------------------------------------')

    for c in sorted(collection):
        file.write('\n{:^9} | {:9} | {:^15}  ---->  {}'.format(c[0], c[1], str(c[3]) + '/2000', c[2]))

    tot = sum([s[3] for s in collection])

    file.write('\n-----------------------------------------------')
    file.write('\n{:9} | {:9} | {:^15}  ---->  {}'.format('-', '-', str(tot) + '/2000', '-'))
    file.close()


if __name__ == '__main__':
    main()
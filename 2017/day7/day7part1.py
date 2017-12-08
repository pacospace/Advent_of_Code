# Advent of Code - day7 (part I)
import re
import time


def main():

    file = open('tower.txt')
    c = file.read()
    nodes = re.findall(r"(\w+) \((\d+)\)", c)
    # for node in nodes:
    #     print('Node', node)

    roots = re.findall(r"(\w+) \((\d+)\) ", c)
    children = [ll.split() for ll in re.findall(r"\w+ \(\d+\) -> ([\w+,\s?]+)\n", c)]

    print()
    leaves = list(set(nodes) - set(roots))
    # for leaf in leaves:
    #     print('Leaf:', leaf)
    l = 0
    print()
    roots_name = []
    couple = []
    for el in list(roots):
        children[l] = [str(s).strip(',') for s in children[l]]
        roots[l] = list(el)
        roots_name.append(roots[l][0])
        couple.append([roots[l][0], children[l]])
        # print('Roots:', roots[l], 'Children:', children[l], len(children[l]))
        l += 1

    print('There are', len(nodes), 'nodes:\n   ', len(roots), 'roots and', len(leaves), 'leaves')

    start = time.time()

    level = 1
    while len(roots_name) > 1:
        print('\n check level', level)
        counter = 0
        up_counter = 0
        tree = []
        no_tree = []
        no_children = []
        for child in children:
            for h in child:
                if any(h in x for x in roots_name)is True:
                    level += 1
                    tree.append([child, level])
                    level -= 1
                    up_counter += 1
                    break
                else:
                    counter += 1
                    tree.append([child, level])

        count_no = 0
        for element in tree:
            for cc in couple:
                if element[1] == level and element[0] == cc[1]:
                    count_no += 1
                    no_tree.append(cc[0])
                    no_children.append(cc[1])

        check = set(roots_name) - set(no_tree)
        if len(check) == 1:
            print('\n--------------------------\nFound the root:', str(check).strip("{''}"), 'at level', level)
            stop = time.time()
            duration = stop - start
            print('\nTime to find the solution is:', duration, ' [s]')
            break
        else:
            roots_name = list(check)
            print('pass', len(roots_name))
            level += 1
            pass


if __name__ == '__main__':
    main()
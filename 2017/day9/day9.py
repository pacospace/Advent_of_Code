

def main():
    f = open('stream.txt')
    stream = f.read()
    l = 1
    r = 0
    group = []
    groups = []
    c = 0
    mom = 0
    while c < len(stream) - 1:
        # print('\n------------------------ \nActions n.', c, 'on -----> ', stream[c], '\n------------------------')
        if stream[c] == '<' and r == 0:
            # print('Start garbage')
            r = 1
            c += 1
        elif stream[c] == '<' and r == 1:
            # print('Still garbage')
            c += 1
            mom += 1
        elif stream[c] == '>' and r == 1:
            # print('Finish garbage')
            r = 0
            c += 1
        elif stream[c] == '<' and r == 1:
            # print('Still garbage')
            c += 1
            mom += 1
        elif stream[c] == '!' and r == 1:
            # print('Error jump in garbage')
            c += 2
        elif stream[c] == '!' and r == 0:
            # print('Error jump')
            c += 2
        elif stream[c] == '{' and r == 0:
            if l == 1:
                # print('\nStart group ----->', stream[c], 'Level', l + 1)
                l += 1
                group.append([stream[c], l])
                c += 1
            else:
                # print('\nAdd group ----->', stream[c], 'Level', l + 1)
                l += 1
                c += 1
        elif stream[c] == '{' and r == 1:
            # print('Still garbage')
            c += 1
            mom += 1
        elif stream[c] == '}' and r == 0:
            # print('\nFinish group ----->', stream[c], 'Level', l)
            l -= 1
            group.append([stream[c], l])
            # print(group)
            groups.append(group)
            group = [['{', l]]
            c += 1

        elif stream[c] == '}' and r == 1:
            # print('Still garbage')
            c += 1
            mom += 1
        elif r == 1:
            # print('Still garbage')
            c += 1
            mom += 1
        else:
            # print('\n Save ----->', stream[c])
            group.append([stream[c], l])
            c += 1

    solution = []
    for g in groups:
        solution.append(g[0][1])
    part1 = sum(solution) + 1
    part2 = mom
    print(f"\n\nPart 1: Total score is {part1}")
    print(f"Part 1: There are {part2} non-canceled characters within the garbage")


if __name__ == '__main__':
    main()

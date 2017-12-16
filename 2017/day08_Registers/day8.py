# Advent of Code - day 8 (Part I and II)
import re


def check_up_down(action):
    if action[1] == 'inc':
        print(action[0], '=', register_list[action[0]])
        register_list[action[0]] = register_list[action[0]] + int(action[2])
        print(action[0], '=', register_list[action[0]])
    elif action[1] == 'dec':
        print(action[0], '=', register_list[action[0]])
        register_list[action[0]] = register_list[action[0]] - int(action[2])
        print(action[0], '=', register_list[action[0]])
    else:
        print('ERROR')
    return register_list


def check_modify_register(main_register, condition, action):

    global register_list

    register_list = main_register

    if condition[1] == '>':
        print('\n', condition[0], condition[1], condition[2])

        if register_list[condition[0]] > int(condition[2]):
            print()
            register_list = check_up_down(action)
        else:
            print(condition[0], condition[1], condition[2], 'not satisfied, continue...')
            pass

    elif condition[1] == '<':
        print('\n', condition[0], condition[1], condition[2])
        if register_list[condition[0]] < int(condition[2]):
            print()
            register_list = check_up_down(action)
        else:
            print(condition[0], condition[1], condition[2], 'not satisfied, continue...')
            pass

    elif condition[1] == '>=':
        print('\n', condition[0], condition[1], condition[2])
        if register_list[condition[0]] >= int(condition[2]):
            print()
            register_list = check_up_down(action)
        else:
            print(condition[0], condition[1], condition[2], 'not satisfied, continue...')
            pass

    elif condition[1] == '!=':
        print('\n', condition[0], condition[1], condition[2])
        if register_list[condition[0]] != int(condition[2]):
            print()
            register_list = check_up_down(action)
        else:
            print(condition[0], condition[1], condition[2], 'not satisfied, continue...')
            pass

    elif condition[1] == '==':
        print('\n', condition[0], condition[1], condition[2])
        if register_list[condition[0]] == int(condition[2]):
            print()
            register_list = check_up_down(action)
        else:
            print(condition[0], condition[1], condition[2], 'not satisfied, continue...')
            pass

    elif condition[1] == '<=':
        print('\n', condition[0], condition[1], condition[2])
        if register_list[condition[0]] <= int(condition[2]):
            print()
            register_list = check_up_down(action)
        else:
            print(condition[0], condition[1], condition[2], 'not satisfied, continue...')
            pass
    else:
        print('Condition not satisfied, continue...')

    return register_list


def main():
    instructions = open('instructions.txt').read()

    regex_registers = "(\w+) \w+ -?\d+"
    registers = re.findall(regex_registers, instructions)
    register = {}
    rr_list = []
    for reg in sorted(set(registers)):
        register[reg] = 0
        rr_list.append(reg)

    print('There are', len(register), 'registers')

    regex_actions = "(\w+) (\w+) (-?\d+)"
    actions = re.findall(regex_actions, instructions)
    regex_conditions = "\w+ \w+ -?\d+ \w+ (\w+) (\W+) (-?\d+)"
    conditions = re.findall(regex_conditions, instructions)
    all_stuff = []
    c = 0
    signs = []
    for cond in conditions:
        all_stuff.append([cond, actions[c]])
        c += 1
        signs.append(cond[1])
    print('List of conditions signs:', set(signs))

    print()
    n = 0
    traceability_matrix = []
    for hook in all_stuff:
        print('\n----------------------\nNumber.', n + 1, '\n\n', hook[0], hook[1])
        register = check_modify_register(register, hook[0], hook[1])
        print()

        keys_n = []
        values_n = []
        for k, v in register.items():
            keys_n.append(k)
            values_n.append(v)
        traceability_matrix.append(values_n)
        n += 1

    print('\nFinal register is:\n')
    values = []
    for k, v in register.items():
        print(k, '  :', v)
        values.append(v)

    print('\nThe maximum register is:', max(values))

    cn = 0
    max_el_register = []
    max_values = []
    for nn in rr_list:
        column = []
        for t in traceability_matrix:
            column.append(t[cn])
        max_el_register.append([nn, max(column)])
        max_values.append(max(column))
        cn += 1
    print()

    print('The highest value held in any register during this process is:')
    [print(m) for m in max_el_register]
    print('\nMax value in the history of the registers is:', max(max_values))


if __name__ == '__main__':
    main()
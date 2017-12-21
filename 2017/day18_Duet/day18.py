# Advent of Code 2017 - day 18 (Part I)
import re


def registers_engine(counter):

    if instructions[counter][1] not in registers:
        registers[instructions[counter][1]] = 0

    d = 0
    if instructions[counter][0] == 'snd':
        print(f'"snd {instructions[counter][1]}" plays '
              f'a sound with a frequency equal to the value of "{instructions[counter][1]}"')
        print('----> ', registers[instructions[counter][1]])
        played_sound.append(registers[instructions[counter][1]])
        counter += 1

    elif instructions[counter][0] == 'set':

        if instructions[counter][2].lstrip('-').isdigit() is False:
            print(f'"set {instructions[counter][1]} {instructions[counter][2]}" sets '
                  f'register "{instructions[counter][1]}" to the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][2]]
            counter += 1

        else:

            print(f'"set {instructions[counter][1]} {instructions[counter][2]}" sets '
                  f'register "{instructions[counter][1]}" to the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = int(instructions[counter][2])
            counter += 1

    elif instructions[counter][0] == 'add':
        if instructions[counter][2].lstrip('-').isdigit() is False:
            print(f'"add {instructions[counter][1]} {instructions[counter][2]}" increases '
                  f'register "{instructions[counter][1]}" by the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][1]] + registers[instructions[counter][2]]
            counter += 1
        else:

            print(f'"add {instructions[counter][1]} {instructions[counter][2]}" increases '
                  f'register "{instructions[counter][1]}" by the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][1]] + int(instructions[counter][2])
            counter += 1

    elif instructions[counter][0] == 'mul':

        if instructions[counter][2].lstrip('-').isdigit() is False:

            print(f'"mul {instructions[counter][1]} {instructions[counter][2]}" sets '
                  f'register "{instructions[counter][1]}" to the value of multiplying the value contained '
                  f'in register {instructions[counter][1]} by the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][1]] * registers[instructions[counter][2]]
            counter += 1
        else:

            print(f'"mul {instructions[counter][1]} {instructions[counter][2]}" sets '
                  f'register "{instructions[counter][1]}" to the value of multiplying the value contained '
                  f'in register {instructions[counter][1]} by the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][1]] * int(instructions[counter][2])
            counter += 1

    elif instructions[counter][0] == 'mod':
        if instructions[counter][2].lstrip('-').isdigit() is False:
            print(f'"mod {instructions[counter][1]} {instructions[counter][2]}" sets '
                  f'register "{instructions[counter][1]}" to the reminder of dividing the value contained '
                  f'in register {instructions[counter][1]} by the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][1]] % registers[instructions[counter][2]]
            counter += 1
        else:

            print(f'"mod {instructions[counter][1]} {instructions[counter][2]}" sets '
                  f'register "{instructions[counter][1]}" to the reminder of dividing the value contained '
                  f'in register {instructions[counter][1]} by the value of {instructions[counter][2]}')
            registers[instructions[counter][1]] = registers[instructions[counter][1]] % int(instructions[counter][2])
            counter += 1

    elif instructions[counter][0] == 'rcv':

        if registers[instructions[counter][1]] != 0:
            print(f'"rcv {instructions[counter][1]} " recovers of the last sound played, '
                  f'but only when the value of {instructions[counter][1]} is not zero.'
                  f' (If it is zero, the command does nothing.)')
            recovers.append([len(played_sound), played_sound[len(played_sound) - 1]])
            d = 1
        else:
            print('Not activated!')
            pass
        counter += 1

    elif instructions[counter][0] == 'jgz':

        if registers[instructions[counter][1]] != 0:
            print(f'"jgz {instructions[counter][1]} {instructions[counter][2]}" jumps '
                  f'with an offset of the value of {instructions[counter][2]},'
                  f' but only if the value of {instructions[counter][1]} is greater than zero')
            counter += int(instructions[counter][2])
            if counter > len(instructions):
                print('Finish')
                d = 1
            elif counter < 0:
                print('Finish')
                d = 1
            else:
                pass
        else:
            print('Not activated!')
            pass
            counter += 1

    return counter, recovers, d


def duet():

    f = open('instructions.txt').read()
    regex = r"(\w+) (\w+)( .+)?"
    global instructions, registers
    instructions = re.findall(regex, f)
    c = 0
    for i in instructions:
        instructions[c] = (instructions[c][0], instructions[c][1], str(instructions[c][2]).strip(' '))
        c += 1
    registers = {}
    i_counter = 0

    global recovers, played_sound
    recovers = []
    played_sound = []

    global x
    x = 0
    while i_counter < len(instructions):
        print('--------------------------------------------------------------')
        print('Iteration n.', x + 1)
        print('\nInstruction n.', i_counter, ' -----> ',  instructions[i_counter], '\n')
        i_counter, recovers, d = registers_engine(i_counter)
        x += 1
        print(registers)
        if d == 1:
            break
    print()
    for r in recovers:
        print(r)


if __name__ == '__main__':
    duet()
# Advent of Code - day 6 (Part II)
import numpy as np
import re
import time


def reallocation_routine(block):
    blocks_config = list(block)
    #  print('\n\nReallocation routine...\n')
    #  print('Current blocks configuration is:', blocks_config)
    max_block = max(blocks_config)
    max_position = blocks_config.index(max(blocks_config))
    #  print('Maximum bank blocks to allocate is:', max_block, ', identified in bank:', max_position)
    blocks_config[max_position] = 0  # empty the bank
    fill_bank = max_position + 1  # Start filling the bank after
    new_blocks_config = list(blocks_config)  # create a new list
    #  print('New banks blocks to fill are:', new_blocks_config)
    for c in np.arange(1, max_block + 1):

        if fill_bank >= len(new_blocks_config):
            fill_bank = 0
            new_blocks_config[fill_bank] = new_blocks_config[fill_bank] + 1
            fill_bank += 1
        else:
            new_blocks_config[fill_bank] = new_blocks_config[fill_bank] + 1
            fill_bank += 1
    # print('\n\nAllocation finished!!')
    # print('New bank blocks configuration is:', new_blocks_config)
    # print('--------------------------------------------------\n\n')

    return new_blocks_config


def check_debug(ordered_config, config, bug_n):

    bug_check = int(bug_n)

    for el in ordered_config:
        if el[1] == config:
            bug_check = 1
            break
        else:
            bug_check = 0
            pass
    return bug_check


def main():
    file = open('init_bank_blocks.txt')
    banks = [int(elm) for elm in re.findall(r'\d+', file.read())]
    print('\nThe are', len(banks), 'banks!')

    max_iteration = 100000
    step = 0
    configurations = [[step, list(banks)]]
    debug = 0
    bug_rep = 0
    start = time.time()
    repetitions = []
    n = 0
    for s in np.arange(1, max_iteration + 1):
        # print('---------------------')
        # print('\n##########  Step n', step)
        # print('Current config:', configurations[step][1])
        current_blocks_config = reallocation_routine(configurations[step][1])

        test_config = list(current_blocks_config)
        bug_res = check_debug(configurations, test_config, debug)
        if bug_res == 1:
            step += 1
            configurations.append([step, test_config])

            repetitions.append([step, list(test_config)])
            n += 1
        else:
            step += 1
            configurations.append([step, test_config])
            if s == max_iteration:
                stop = time.time()
                duration = stop - start
                print('\nTime to find the solution is:', duration, ' [s]')
                print('Reached maximum iteration step!! -->', max_iteration)
            else:
                pass
            pass

        if n > 1:

            bug_rep_check = check_debug(repetitions[1:], repetitions[0][1], bug_rep)
            if bug_rep_check == 1:
                stop = time.time()
                duration = stop - start
                print('\nTime to find the solution is:', duration, ' [s]')
                print('\n-----------------------------------------')
                print('Second loop detected after ----->', step - repetitions[0][0], 'steps')
                print('-----------------------------------------')
                print('First configuration repeated is:', test_config)
                break
            else:
                continue


if __name__ == '__main__':
    main()

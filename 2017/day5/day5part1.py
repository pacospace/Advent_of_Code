# Advent of Code - day 5 (Part I)
import numpy as np
import time


def main():

    file = open('jumps.py')

    jumps_list = [int(j) for j in file.read().split()]
    maze_len = len(jumps_list)
    max_step = 1000000
    gps_jump = 0  # Initial position in the maze

    start = time.time()
    for step in np.arange(0, max_step + 1):
        # print('---------------------------------')
        # print('\nNext position to consider in the list is:', gps_jump)
        # print('Maze positions are:', jumps_list)
        if 0 <= gps_jump < maze_len:
            current_gps_jump = gps_jump
            current_jump = jumps_list[gps_jump]
            # print('----------------------')
            # print('Jump n.', step)
            # print('The jump to perform is:', current_jump)
            gps_jump = gps_jump + current_jump

            # increment the instruction of 1
            jumps_list[current_gps_jump] = current_jump + 1
            # print('Modified Maze positions are:', jumps_list)
            # print("\nYou are still inside the maze, don't give up!!! Step n.----->", step)
            pass
        else:
            print('\n\n**********************************************')
            print('Well Done!!! You are out of the maze')
            print('\nNumber of steps to exit the maze is ------>', step)
            print('**********************************************')
            stop = time.time()
            duration = stop - start
            print('Time to find the solution is:', duration, ' [s]')
            break


if __name__ == '__main__':
    main()


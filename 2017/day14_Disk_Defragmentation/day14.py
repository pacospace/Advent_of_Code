# Advent of Code - day14 (Part I)
import math


def current_c(c_list, c_counter):

    d = math.floor(c_counter/len(c_list))
    c_new = c_counter - len(c_list)*d

    return c_new


def xor_result(xor_list):
    kn = xor_list
    r_kn = kn[0] ^ kn[1] ^ kn[2] ^ kn[3] ^ kn[4] ^ kn[5] ^ kn[6] ^ kn[7] ^ kn[8] ^ kn[9] ^ kn[10] ^ kn[11] ^ kn[12] ^ \
           kn[13] ^ kn[14] ^ kn[15]
    return r_kn


def d_hash(sp_hash):
    dn_hash = []

    for i in range(0, 256, 16):
        ken = sp_hash[i:i + 16]
        xor = xor_result(ken)
        dn_hash.append(xor)

    return dn_hash


def k_hash(d_h):
    knot_hash = ''
    for elx in d_h:
        knot_hash = knot_hash + str(format(elx, '02x'))
    return knot_hash


def knot_hash_f(input_str):
    circular_list = list(range(0, 256))

    input_lengths = []

    for each in input_str:
        input_lengths.append(ord(each))

    input_lengths = input_lengths + [17, 31, 73, 47, 23]
    c = 0
    skip_size = 0
    max_round = 64
    round = 1

    while round <= max_round:

        n = 0

        if len(circular_list) == 256:

            for il in input_lengths:

                c = current_c(circular_list, c)

                if c + il <= len(circular_list) - 1:

                    sublist = circular_list[c:c + il]
                    rev_sublist = list(sublist[::-1])
                    circular_list[c:c + il] = rev_sublist

                elif c + il > len(circular_list) - 1:

                    diff = c + il - len(circular_list)
                    sublist = circular_list[c:len(circular_list)] + circular_list[0: diff]
                    rev_sublist = list(sublist[::-1])
                    circular_list[c:len(circular_list)] = rev_sublist[0:len(circular_list) - c]
                    circular_list[0: diff] = rev_sublist[len(circular_list) - c: len(rev_sublist)]

                c = c + il + skip_size
                skip_size += 1
                n += 1

        round += 1

    sparse_hash = list(circular_list)
    dense_hash = d_hash(sparse_hash)
    knot_hash_r = k_hash(dense_hash)

    return knot_hash_r


def hex2bin(chain):
    return ''.join((bin(int(chain[i:i+2], 16))[2:].zfill(4) for i in range(0, len(chain), 2)))


def main():
    grid = []
    input_puzzle = 'wenycdww'
    for i in range(0, 128):
        kh = knot_hash_f(input_puzzle + '-' + str(i))
        b = (bin(int(kh, 16))[2:]).zfill(4)
        grid.append(list((128-b.__len__()) * "0" + b))

    cnt = [g.count("1") for g in grid]
    print('{} squares are used'.format(sum(cnt)))


if __name__ == '__main__':
    main()

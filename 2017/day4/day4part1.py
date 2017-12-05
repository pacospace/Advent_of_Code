# Advent of Code - day 4 (Part I)


def main():

    file = open('inputday4.txt')

    passphrases = file.read().split('\n')

    print()
    n_passphrase = 1
    n_not_valid_pass = 0
    for passphrase in passphrases:
        print('------------------')
        print('Passphrase n.', n_passphrase)
        print('Passphrase:', passphrase)
        current = passphrase.split()
        print()
        dict = {}
        l_checkold = 0
        for element in current:
            dict[element] = 1
            l_check = len(dict)
            if l_check == l_checkold:
                print("It's not a passphrase!!!")
                print(element, ' is already in the passphrase')
                n_not_valid_pass += 1
                break
            else:
                l_checkold = l_check

        n_passphrase += 1

    print('_______________________________________________')
    print('The total number of passphrase is --------->', n_passphrase - 1)
    print('_______________________________________________')
    print('The number of valid passphrase is --------->', (n_passphrase - 1) - n_not_valid_pass)
    print('_______________________________________________')
    print('The number of not valid passphrase is ----->', n_not_valid_pass)


if __name__ == '__main__':
    main()


# Advent of Code - day 4 (Part II)

file = open('inputday4.txt')

passphrases = file.read().split('\n')

print()
n_passphrase = 1
n_not_valid_pass = 0
for passphrase in passphrases:
    d = 0

    print('------------------')
    print()
    print('Passphrase n.', n_passphrase)
    print('Passphrase:', passphrase)
    print()
    print('------------------')
    print()
    current = passphrase.split()
    print()

    c = 0

    for element in current:
        if c < len(current) - 1:
            print()
            print('------------ Cheks n.1, step', c + 1)
            current_element = list(element)
            print('Current element:', element)

            current_new = current[0:c] + current[c + 1:len(current)]
            print('The elements to compare are:', current_new)

            alarm = 0
            e = 0
            for check_pass in current_new:
                if e <= len(current_new) - 1:
                    element_new = list(current_new[e])

                    if sorted(current_element) == sorted(element_new):
                        print("It's not a passphrase!!!")
                        print(current_element, 'and ', element_new, ' are anagrams')
                        n_not_valid_pass += 1
                        d = 1
                        alarm = 1
                        break
                    else:
                        alarm = 0
                        e += 1

            if alarm == 1:
                break
            else:
                print('Continue...')
                c += 1

    if d == 0:
        print()
        print("It's a possible passphrase, check n.1 passed\n")

        dict = {}
        l_checkold = 0
        for element in current:
            dict[element] = 1
            l_check = len(dict)

            # First check
            if l_check == l_checkold:
                print('Cheks n.2')
                print("It's not a passphrase!!!")
                print(element, ' is already in the passphrase')
                n_not_valid_pass += 1
                d = 1
                break
            else:
                l_checkold = l_check

        if d == 0:
            print("It's a passphrase, check n.1 and n.2 passed")
        else:
            print()
            print('Check n.2 failed')
            print()
            print()

    else:
        print()
        print('Check n.1 failed')
        print()
        print()

    n_passphrase += 1

print('_______________________________________________')
print('The total number of passphrase is --------->', n_passphrase - 1)
print('_______________________________________________')
print('The number of valid passphrase is --------->', (n_passphrase - 1) - n_not_valid_pass)
print('_______________________________________________')
print('The number of not valid passphrase is ----->', n_not_valid_pass)

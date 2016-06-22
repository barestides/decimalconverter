#!/usr/bin/python3.5

running = True

while running:
    run_option = int(input('What would you like to do?\n0:\t Quit\n1:\t Run part 1\n2:\t Run Part 2\n'))

    if run_option == 0:
        # Quit Program
        print('Quitting Program')
        running = False

    elif run_option == 1:
        # Part 1
        block1 = input('What is the first block of digits?\n')
        block2 = input('What is the second block of digits?\n')

        decimal = float('0.' + block1 + block2 + block2)
        print(str(decimal) + '...')

        n = len(block1)
        print(decimal * 10**n)

    elif run_option == 2:
        # Part 2
        integer = input('What is the integer to the left of the decimal point?\n')
        block1 = input('What is the first block of digits?\n')
        block2 = input('What is the second block of digits?\n')
        decimal = float(integer + '.' + block1 + block2 + block2)
        print('Your number:\t', decimal)

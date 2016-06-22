#!/usr/bin/python3.5
from fractions import Fraction


def convertToFraction(integer, first_block, repeating_block):
    number = float(integer + '.' + first_block + repeating_block)

    # Move the decimal point directly to the right, and to the left
    # then subtract equations:
    # decimalptright(x) - decimalptleft(x) =  decimalptright*num - decimalptleft*num

    decimal_pt_top = 10**(len(first_block) + len(repeating_block))
    decimal_pt_bottom = 10**len(first_block)

    left_side = decimal_pt_top - decimal_pt_bottom
    right_side = (decimal_pt_top*number) - (decimal_pt_bottom*number)

    print('num', number)
    print('Current num / dem', round(right_side), left_side)
    print(decimal_pt_top, decimal_pt_bottom)

    print(Fraction(round(right_side), int(left_side)))

    fraction = (right_side, left_side)
    return fraction


def main():
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

            fraction = convertToFraction('0', block1, block2)
            print('Fractional form: ', fraction[0], '/', fraction[1])

        elif run_option == 2:
            # Part 2
            integer = input('What is the integer to the left of the decimal point?\n')
            block1 = input('What is the first block of digits?\n')
            block2 = input('What is the second block of digits?\n')
            decimal = float(integer + '.' + block1 + block2 + block2)
            print('Your number:\t', decimal)

            fraction = convertToFraction(integer, block1, block2)
            print('Fractional form: ', fraction[0], '/', fraction[1])

main()


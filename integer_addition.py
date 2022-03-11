#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program adds two integers together


def main():
    # this function adds to integers together

    # input
    int1 = int(input("Enter the first number to add (integer): "))
    int2 = int(input("Enter the second number to add (integer): "))

    # process
    total = int1 + int2

    # output
    print("")
    print("{0} + {1}".format(int1, int2))
    print("")
    print("Your answer is {0:,.0f}".format(total))
    print("\nDone.")


if __name__ == "__main__":
    main()

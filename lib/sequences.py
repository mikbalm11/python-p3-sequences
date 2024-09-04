#!/usr/bin/env python3

def print_fibonacci(length):
    '''Prints the first 'length' Fibonacci numbers.'''
    fib_numbers = [0, 1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(fib_numbers)
    else:
        # recursively print the first 'length' Fibonacci numbers
        for numbers in range(2, length):
            fib_numbers.append(sum(fib_numbers[-2:]))
        print(fib_numbers)

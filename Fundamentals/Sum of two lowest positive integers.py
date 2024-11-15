'''
Create a function that returns the sum of the two lowest positive numbers
given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
'''


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


def sum_two_smallest_numbers1(numbers):
    return sum(sorted(numbers)[:2])
'''
Given two numbers and an arithmetic operator (the name of it, as a string),
return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation,
and b always the second.

The four operators are "add", "subtract", "divide", "multiply".
'''


def arithmetic(a, b, operator):
    if operator is 'add':
        return a + b
    elif operator is 'subtract':
        return a - b
    elif operator is 'divide':
        return a / b
    else:
        return a * b


def arithmetic1(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]


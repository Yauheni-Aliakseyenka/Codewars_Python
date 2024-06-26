'''
Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''
#def array_diff(a, b):

a = [1, 2, 3]
b = [1, 2]

def array_diff(a, b):
    new_a = []
    for i in a:
        if i not in b:
            new_a.append(i)
    return new_a

def array_diff1(a, b):
    return [x for x in a if x not in b]

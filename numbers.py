'''
Docstring for numbers
get n numbers and print the min, max, average and the sorted numbers.
'''

def minimum(*args):
    first = args[0]
    for i in args:
        if first > i:
            first = i
    return first

def maximum(*args):
    first = args[0]
    for i in args:
        if first < i:
            first = i
    return first

def average(*args):
    total = 0
    for i in args:
        total += i
    avg = total / len(args)
    return avg

def sort(*args):
    lst = list(args)

    for i in range(len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst



print(minimum(1, 2 ,3 ,4 ,5))
print(maximum(1, 2 ,3 ,4 ,5))
print(average(1, 2 ,3 ,4 ,5))
print(sort(5, 4 ,3 ,2 , 1))
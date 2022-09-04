from itertools import count


def sum(arr):
    #base 
    if arr == []:
        return 0
    #recursion
    else:
        store = arr[-1]
        arr.pop()
        return store + sum(arr)

print(sum([1,2,3,4]))

def howmany(arr):
    if arr == []:
        return 0
    else:
        arr.pop()
        return 1 + howmany(arr)

print(howmany([1,2,3,7,8,9]))


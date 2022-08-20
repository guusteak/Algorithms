def binary_search(list, item):
    low=0 #pierwszy indeks tablicy
    high = len(list)-1 #ostatni indeks tablicy

    while low <= high: 
        #elementy sie nie zrównały
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
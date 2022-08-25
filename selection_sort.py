def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    print(len(arr))
    print(arr)
    for i in range(len(arr)):
        #od 1 do len(arr) bo smallest jest ustawiony na  
        #indeks 0 
        print(i)
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))


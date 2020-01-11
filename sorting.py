def insertion_sort(arr, reverse):
    '''Quick sorting algorithm for small data.'''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if reverse:
            while j >= 0 and key > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        else:
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    return arr

'''sort tu lon den be bang cach cho parameter thu 2 la True'''
print(insertion_sort([14,5,7,4,1,4,9], True))
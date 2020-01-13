def insertion_sort(arr):
    '''Quick sorting algorithm for small data.'''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def simple_arr(array, x):
    insertion_sort(array)
    sumary = 0
    counter = 0
    for i in array:
        sumary += i
        if i == x:
            counter += 1
    biggest = array[-1]
    smallest = array[0]
    return "sum: %d | biggest: %d | smallest: %d | number of time x shows up: %d" % (sumary, biggest, smallest, counter)

array = input("enter numbers: ").split(",")
int_arr = []
for i in array:
    int_arr.append(int(i))
x = int(input("enter value x: "))
print(simple_arr(int_arr, x))
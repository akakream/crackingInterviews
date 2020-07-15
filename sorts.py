arr1 = [324,35,5,5,25,27,568,26, 0, 34275,8365,-23,34,-34,-5]


# BUBBLE SORT
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


# INSERTION SORT
def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]

        j = i-1 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


# SELECTION SORT
def selectionSort(arr):
    for i in range(len(arr)):

        smallest = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp


# MERGE SORT
def mergeSort(arr):
    if len(arr) == 1:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    sorted_left = mergeSort(left)
    sorted_right = mergeSort(right)

    return merge(sorted_left, sorted_right) 

def merge(left, right):
    
    r_l = list()
    i = 0
    j = 0

    while i != len(left) and j != len(right):
        if left[i] <= right[j]:
            r_l.append(left[i])
            i += 1
        else:
            r_l.append(right[j])
            j += 1

    while i < len(left):
        r_l.append(left[i])
        i += 1
    
    while j < len(right):
        r_l.append(right[j])
        j += 1

    return r_l 


# QUICK SORT
def quickSort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quickSort(arr, low, part-1)
        quickSort(arr, part+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1

    temp = arr[i]
    arr[i] = arr[high]
    arr[high] = temp

    return i

quickSort(arr1, 0, len(arr1)-1)
print(arr1)

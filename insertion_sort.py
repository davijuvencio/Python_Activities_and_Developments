import random

arr = random.sample(range(1, 101), 10)
print("Array desordenado:", arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("Insertion Sort:", arr)

insertion_sort(arr)
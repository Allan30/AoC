import random

l = list(range(10))
random.shuffle(l)


# sorting the first and last elements of an array.
def find_pviot_index(A, start, end):
    pivot = A[end]
    p_index = start
    for iter in range(start, end):
        if A[iter] <= pivot:
            A[p_index], A[iter] = A[iter], A[p_index]
            p_index += 1
    A[p_index], A[end] = pivot, A[p_index]
    return p_index


# main sorting function
def quick_sort(A, start, end):
    if start < end:
        pivot_index = find_pviot_index(A, start, end)
        quick_sort(A, start, pivot_index - 1)
        quick_sort(A, pivot_index + 1, end)


# Driver code
A = l
n = len(l)
print("Orignal array:", A)
quick_sort(A, 0, n - 1)
print("Sorted array :", A)

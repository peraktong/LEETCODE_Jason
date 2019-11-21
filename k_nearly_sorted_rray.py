# https://www.geeksforgeeks.org/nearly-sorted-algorithm/
# O(Nlogk)
def insertionSort(A, size):
    i, key, j = 0, 0, 0


for i in range(size):
    key = A[i]
    j = i - 1

    # Move elements of A[0..i-1], that are
    # greater than key, to one position
    # ahead of their current position.
    # This loop will run at most k times
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key
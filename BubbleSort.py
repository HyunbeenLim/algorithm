def Bubble_sort(arr):
    N = len(arr)

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

w = [55,7,78,12,42]
print(Bubble_sort(w))
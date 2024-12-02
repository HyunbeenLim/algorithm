def Selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j # 해당 구간 중 최소 값의 인덱스가 j가 됨
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


w = [1,3,4,6,2,3,4,6,1,3,4,6,7,3,5,6,9,2,5,2,5]
print(Selection_sort(w))

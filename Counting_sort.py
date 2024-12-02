def counting_sort(arr):
    n = len(arr)
    
    # 최대값
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    # 카운팅 배열
    counts = [0] * (max_value + 1)
    for ele in arr:
        counts[ele] += 1

    # 누적 합 배열//counts 배열에서 바로 수정해도 됨!
    adj_counts = [0] * (max_value + 1)
    adj_counts[0] = counts[0]

    for i in range(1, max_value + 1):
        adj_counts[i] = adj_counts[i - 1] + counts[i]
    
    # 정렬된 배열
    sorted_list = [0] * n
    for j in range(n - 1, -1, -1):  # 뒤에서 시작
        element = arr[j]
        adj_counts[element] -= 1
        sort_idx = adj_counts[element]
        sorted_list[sort_idx] = element

    return sorted_list

w = [0,3,5,4,1,7,3,5,8,11,0,1,3,4,4,14]
print(counting_sort(w))
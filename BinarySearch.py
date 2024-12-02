# 일반적인 이진 검색

def Binary_search(arr, key):
    # key는 찾고자 하는 값
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        idx_to_search = (end + start) // 2 # 몫
        if arr[idx_to_search] == key:
            return True # 인덱스 반환도 가능
        elif arr[idx_to_search] > key:
            end = idx_to_search - 1
        else:
            start = idx_to_search + 1
    return False


# 재귀 함수

def Binary_recur(arr, low, high, key):
    # low == start_idx, high == end_idx
    if low > high: # start > end
        return False
    else:
        idx_to_search = (low + high) // 2
        if key == arr[idx_to_search]:
            return True
        elif key < arr[idx_to_search]:
            return Binary_recur(arr, low, idx_to_search - 1, key)
        elif key > arr[idx_to_search]:
            return Binary_recur(arr, idx_to_search + 1, high, key)
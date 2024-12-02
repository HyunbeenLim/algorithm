import sys
sys.stdin = open('./sample_input.txt', 'r')

def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]
    arr[left], arr[mid] = arr[mid], arr[left]

    i = left + 1
    j = right

    while i <= j:
        # 피봇보다 작은 것들 왼쪽으로
        while i <= j and arr[i] <= pivot:
            i += 1
        # 큰 것들 오른쪽으로
        while i <= j and arr[j] >= pivot:
            j -= 1
        # i, j가 만나기 전에 while 문을 탈출했다 => arr[i]가 pivot 보다 크고 arr[j]가 pivot보다 작다
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # 피봇 업데이트
    arr[left], arr[j] = arr[j], arr[left]

    return j

def quick_sort(left, right):
    # 정렬이 될 때까지
    if left < right:
        pivot = hoare_partition3(left, right)
        # pivot 기준 분할
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N-1)

    print(f'#{tc} {arr[N//2]}')

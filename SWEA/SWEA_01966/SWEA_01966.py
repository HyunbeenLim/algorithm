def bubble_sort(arr):
    n = len(arr)
    for i in range((n - 1), 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    number_list = list(map(int, input().split()))

    sorted_list = bubble_sort(number_list)

    print(f'#{tc}', *sorted_list)
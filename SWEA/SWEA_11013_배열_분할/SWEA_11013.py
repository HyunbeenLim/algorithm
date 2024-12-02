import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11013_배열_분할/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    minimum_diff = float('inf')

    for i in range(1, N-1):
        for j in range(i + 1, N):
            sum_list = []
            # 3분할
            split = [arr[:i], arr[i:j], arr[j:]]
            # 각각의 합 구하기
            for frac in split:
                sum_value = 0
                for num in frac:
                    sum_value += num
                sum_list.append(sum_value)
            # 최대 최소 구하기
            max_sum = sum_list[0]
            min_sum = sum_list[0]
            for idx in range(1, 3):
                if sum_list[idx] > max_sum:
                    max_sum = sum_list[idx]
                elif sum_list[idx] < min_sum:
                    min_sum = sum_list[idx]
            # 최대 - 최소의 최솟값
            diff = max_sum - min_sum
            if diff < minimum_diff:
                minimum_diff = diff

    print(f'#{tc} {minimum_diff}')

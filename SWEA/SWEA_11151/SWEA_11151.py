T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    number_list = list(map(int, input().split()))

    max_sum = number_list[0] + number_list[1]
    for i in range(1, n - 1):
        two_sum = number_list[i] + number_list[i + 1]
        if two_sum > max_sum:
            max_sum = two_sum

    print(f'#{tc} {max_sum}')
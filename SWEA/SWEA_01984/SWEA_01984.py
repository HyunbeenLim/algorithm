T = int(input())

for tc in range(1, T + 1):
    n_list = list(map(int, input().split()))

    n_list.remove(max(n_list))
    n_list.remove(min(n_list))

    mean_value = int()
    for i in range(len(n_list)):
        mean_value += n_list[i]
    mean_value = round(mean_value / len(n_list))

    print(f'#{tc} {mean_value}')
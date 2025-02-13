import copy

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input())

    for i in range(1, N + 1):
        new_list = [1] * i
        if len(new_list) == 1 or len(new_list) == 2:
            print(*new_list)
        else:
            for j in range((len(old_list) - 1)):
                new_list[j + 1] = old_list[j] + old_list[j + 1]
            print(*new_list)

        old_list = copy.deepcopy(new_list)
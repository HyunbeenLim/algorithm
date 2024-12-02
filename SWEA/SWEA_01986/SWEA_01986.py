T = int(input())

for test_case in range(1, T + 1):
    num_list = list(range(1, int(input()) + 1))
    zig_sum = int()

    for i in range(len(num_list)):
        number = num_list[i]
        if number % 2 == 1:
            zig_sum += number
        else:
            zig_sum -= number
    print(f'#{test_case} {zig_sum}')
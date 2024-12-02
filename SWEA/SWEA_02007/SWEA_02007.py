T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    input_string = input()

    for i in range(2, 11):
        if input_string[0:(i - 1)] == input_string[i:(2 * i - 1)]:
            print(i)
            break
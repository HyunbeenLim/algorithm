N = int(input())

for i in range(1, N + 1):
    count = 0
    num = str(i)

    for n in num:
        if n == '3' or n == '6' or n == '9':
            count += 1
    if count > 0:
        print('-' * count, end='')
    else:
        print(num, end='')
    print(' ', end='')
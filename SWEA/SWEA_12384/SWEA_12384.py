'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_value = num_list[0]
    min_value = num_list[0]

    for i in range(1, len(num_list)):
        if num_list[i] > max_value:
            max_value = num_list[i]
        elif num_list[i] < min_value:
            min_value = num_list[i]

    print(f'#{tc} {max_value - min_value}')
import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_01989/input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    r_string = string[::-1]

    judge = int()

    if string == r_string:
        judge = 1
    else:
        judge = 0

    print(f'#{test_case} {judge}')
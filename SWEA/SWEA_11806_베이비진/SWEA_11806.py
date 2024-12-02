import sys
sys.stdin = open('./sample_input.txt', 'r')

def check(arr1:list, arr2:list):
    arr1.sort()
    arr2.sort()

    ans = 0
    tri_cnt_1 = 1
    run_cnt_1 = 1
    tri_cnt_2 = 1
    run_cnt_2 = 1

    for i in range(len(arr1) - 1):
        if arr1[i] == arr1[i+1]:
            tri_cnt_1 += 1
        else:
            tri_cnt_1 = 1
            if arr1[i] + 1 == arr1[i+1]:
                run_cnt_1 += 1
            else:
                run_cnt_1 = 1

        if tri_cnt_1 >= 3 or run_cnt_1 >= 3:
            return '1'

    for i in range(len(arr2) - 1):
        if arr2[i] == arr2[i+1]:
            tri_cnt_2 += 1
        else:
            tri_cnt_2 = 1
            if arr2[i] + 1 == arr2[i+1]:
                run_cnt_2 += 1
            else:
                run_cnt_2 = 1

        if tri_cnt_2 >= 3 or run_cnt_2 >= 3:
            return '2'

    return ans

T = int(input())

for tc in range(1, T + 1):
    cards = [0] + list(map(int, input().split()))
    N = 12

    p1 = []
    p2 = []

    for i in range(1, N, 2):
        p1.append(cards[i])
        p2.append(cards[i+1])
        if len(p1) >= 3:
            ans = check(p1, p2)
            if ans:
                print(f'#{tc} {ans}')
                break
    else:
        print(f'#{tc} {ans}')
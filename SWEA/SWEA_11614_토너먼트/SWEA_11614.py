import sys
sys.stdin = open('sample_input.txt', 'r')

def find_min(s, e):
    # 중단
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lidx = find_min(s, mid)
        ridx = find_min(mid + 1, e)
        if arr[lidx] == arr[ridx]:
            return min(lidx, ridx)
        elif abs(arr[lidx] - arr[ridx]) == 1:
            return max(lidx, ridx)
        else:
            return min(lidx, ridx)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ret = find_min(0, N - 1)
    print(f'#{tc} {ret}')

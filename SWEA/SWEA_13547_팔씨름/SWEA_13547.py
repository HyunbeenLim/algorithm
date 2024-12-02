import sys
sys.stdin = open('sample_lnput.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n = 15
    string = input()
    k = len(string)
    left_games = n - k

    win_count = 0

    for s in string:
        if s == 'o':
            win_count += 1
    
    ans = 'YES'
    if left_games < 8 - win_count:
        ans = 'NO'

    print(f'#{tc} {ans}')
    
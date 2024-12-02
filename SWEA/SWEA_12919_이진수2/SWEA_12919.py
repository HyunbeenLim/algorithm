import sys
sys.stdin = open('./sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    number = float(input())
    
    cnt = 0
    ans = ''
    while number != 0:
        cnt -= 1
        check = 2 ** cnt
        
        if number >= check:
            ans += '1'
            number -= check
        else:
            ans += '0'
        
        if cnt < -12:
            print(f'#{tc} overflow')
            break
    else:
        print(f'#{tc} {ans}')
        

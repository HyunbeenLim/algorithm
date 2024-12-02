import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    length = int(input())
    
    if length % 2 == 0:
        print(f'#{tc} {"Alice"}')
    else:
        print(f'#{tc} {"Bob"}')
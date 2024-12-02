import sys
sys.stdin = open('./1_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    string = list(input())
    string.sort()
    
    str_dict = {}
    
    for frac in string:
        if frac not in str_dict:
            str_dict[frac] = 1
        else:
            str_dict[frac] += 1
    
    ans = ''
    
    for k, v in str_dict.items():
        if v % 2 == 1:
            ans += k
    
    if ans:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} Good')
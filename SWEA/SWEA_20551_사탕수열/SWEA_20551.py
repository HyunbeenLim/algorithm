import sys
sys.stdin = open('./sample_input.txt', 'r')

def number_to_eat():
    cnt = 0
    # 안되면 -1
    if (candies[2] <= 2) or (candies[1] <= 1):
        return -1
    
    # b 조작
    if candies[1] >= candies[2]:
        b_temp = candies[2] - 1
        cnt += candies[1] - b_temp
        candies[1] = b_temp
    
    # a 조작
    if candies[0] >= candies[1]:
        a_temp = candies[1] - 1
        cnt += candies[0] - a_temp
        candies[0] = a_temp
    
    return cnt
            
        
        

T = int(input())

for tc in range(1, T + 1):
    candies = list(map(int, input().split()))
    ans = number_to_eat()
    
    print(f'#{tc} {ans}')
    
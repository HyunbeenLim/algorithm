import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_01231_중위순회/input.txt', 'r')

def inorder(v):
    global str_to_print
    if v == 0: return
    
    inorder(left[v])
    str_to_print += alphabet[v]
    inorder(right[v])

for tc in range(1, 11):
    N = int(input())
    
    alphabet = [0] * (N + 1)
    left = [0] * (N + 1)
    right =[0] * (N + 1)
    
    for _ in range(N):
        temp = list(input().split())
        alphabet[int(temp[0])] = temp[1]
        
        if len(temp) >= 3:
            left[int(temp[0])] = int(temp[2])
            if len(temp) == 4:
                right[int(temp[0])] = int(temp[3])
    
    str_to_print = ''
    inorder(1)
    
    print(f'#{tc} {str_to_print}')
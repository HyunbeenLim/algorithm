import sys
sys.stdin = open('./input.txt', 'r')

code_dict = {
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9'
}

# 올바른 암호인지 확인하자
def code_vailidity(lst:list):
    # 홀수 자리 합
    odd_sum = 0
    # 짝수 자리 합
    even_sum = 0
    
    for idx in range(1, 9):
        if idx % 2 == 0:
            even_sum += lst[idx]
        else:
            odd_sum += lst[idx]
    
    # 올바른 암호면 합 return
    if (odd_sum * 3 + even_sum) % 10 == 0:
        return odd_sum + even_sum
    # 아니면 0
    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    # 인덱스 쓰기 편하게 하자
    code_list = [0]
    
    # 일단 1이 있는 행 찾기
    for r in range(N):
        if '1' in matrix[r]:
            break
            
    # 암호 찾는 배열
    code_inc = matrix[r]
    
    # 암호가 끝나는 컬럼 인덱스 찾기
    for c in range(M - 1, -1, -1):
        if code_inc[c] == '1':
            break
    
    # 암호가 속한 배열만 뽑아보자
    code_inc = code_inc[(c - 55):(c + 1)]
    
    # 암호 넣자
    for start_idx in range(0, len(code_inc), 7):
        code_digit = ''
        for digit in code_inc[start_idx:(start_idx + 7)]:
            code_digit += digit
        if code_digit in code_dict:
            # 암호 리스트 완성
            code_list.append(int(code_dict[code_digit]))
    
    ans = code_vailidity(code_list)
    
    print(f'#{tc} {ans}')
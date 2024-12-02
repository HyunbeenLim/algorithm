import sys
sys.stdin = open('./sample_input.txt', 'r')




## 실습문제
# 16진수 문자열 => 2진수 문자열 변환
# 1. 16개의 숫자에 대한 2진수 표현을 dict로 저장해서 사용
hex_dict = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

T = int(input())

for tc in range(1, T + 1):
    n, hex_str = input().split()
    ans = ''
    for h in hex_str:
        ans += hex_dict[h]

    print(f'#{tc} {ans}')

# # 2. 16진수 한자리를 정수로 변환
# ans = []
# for ch in hex_str:
#     num = int(ch, 16)
#     # num의 하위 4개의 비트를 조사
#     ans.append('1' if num & 8 else '0')     # num & (1 << 3)
#     ans.append('1' if num & 4 else '0')    # num & (1 << 2)
#     ans.append('1' if num & 2 else '0')   # num & (1 << 1)
#     ans.append('1' if num & 1 else '0')   # num & (1 << 0)

# print(''.join(ans))
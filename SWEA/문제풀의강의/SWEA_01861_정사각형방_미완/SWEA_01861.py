import sys
sys.stdin = open('./input.txt', 'r')

## 접근 방법
'''
1.
모든 방에서 출발해 최대한 이동해 본다 
-> 얘는 시간이 오래 걸릴 것이다

2.
1) 1부터 N**2을 인덱스로 갖는 배열 A를 만든다
2) 숫자 i의 인접에 1 큰 수가 있는 경우 A[i]에 1을 표시한다.
3) 연속한 1의 개수가 최대인 경우를 찾는다.
'''
# visited = [0] * (N * N + 1)   하는 이유 생각해보자




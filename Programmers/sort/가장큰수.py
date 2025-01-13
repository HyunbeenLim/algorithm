from functools import cmp_to_key

def solution(numbers):
    # 비교 함수 정의
    def compare(a, b):
        if a + b > b + a:
            return -1  # a가 b보다 앞에 와야 함
        elif a + b < b + a:
            return 1   # b가 a보다 앞에 와야 함
        else:
            return 0   # 순서 변경 없음
    
    # 숫자를 문자열로 변환 후 정렬
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 결과를 이어 붙임
    result = ''.join(numbers)
    
    # "0"이 여러 개 있는 경우 처리
    return result if result[0] != "0" else "0"

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
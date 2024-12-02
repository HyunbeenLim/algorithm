# 백준_스위치 켜고 끄기

# 0 = off, 1 = on

# 남학생 = 받은 수의 배수들의 스위치들을 온오프한다.
# 즉, 스위치가 켜져있으면 끄고, 켜져있으면 끈다.

# 여학생 = 받은 수의 스위치를 중심으로 좌우가 대칭이면 스위치를 바꾸고
# 1) 받은 수가 다르면 스위치 바꾸고 아니면 그대로
# 2) 받은 수 중심으로 좌우 대칭이면 스위치 바꾸기, 아니면 그대로

#스위치 개수 (0<N<=100)
N = int(input())
# 스위치의 상태
    # 받은 넘버 자체를 인덱스 숫자로 받으면 안되지! 인덱스가 0일때 문제가 생기니까
    # arr 앞에 0번 인덱스를 추가해주기 -> num == idx

arr = list(map(int, input().split()))
arr = [0] + arr
on = 1
off = 0
op = [1,0]
# 학생수
stu = int(input())
for _ in range(stu):
    # gender ; 1 = man 2 = woman
    gender, num = map(int,input().split())
    
    # 남학생일때
    if gender == 1:
        for s in range(num, N+1, num):
            arr[s] = op[arr[s]]
    else:
        arr[num] = op[arr[num]]
        for i in range(1, N+1):
            if 1<=num-i and num+i<N+1 and arr[num-i] == arr[num+i]:
                arr[num-i] = op[arr[num-i]]
                arr[num+i] = op[arr[num+i]]
            else:
                break
        


# print(arr[1:])

# for i in range(1, N+1):
#     print(arr[i], end = " ")
#     if i % 20 == 0:
#         print()

for i in range(1, len(arr), 20):
    line = arr[i:i+20]
    print(' '.join(map(str,line)))




# if N >20:
#     for i in range(1, N+1, 20):
#         print(*arr[i:i+20])
# else:
#     print(*arr[1:])``
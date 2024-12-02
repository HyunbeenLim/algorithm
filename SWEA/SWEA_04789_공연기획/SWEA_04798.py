import sys
sys.stdin = open('./sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    people = [0] + list(map(int, input()))
    N = len(people)

    clap_cnt = people[1]                            # 박수치는 사람 수 
    people_emp = 0                                  # 고용할 사람 수
    for i in range(2, N):
        if people[i] != 0:                  
            if clap_cnt < (i-1):
                people_emp += (i-1 - clap_cnt)
                clap_cnt += (i-1 - clap_cnt + people[i])
            else:
                clap_cnt += people[i]
        
    print(f'#{tc} {people_emp}')

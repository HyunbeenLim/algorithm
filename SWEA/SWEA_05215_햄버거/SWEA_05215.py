import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_05215_햄버거/sample_input.txt', 'r')

def best_hamburger(idx, score, kcal):
    global max_score
    
    # 1000 넘으면 안해
    if kcal > limit:
        return
    # 1000 이하고, 최대면 업데이트
    if score > max_score:
        max_score = score
    # N까지 다 돌면 안해
    if idx == N:
        return
    
    # 재료 선택하고 점수, 칼로리 업데이트
    best_hamburger(idx + 1, score + ingredient[idx][0], kcal + ingredient[idx][1])
    # 선택 안하고 다음 재료로 넘어가기
    best_hamburger(idx + 1, score, kcal)

T = int(input())

for tc in range(1, T + 1):
    N, limit = map(int, input().split())
    
    ingredient = []
    
    for _ in range(N):
        # 점수, 칼로리
        ingredient.append(list(map(int, input().split())))
    
    max_score = 0
    best_hamburger(0, 0, 0)
    
    print(f'#{tc} {max_score}')
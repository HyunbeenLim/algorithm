def solution(genres, plays):
    songs = len(plays)
    cnt_dict = dict()

    # 장르 별 전체 재생 수, 음악과 음악의 재생 수 저장
    for i in range(songs):
        try:
            cnt_dict[genres[i]][0] += plays[i]
            cnt_dict[genres[i]].append([i, plays[i]])
        except KeyError:
            cnt_dict[genres[i]] = [plays[i], [i, plays[i]]]

    total_played = []
    for key in cnt_dict.keys():
        total_played.append([key, cnt_dict[key][0]])
    # 재생 수 정렬
    total_played = sorted(total_played, key=lambda x:x[1], reverse=True)

    ans = []
    for frac in total_played:
        genre = frac[0]
        genre_lst = cnt_dict[genre][1:]
        genre_lst = sorted(genre_lst, key=lambda x:x[1], reverse=True)
        # 장르 별 노래가 하나만 있을 수도 있음
        for i in range(min(2, len(genre_lst))):
            ans.append(genre_lst[i][0])

    return ans


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]
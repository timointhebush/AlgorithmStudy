def solution(genres, plays):
    answer = []
    genre_play = {}
    genre_num = {}
    for i, genre in enumerate(genres):
        if genre not in genre_play:
            genre_play[genre] = plays[i]
            genre_num[genre] = {i:plays[i]}
        else:
            genre_play[genre] += plays[i]
            genre_num[genre][i] = plays[i]
    genre_play = dict(sorted(genre_play.items(), reverse=True, key=lambda item: item[1]))
    for genre in genre_num:
        genre_num[genre] = dict(sorted(genre_num[genre].items(), reverse=True, key=lambda item: (item[1], -item[0])))
    print(genre_num)
    for genre in genre_play:
        tmp = []
        for idx in genre_num[genre]:
            tmp.append(idx)
            if len(tmp) == 2:
                break
        answer.extend(tmp)
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 500, 500, 2500]))
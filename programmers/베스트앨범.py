from collections import defaultdict


def solution(genres, plays):
    genre_cnt = defaultdict(int)
    genre_songs = defaultdict(list)
    for i in range(len(genres)):  # O(n)
        genre = genres[i]
        genre_cnt[genre] += plays[i]
        genre_songs[genre].append((plays[i], i))
    answer = []
    while len(genre_cnt) != 0:
        genre = find_most_played_genre(genre_cnt)
        songs = genre_songs[genre]
        songs = sorted(songs, key=lambda x: (x[0], -x[1]), reverse=True)
        print("songs: ", songs)
        answer.append(songs[0][1])
        if len(songs) >= 2:
            answer.append(songs[1][1])
    return answer


def find_most_played_genre(genre_cnt):
    most_cnt = -1
    most_genre = None
    for genre in genre_cnt.keys():
        if genre_cnt[genre] > most_cnt:
            most_cnt = genre_cnt[genre]
            most_genre = genre
    if most_genre != None:
        del genre_cnt[most_genre]
    return most_genre


print(solution(["classic", "classic"], [100, 100]))

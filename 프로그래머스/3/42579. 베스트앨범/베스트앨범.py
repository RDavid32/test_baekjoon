def solution(genres, plays):
    genre_total = {}
    songs = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play
        songs.setdefault(genre, []).append((play, idx))

    answer = []

    for genre in sorted(genre_total, key=genre_total.get, reverse=True):

        songs[genre].sort(key=lambda x: (-x[0], x[1]))

        for play, idx in songs[genre][:2]:
            answer.append(idx)

    return answer
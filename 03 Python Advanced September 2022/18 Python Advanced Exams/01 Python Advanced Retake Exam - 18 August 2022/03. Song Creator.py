def add_songs(*args):
    songs_dict = {}
    result = ''
    for element in args:
        song, lyrics = element
        if song in songs_dict:
            songs_dict[song] += lyrics
        else:
            songs_dict[song] = lyrics
    for song, lyrics in songs_dict.items():
        result += f"- {song}\n"
        if lyrics:
            for line in lyrics:
                result += f"{line}\n"
    return result
#1
def create_playlist (playlist_name: str, *songs: str) -> dict:
    playlist: dict = {playlist_name: {*songs}}
    return playlist
playlist1: str = 'play1'
song1: str = 's1'
song2: str = 's2'
playlist2: str = 'play2'
song3: str = 's3'
print(create_playlist(playlist1, song1, song2))
print(create_playlist(playlist2, song3))
def add_like(playlist: dict, playlist_name: str, whether: bool):
    
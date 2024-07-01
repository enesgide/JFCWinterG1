import os


class MediaPlayerModel:
    def __init__(self):
        self.songs = []
        self.current_song = ''
        self.is_paused = False

    def add_songs_from_dir(self, dir):
        self.songs.clear()
        for song in os.listdir(dir):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                self.songs.append(song)

    def get_songs(self):
        return self.songs

    def set_current_song(self, cur):
        self.current_song = cur

    def get_current_song(self):
        return self.current_song

class MusicLibrary():
    def __init__(self):
        self.music_library = []
    def list_tracks(self):
        if not self.music_library:
            raise Exception('Error: Library currently empty')
        return list(self.music_library)
    def add(self, track_name):
        if track_name == '':
            raise Exception('Error: Song name invalid')
        else:
            self.music_library.append(track_name)
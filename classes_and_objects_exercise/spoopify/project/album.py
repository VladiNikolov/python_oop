from project.song import Song

class Album:
    def __init__(self, name: str, *song):
        self.name = name
        self.published = False
        self.songs = []

        for s in song:
            self.songs.append(s)

    def add_song(self, song: Song):

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."


        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        else:
            return "Song is already in the album."


    def remove_song(self, song_name: str):

        if self.published:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."


    def publish(self):

        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):

        result = [f"Album {self.name}"]
        [result.append(s.get_info()) for s in self.songs]
        return "\n".join(result)






from playsound import playsound
import os

class MusicPlayer:
    def __init__(self):
        folder = "music/sample_tracks"
        self.tracks = [os.path.join(folder, f) for f in os.listdir(folder)
                       if f.endswith(".wav")]
        if not self.tracks:
            raise Exception("Нет WAV файлов в music/sample_tracks!")

        self.current = 0

    def play(self):
        playsound(self.tracks[self.current], block=False)

    def stop(self):
        # playsound не умеет стоп, оставим как заглушку
        pass

    def next(self):
        self.current = (self.current + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.current = (self.current - 1) % len(self.tracks)
        self.play()

    def current_track_name(self):
        return os.path.basename(self.tracks[self.current])
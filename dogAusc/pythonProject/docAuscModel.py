import os


class dogAuscModel:
    def __init__(self):
        self.s1_audio = None
        self.s2_audio = None
        self.s3_audio = None
        self.s4_audio = None

    def set_s1(self, audio):
        self.s1_audio = audio

    def set_s2(self, audio):
        self.s2_audio = audio

    def set_s3(self, audio):
        self.s3_audio = audio

    def set_s4(self, audio):
        self.s4_audio = audio

    def get_s1(self):
        return self.s1_audio

    def get_s2(self):
        return self.s2_audio

    def get_s3(self):
        return self.s3_audio
    
    def get_s4(self):
        return self.s4_audio




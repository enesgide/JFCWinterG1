import os
from tkinter import filedialog

class PopupController:
    def __init__(self, main_window, popup, model) -> None:
        self.main_window = main_window
        self.popup = popup
        self.model = model

        self.heart_choice = None
        self.lung_choice = None

    def select_audio(self):
        file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac")])

        if file_path:
            # use basename for label in popup, abspath for model attribute so pygame can play it
            return file_path

    def setHeartAudio(self):
        self.heart_choice = self.select_audio()
        if self.heart_choice is not None:
            self.popup.heart_label.configure(text=f"Heart audio file: {os.path.basename(self.heart_choice)}")
        else:
            self.popup.heart_label.configure(text="Heart audio file: None")
    
    def setLungAudio(self):
        self.lung_choice = self.select_audio()
        if self.lung_choice is not None:
            self.popup.lung_label.configure(text=f"Lung audio file: {os.path.basename(self.lung_choice)}")
        else:
            self.popup.lung_label.configure(text="Lung audio file: None")

    def confirm(self):
        #only works if you set both audio files
        if self.heart_choice != None or self.lung_choice != None:
            self.model.set_s1(os.path.abspath(self.heart_choice))
            self.model.set_s2(os.path.abspath(self.lung_choice))

            self.main_window.heart_label.configure(text=f"Heart audio file: {os.path.basename(self.heart_choice)}")
            self.main_window.lung_label.configure(text=f"Lung audio file: {os.path.basename(self.lung_choice)}")
            self.main_window.main_label.configure(text=f"Current active profile: Custom")
            self.popup.destroy()
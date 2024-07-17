import os
from tkinter import filedialog

# Controller class for the Popup view, which updates the popup, main window, and model classes based on user actions
class PopupController:

    # __init__(self, main_window, popup, model)
    # initialises the popup controller, setting the main window/popup view, and model as class attributes, as well as creating attributes for the apex/non-apex audio file paths

    # params:
    # self = the class instance
    # main_window = instance of the DogAuscView class
    # popup = instance of the DogAuscPopup class
    # model = instance of the DogAuscModel class

    # returns: None

    def __init__(self, main_window, popup, model):
        self.main_window = main_window
        self.popup = popup
        self.model = model

        self.apex_choice = None
        self.non_apex_choice = None
    
    # select_audio(self)
    # opens a filedialog that returns the path to an audio file selected

    # params:
    # self = the class instance

    # returns: file_path, the path to an audio file as a String

    def select_audio(self):
        file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac")])

        if file_path:
            # use basename for label in popup, abspath for model attribute so pygame can play it
            return file_path
        
    # setApexAudio(self)
    # sets the file path choice for the apex audio to the class attribute, as well as reflecting the selection on the popup view

    # params:
    # self = the class instance

    # returns: None

    def setApexAudio(self):
        self.apex_choice = self.select_audio()
        if self.apex_choice is not None:
            self.popup.apex_label.configure(text=f"Apex audio file: {os.path.basename(self.apex_choice)}")
        else:
            self.popup.apex_label.configure(text="Apex audio file: None")

    # setNonApexAudio(self)
    # sets the file path choice for the non apex audio to the class attribute, as well as reflecting the selection on the popup view

    # params:
    # self = the class instance

    # returns: None
    
    def setNonApexAudio(self):
        self.non_apex_choice = self.select_audio()
        if self.non_apex_choice is not None:
            self.popup.non_apex_label.configure(text=f"Non apex audio file: {os.path.basename(self.non_apex_choice)}")
        else:
            self.popup.non_apex_label.configure(text="Non apex audio file: None")

    # confirm(self)
    # confirms the choices by setting the the model's s1 and s2 attributes to the apex and non apex choices, as well as updating the main window view's audio file labels to the choices.

    # params:
    # self = the class instance

    # returns: None
    
    def confirm(self):
        #only works if you set both audio files
        if self.apex_choice != None or self.non_apex_choice != None:
            self.model.set_s1(os.path.abspath(self.apex_choice))
            self.model.set_s2(os.path.abspath(self.non_apex_choice))

            self.main_window.apex_label.configure(text=f"Heart audio file: {os.path.basename(self.apex_choice)}")
            self.main_window.non_apex_label.configure(text=f"Lung audio file: {os.path.basename(self.non_apex_choice)}")
            self.popup.destroy()
        else:
            return
import customtkinter
from tkinter import Toplevel

# class that represents the View for the Popup window, which handles file loading UI
class DogAuscPopup:

    # __init__(self, app)
    # initialises the popup class, setting dimensions based on the base App's dimensions

    # params:
    # self = the class instance
    # app = the instance of the base App

    # returns: None

    def __init__(self, app) -> None:
        self.popup = Toplevel()
        self.popup.title("Select Files")
        self.popup.geometry("800x400")
        self.controller = None
        self.popup.configure(bg="#292929")

        # calculate the position for centering the popup
        main_x = app.get_omni().winfo_rootx()
        main_y = app.get_omni().winfo_rooty()

        win_x = main_x + 100
        win_y = main_y + 100

        self.popup.geometry(f'+{win_x}+{win_y}')

        # Make the popup transient and modal
        self.popup.grab_set()
    
        # Ensure the popup gets focus
        self.popup.focus_set()

    # set_controller(self, controller)
    # method used to set the controller on view initialisation

    # params:
    # self = the class instance
    # controller = the instance of the DogAuscController class 

    # returns: None

    def set_controller(self, controller):
        self.controller = controller


    # init_popup(self)
    # initialises the GUI elements for the popup

    # params:
    # self = the class instance

    # returns: None

    def init_popup(self):

        # configures the frame area into weighted rows and columns as a grid where other components can be placed
        self.popup.columnconfigure(0, weight=1)
        self.popup.columnconfigure(1, weight=1)
        self.popup.columnconfigure(2, weight=1)

        self.popup.rowconfigure(0, weight=1)
        self.popup.rowconfigure(1, weight=1)

        ins_label = customtkinter.CTkLabel(master=self.popup, text = "Please set your audio:\n(Remember to select both files before confirming!)", font=("Bahnschrift", 16))
        ins_label.grid(row=0, column=0, columnspan = 3, pady = 10, sticky='new')

        self.apex_label = customtkinter.CTkLabel(master=self.popup, text = "Apex audio file: Not set", font=("Bahnschrift", 16))
        self.apex_label.grid(row=0, column=0, sticky="ew")

        apex_button = customtkinter.CTkButton(master=self.popup, text='Select file', command=self.controller.setApexAudio, font=("Bahnschrift", 14))
        apex_button.grid(row=0, column=1, padx=2, pady=2)

        self.non_apex_label = customtkinter.CTkLabel(master=self.popup, text = "Non apex audio file: Not set", font=("Bahnschrift", 16))
        self.non_apex_label.grid(row=0, column=0, sticky="sew")

        non_apex_button = customtkinter.CTkButton(master=self.popup, text='Select file', command=self.controller.setNonApexAudio, font=("Bahnschrift", 14))
        non_apex_button.grid(row=0, column=1, padx=2, pady=2, sticky="s")

        confirm = customtkinter.CTkButton(self.popup, text="Confirm", command=self.controller.confirm, font=("Bahnschrift", 14))
        confirm.grid(row=1, column = 0)

        close_button = customtkinter.CTkButton(self.popup, text="Close", command=self.popup.destroy, font=("Bahnschrift", 14))
        close_button.grid(row=1, column=2)

    # destroy(self)
    # destroys the popup window

    # params:
    # self = the class instance

    # returns: None
    
    def destroy(self):
        self.popup.destroy()

    

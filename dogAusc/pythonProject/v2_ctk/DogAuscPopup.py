import customtkinter

class DogAuscPopup:
    def __init__(self, app) -> None:
        self.popup = customtkinter.CTkToplevel(fg_color="#B9CFD4")
        self.popup.title("Select Files")
        self.popup.geometry("600x400")
        self.controller = None

        # calculate the position for centering the popup
        main_x = app.get_omni().winfo_rootx()
        main_y = app.get_omni().winfo_rooty()

        win_x = main_x + 100
        win_y = main_y + 100


        self.popup.geometry(f'+{win_x}+{win_y}')

        # bring popup to front
        self.popup.lift()

        # set focus to popup
        self.popup.focus_set()

        # ensure user is unable to interact with main window
        self.popup.grab_set()

    def set_controller(self, controller):
        self.controller = controller

    def init_popup(self):
        self.popup.columnconfigure(0, weight=1)
        self.popup.columnconfigure(1, weight=1)

        self.popup.rowconfigure(0, weight=1)
        self.popup.rowconfigure(1, weight=1)

        ins_label = customtkinter.CTkLabel(master=self.popup, text = "Please set your audio:\n(Remember to select both files before confirming!)", font=("Bahnschrift", 16), text_color="#a5243d")
        ins_label.grid(row=0, column=0, columnspan = 2, pady = 10, sticky='new')

        self.heart_label = customtkinter.CTkLabel(master=self.popup, text = "Heart audio file: Not set", font=("Bahnschrift", 16), text_color="#a5243d")
        self.heart_label.grid(row=0, column=0, sticky="ew")

        heart_button = customtkinter.CTkButton(master=self.popup, text='Select file', command=self.controller.setHeartAudio, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        heart_button.grid(row=0, column=1, padx=2, pady=2)

        self.lung_label = customtkinter.CTkLabel(master=self.popup, text = "Lung audio file: Not set", font=("Bahnschrift", 16), text_color="#a5243d")
        self.lung_label.grid(row=0, column=0, sticky="sew")

        lung_button = customtkinter.CTkButton(master=self.popup, text='Select file', command=self.controller.setLungAudio, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        lung_button.grid(row=0, column=1, padx=2, pady=2, sticky="s")

        confirm = customtkinter.CTkButton(self.popup, text="Confirm", command=self.controller.confirm, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        confirm.grid(row=1, column = 0)

        close_button = customtkinter.CTkButton(self.popup, text="Close", command=self.popup.destroy, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        close_button.grid(row=1, column=1)

    def destroy(self):
        self.popup.destroy()

    

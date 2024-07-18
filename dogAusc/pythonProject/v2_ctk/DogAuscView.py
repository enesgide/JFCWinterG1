import asyncio
import customtkinter
import os
from PIL import Image  
from async_tkinter_loop import async_handler


# Class that initialises the entire GUI view. Separated into two main frames, the side frame (which contains the app label and picture of the model) and the main frame
# which has the buttons and labels required for managing the model
class DogAuscView:

    # __init__(self, root)
    # inits all the attributes required by the View class, including the root Tk window created in Main, as well as the Controller class that contains the logic for each
    # interactable element

    # params: 
    # self = the class instance
    # root = the root Tk object

    # returns: None

    def __init__(self, root):
        self.root = root
        self.controller = None
        self.root.geometry('800x600')
        self.omni_frame = customtkinter.CTkFrame(master=self.root, width=800, height=600, corner_radius=10)
        self.omni_frame.pack(fill="both", expand=True)

        self.main_label = None
        self.connection_label = None
        self.apex_label = None
        self.non_apex_label = None

    # init_main_frame(self)
    # initialises the main frame (right side), with the audio view and test interface, and preset selection

    # params:
    # self = the class instance

    # returns: None

    def init_main_frame(self):
        main_frame = customtkinter.CTkFrame(master=self.omni_frame, width=600, height=550)
        main_frame.pack(side="right", fill="both", expand=True, padx=(5,10), pady=10)

        # configures the frame area into weighted rows and columns as a grid where other components can be placed
        main_frame.columnconfigure(0, weight = 1)
        main_frame.columnconfigure(1, weight = 1)
        main_frame.rowconfigure(0, weight=0)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(3, weight=1)

        self.apex_label = customtkinter.CTkLabel(master=main_frame, text = "Apex audio file: Not set", font=("Bahnschrift", 16))
        self.apex_label.grid(row=1, column=0, sticky="ew")

        apex_button = customtkinter.CTkButton(master=main_frame, text='Test apex audio', 
                                               command=self.controller.onTestApex, font=("Bahnschrift", 14))
        apex_button.grid(row=1, column=1, padx=2, pady=2)

        self.non_apex_label = customtkinter.CTkLabel(master=main_frame, text = "Non apex audio file: Not set", font=("Bahnschrift", 16))
        self.non_apex_label.grid(row=2, column=0, sticky="new")

        non_apex_button = customtkinter.CTkButton(master=main_frame, text='Test non apex audio', 
                                              command=self.controller.onTestNonApex, font=("Bahnschrift", 14))
        non_apex_button.grid(row=2, column=1, padx=2, pady=2, sticky='n')

        start_btn = customtkinter.CTkButton(main_frame, text='Start Auscultation', 
                                            command=async_handler(self.controller.startAuscultation), font=("Bahnschrift", 14))
        start_btn.grid(row=3, column=0, columnspan=2, sticky="new", padx=5)

        stop_btn = customtkinter.CTkButton(main_frame, text='End Auscultation', 
                                           command=async_handler(self.controller.endAuscultation), font=("Bahnschrift", 14))
        stop_btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5)

        self.connection_label = customtkinter.CTkLabel(master=main_frame, text = "Connection Status: Inactive", font=("Bahnschrift", 20), text_color = 'red')
        self.connection_label.grid(row=3, column=0, columnspan=2, padx=0, pady=10, sticky='s')


    # init_side_frame(self)    
    # initialises the side frame (left side), which has the start/stop auscultation buttons, image of the model, and load preset button

    # params:
    # self = the class instance

    # returns: None

    def init_side_frame(self):
        side_frame = customtkinter.CTkFrame(master=self.omni_frame, width=200, height=550, corner_radius=10)
        side_frame.pack(side="left", fill="both", expand=True, padx=(10,5), pady=10)

        # configures the frame area into weighted rows and columns as a grid where other components can be placed
        side_frame.columnconfigure(0, weight=1)
        side_frame.rowconfigure(0, weight=1)
        side_frame.rowconfigure(1, weight=1)

        side_label = customtkinter.CTkLabel(master=side_frame, text = "Auscultation Model:\nCardi B ", font=("Bahnschrift", 18))
        side_label.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        
        img_path = self.controller.resource_path(os.path.join("resources", "img", "cardi_b.jpg"))
        my_image = customtkinter.CTkImage(light_image=Image.open(img_path),
                                  dark_image=Image.open(img_path),
                                  size=(200, 250))
        
        image_label = customtkinter.CTkLabel(master = side_frame, image=my_image, text="")
        image_label.grid(row=0, column=0, sticky="s")

        load_btn = customtkinter.CTkButton(side_frame, text='Load files', 
                                           command=self.controller.onLoadAudio, font=("Bahnschrift", 14))
        load_btn.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=(0,10))

    # set_controller(self, controller)
    # method used to set the controller on view initialisation

    # params:
    # self = the class instance
    # controller = the instance of the DogAuscController class 

    # returns: None

    def set_controller(self, controller):
        self.controller = controller

    # get_omni(self)
    # method used to return the "omni frame," which is basically the root frame (only used to provide a different main background colour)

    # params: 
    # self = the class instance

    # returns: None

    def get_omni(self):
        return self.omni_frame
    
    # update_status(self, state)
    # asynchronous method that uptades the connection label in the view according the state. Called in asynchronous function controller.startAuscultation

    # params: 
    # self = the class instance
    # state = the application state identifier as a String

    #returns: None
    
    async def update_status(self, state):
        if state == "Inactive":
            self.connection_label.configure(text="Connection status: Inactive")
            self.connection_label.configure(text_color="red")
        elif state == "Pending":
            self.connection_label.configure(text="Connection status: Pending")
            self.connection_label.configure(text_color="orange")
        elif state == "Active":
            self.connection_label.configure(text="Connection status: Active")
            self.connection_label.configure(text_color="green")
        elif state == "NoFile":
            self.connection_label.configure(text="Please load audio files first!")
            await asyncio.sleep(5)
            self.connection_label.configure(text="Connection status: Inactive")
            self.connection_label.configure(text_color="red")

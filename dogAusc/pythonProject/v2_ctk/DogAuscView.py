import tkinter
import customtkinter
import os
from PIL import Image  

class DogAuscView:
    def __init__(self, root) -> None:
        self.root = root
        self.controller = None
        self.root.geometry('800x600')
        self.omni_frame = customtkinter.CTkFrame(master=self.root, width=800, height=600, corner_radius=10, fg_color="#CEE0DC")
        self.omni_frame.pack(fill="both", expand=True)

        self.main_label = None
        self.connection_label = None

        self.heart_label = None
        self.lung_label = None

    
    def init_main_frame(self):
        main_frame = customtkinter.CTkFrame(master=self.omni_frame, width=600, height=550, fg_color="#B9CFD4")
        main_frame.pack(side="right", fill="both", expand=True, padx=(5,10), pady=10)

        main_frame.columnconfigure(0, weight = 1)
        main_frame.columnconfigure(1, weight = 1)
        main_frame.rowconfigure(0, weight=0)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(3, weight=1)

        self.main_label = customtkinter.CTkLabel(master=main_frame, text = "Current Active Profile: None", font=("Bahnschrift", 20), text_color="#a5243d")
        self.main_label.grid(row=1, column=0, columnspan=2, sticky="n", padx=0, pady=10)

        self.heart_label = customtkinter.CTkLabel(master=main_frame, text = "Heart audio file: Not set", font=("Bahnschrift", 16), text_color="#a5243d")
        self.heart_label.grid(row=1, column=0, sticky="ew")

        heart_button = customtkinter.CTkButton(master=main_frame, text='Test heart audio', command=self.controller.onTestHeart, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        heart_button.grid(row=1, column=1, padx=2, pady=2)

        self.lung_label = customtkinter.CTkLabel(master=main_frame, text = "Lung audio file: Not set", font=("Bahnschrift", 16), text_color="#a5243d")
        self.lung_label.grid(row=2, column=0, sticky="new")

        lung_button = customtkinter.CTkButton(master=main_frame, text='Test lung audio', command=self.controller.onTestLung, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        lung_button.grid(row=2, column=1, padx=2, pady=2, sticky='n')


        preset_label = customtkinter.CTkLabel(master=main_frame, text = "Or select from presets here:", font=("Bahnschrift", 20), text_color="#a5243d")
        preset_label.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="ew")
            

        combobox = customtkinter.CTkComboBox(main_frame, 
                                             fg_color="#B48291", border_width=0, button_color= "#B48291",
                                             dropdown_fg_color="#B48291", dropdown_hover_color="#AB7384",
                                             font=("Bahnschrift", 14), dropdown_font=("Bahnschrift", 14),
                                             values=["Year 1", "Year 2", "Year 3", "DVM"], state="readonly", command=self.controller.onLoadPreset)
        combobox.set("Select your preset here")
        combobox.grid(row=2, column=0, columnspan=2, padx=10, pady=(0,10), sticky="sew")

        self.connection_label = customtkinter.CTkLabel(master=main_frame, text = "Connection Status: Inactive", font=("Bahnschrift", 20), text_color="red")
        self.connection_label.grid(row=3, column=0, columnspan=2, padx=0, pady=10, sticky='s')


        

    def init_side_frame(self):
        side_frame = customtkinter.CTkFrame(master=self.omni_frame, width=200, height=550, corner_radius=10, fg_color="#B9CFD4")
        side_frame.pack(side="left", fill="both", expand=True, padx=(10,5), pady=10)

        side_frame.columnconfigure(0, weight=1)
        side_frame.rowconfigure(0, weight=1)
        side_frame.rowconfigure(1, weight=1)
        side_frame.rowconfigure(2, weight=1)

        side_label = customtkinter.CTkLabel(master=side_frame, text = "Auscultation Model:\nCardi B ", font=("Bahnschrift", 18), text_color="#a5243d")
        side_label.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        
        img_path = os.path.join(r"C:\Users\allen\Documents\jfc\wslcode\jfc\JFCWinterG1\dogAusc\pythonProject\v2_ctk\resources\t1.jpg")
        my_image = customtkinter.CTkImage(light_image=Image.open(img_path),
                                  dark_image=Image.open(img_path),
                                  size=(200, 200))
        
        image_label = customtkinter.CTkLabel(master = side_frame, image=my_image, text="")
        image_label.grid(row=0, column=0, sticky="s")

        load_btn = customtkinter.CTkButton(side_frame, text='Load files', command=self.controller.onLoadAudio, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        load_btn.grid(row=1, column=0, sticky="ew", padx=5, pady=(0,10))

        start_btn = customtkinter.CTkButton(side_frame, text='Start Auscultation', command=self.controller.startAuscultation, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        start_btn.grid(row=2, column=0, sticky="new", padx=5, pady=5)

        stop_btn = customtkinter.CTkButton(side_frame, text='End Auscultation', command=self.controller.endAuscultation, font=("Bahnschrift", 14), fg_color="#B48291", hover_color="#AB7384")
        stop_btn.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    def set_controller(self, controller):
        self.controller = controller

    def get_omni(self):
        return self.omni_frame

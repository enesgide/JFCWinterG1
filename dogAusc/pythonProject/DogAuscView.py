#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
# in conjunction with Tcl version 8.6
# Jul 02, 2024 11:55:03 AM +1000 platform: Windows NT
# Modified to fit MVC by Allen Burias
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from functools import partial
from async_tkinter_loop import async_handler

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = 'black'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'


# To fix: rework command association similar to test project, rename stuff around

class DogAuscView:
    def __init__(self, root):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.root = root
        self.controller = None
        self.root.geometry("510x394+660+210")
        self.root.minsize(120, 1)
        self.root.maxsize(1924, 1061)
        self.root.resizable(1, 1)
        self.root.title("VetSci Dog Auscultation Model")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")

        self.connection_label = None
        self.s1_label = None
        self.s2_label = None
        self.s3_label = None
        self.s4_label = None

    def set_controller(self, controller):
        self.controller = controller

    def get_root(self):
        return self.root

    def init_main_frame(self):
        main_frame = tk.LabelFrame(self.root)
        main_frame.place(relx=0.02, rely=0.025, relheight=0.749, relwidth=0.961)
        main_frame.configure(relief='groove')
        main_frame.configure(foreground="black")
        main_frame.configure(text='''Dog Auscultation Model: Cardi B''')
        main_frame.configure(background="#d9d9d9")
        main_frame.configure(highlightbackground="#d9d9d9")
        main_frame.configure(highlightcolor="black")

        self.s1_label = tk.Label(main_frame)
        self.s1_label.place(relx=0.041, rely=0.136, height=30, width=315, bordermode='ignore')
        self.s1_label.configure(activebackground="#d9d9d9")
        self.s1_label.configure(activeforeground="black")
        self.s1_label.configure(anchor='w')
        self.s1_label.configure(background="#d9d9d9")
        self.s1_label.configure(compound='left')
        self.s1_label.configure(disabledforeground="#a3a3a3")
        self.s1_label.configure(foreground="black")
        self.s1_label.configure(highlightbackground="#d9d9d9")
        self.s1_label.configure(highlightcolor="black")
        self.s1_label.configure(text='''Audio file for sensor 1: test''')

        self.s2_label = tk.Label(main_frame)
        self.s2_label.place(relx=0.041, rely=0.305, height=30, width=315, bordermode='ignore')
        self.s2_label.configure(activebackground="#d9d9d9")
        self.s2_label.configure(activeforeground="black")
        self.s2_label.configure(anchor='w')
        self.s2_label.configure(background="#d9d9d9")
        self.s2_label.configure(compound='left')
        self.s2_label.configure(disabledforeground="#a3a3a3")
        self.s2_label.configure(foreground="black")
        self.s2_label.configure(highlightbackground="#d9d9d9")
        self.s2_label.configure(highlightcolor="black")
        self.s2_label.configure(text='''Audio file for sensor 2: test''')

        self.s3_label = tk.Label(main_frame)
        self.s3_label.place(relx=0.041, rely=0.475, height=30, width=315, bordermode='ignore')
        self.s3_label.configure(activebackground="#d9d9d9")
        self.s3_label.configure(activeforeground="black")
        self.s3_label.configure(anchor='w')
        self.s3_label.configure(background="#d9d9d9")
        self.s3_label.configure(compound='left')
        self.s3_label.configure(disabledforeground="#a3a3a3")
        self.s3_label.configure(foreground="black")
        self.s3_label.configure(highlightbackground="#d9d9d9")
        self.s3_label.configure(highlightcolor="black")
        self.s3_label.configure(text='''Audio file for sensor 3: test''')

        self.s4_label = tk.Label(main_frame)
        self.s4_label.place(relx=0.041, rely=0.644, height=40, width=315, bordermode='ignore')
        self.s4_label.configure(activebackground="#d9d9d9")
        self.s4_label.configure(activeforeground="black")
        self.s4_label.configure(anchor='w')
        self.s4_label.configure(background="#d9d9d9")
        self.s4_label.configure(compound='left')
        self.s4_label.configure(disabledforeground="#a3a3a3")
        self.s4_label.configure(foreground="black")
        self.s4_label.configure(highlightbackground="#d9d9d9")
        self.s4_label.configure(highlightcolor="black")
        self.s4_label.configure(text='''Audio file for sensor 4: test''')

        s1_test = tk.Button(main_frame)
        s1_test.place(relx=0.837, rely=0.136, height=26, width=47, bordermode='ignore')
        s1_test.configure(activebackground="#d9d9d9")
        s1_test.configure(activeforeground="black")
        s1_test.configure(background="#d9d9d9")
        s1_test.configure(command=self.controller.onTestS1)
        s1_test.configure(disabledforeground="#a3a3a3")
        s1_test.configure(foreground="black")
        s1_test.configure(highlightbackground="#d9d9d9")
        s1_test.configure(highlightcolor="black")
        s1_test.configure(text='''Test S1''')

        s2_test = tk.Button(main_frame)
        s2_test.place(relx=0.837, rely=0.305, height=26, width=47, bordermode='ignore')
        s2_test.configure(activebackground="#d9d9d9")
        s2_test.configure(activeforeground="black")
        s2_test.configure(background="#d9d9d9")
        s2_test.configure(command=self.controller.onTestS2)
        s2_test.configure(disabledforeground="#a3a3a3")
        s2_test.configure(foreground="black")
        s2_test.configure(highlightbackground="#d9d9d9")
        s2_test.configure(highlightcolor="black")
        s2_test.configure(text='''Test S2''')

        s3_test = tk.Button(main_frame)
        s3_test.place(relx=0.837, rely=0.475, height=26, width=47, bordermode='ignore')
        s3_test.configure(activebackground="#d9d9d9")
        s3_test.configure(activeforeground="black")
        s3_test.configure(background="#d9d9d9")
        s3_test.configure(command=self.controller.onTestS3)
        s3_test.configure(disabledforeground="#a3a3a3")
        s3_test.configure(foreground="black")
        s3_test.configure(highlightbackground="#d9d9d9")
        s3_test.configure(highlightcolor="black")
        s3_test.configure(text='''Test S3''')

        s4_test = tk.Button(main_frame)
        s4_test.place(relx=0.837, rely=0.644, height=26, width=47, bordermode='ignore')
        s4_test.configure(activebackground="#d9d9d9")
        s4_test.configure(activeforeground="black")
        s4_test.configure(background="#d9d9d9")
        s4_test.configure(command=self.controller.onTestS4)
        s4_test.configure(disabledforeground="#a3a3a3")
        s4_test.configure(foreground="black")
        s4_test.configure(highlightbackground="#d9d9d9")
        s4_test.configure(highlightcolor="black")
        s4_test.configure(text='''Test S4''')

        start_button = tk.Button(main_frame)
        start_button.place(relx=0.163, rely=0.847, height=26, width=107, bordermode='ignore')
        start_button.configure(activebackground="#d9d9d9")
        start_button.configure(activeforeground="black")
        start_button.configure(background="#d9d9d9")
        start_button.configure(command=async_handler(self.controller.startAuscultation))
        start_button.configure(disabledforeground="#a3a3a3")
        start_button.configure(foreground="black")
        start_button.configure(highlightbackground="#d9d9d9")
        start_button.configure(highlightcolor="black")
        start_button.configure(text='''Start Auscultation''')

        end_button = tk.Button(main_frame)
        end_button.place(relx=0.633, rely=0.847, height=26, width=107, bordermode='ignore')
        end_button.configure(activebackground="#d9d9d9")
        end_button.configure(activeforeground="black")
        end_button.configure(background="#d9d9d9")
        end_button.configure(command=async_handler(self.controller.endAuscultation))
        end_button.configure(disabledforeground="#a3a3a3")
        end_button.configure(foreground="black")
        end_button.configure(highlightbackground="#d9d9d9")
        end_button.configure(highlightcolor="black")
        end_button.configure(text='''End Auscultation''')

    def init_button_frame(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        button_frame.place(relx=0.02, rely=0.787, relheight=0.19, relwidth=0.961)
        button_frame.configure(relief='groove')
        button_frame.configure(borderwidth="2")
        button_frame.configure(relief="groove")
        button_frame.configure(background="#d9d9d9")
        button_frame.configure(highlightbackground="#d9d9d9")
        button_frame.configure(highlightcolor="black")

        load_preset_button = tk.Button(button_frame)
        load_preset_button.place(relx=0.755, rely=0.333, height=26, width=107)
        load_preset_button.configure(activebackground="#d9d9d9")
        load_preset_button.configure(activeforeground="black")
        load_preset_button.configure(background="#d9d9d9")
        load_preset_button.configure(disabledforeground="#a3a3a3")
        load_preset_button.configure(foreground="black")
        load_preset_button.configure(command=self.controller.onLoadPreset)
        load_preset_button.configure(highlightbackground="#d9d9d9")
        load_preset_button.configure(highlightcolor="black")
        load_preset_button.configure(text='''Load from preset''')

        self.connection_label = tk.Label(button_frame)
        self.connection_label.place(relx=0.041, rely=0.333, height=11, width=300)
        self.connection_label.configure(activebackground="#d9d9d9")
        self.connection_label.configure(activeforeground="black")
        self.connection_label.configure(anchor='w')
        self.connection_label.configure(background="#d9d9d9")
        self.connection_label.configure(compound='left')
        self.connection_label.configure(disabledforeground="#a3a3a3")
        self.connection_label.configure(foreground="red")
        self.connection_label.configure(highlightbackground="#d9d9d9")
        self.connection_label.configure(highlightcolor="black")
        self.connection_label.configure(text='''Bluetooth Connection to Model: Inactive''')

        load_new_button = tk.Button(button_frame)
        load_new_button.place(relx=0.541, rely=0.333, height=26, width=97)
        load_new_button.configure(activebackground="#d9d9d9")
        load_new_button.configure(activeforeground="black")
        load_new_button.configure(background="#d9d9d9")
        load_new_button.configure(command=self.controller.onLoadAudio)
        load_new_button.configure(disabledforeground="#a3a3a3")
        load_new_button.configure(foreground="black")
        load_new_button.configure(highlightbackground="#d9d9d9")
        load_new_button.configure(highlightcolor="black")
        load_new_button.configure(text='''Load new audio''')

    def view_initialise(self):
        self.init_main_frame()
        self.init_button_frame()

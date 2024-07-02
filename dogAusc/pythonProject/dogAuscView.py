#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
# in conjunction with Tcl version 8.6
# Jul 02, 2024 11:55:03 AM +1000 platform: Windows NT
# Significant modifications made by Allen Burias
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)


_bgcolor = '#d9d9d9'
_fgcolor = 'black'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'



# To fix: rework command association similar to test project, rename stuff around

class dpgAuscView:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("510x394+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("VetSci Dog Auscultation Model")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.mainFrame = tk.LabelFrame(self.top)
        self.mainFrame.place(relx=0.02, rely=0.025, relheight=0.749, relwidth=0.961)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(foreground="black")
        self.mainFrame.configure(text='''Dog Auscultation Model: Cardi B''')
        self.mainFrame.configure(background="#d9d9d9")
        self.mainFrame.configure(highlightbackground="#d9d9d9")
        self.mainFrame.configure(highlightcolor="black")

        self.s2Label = tk.Label(self.mainFrame)
        self.s2Label.place(relx=0.041, rely=0.339, height=30, width=315, bordermode='ignore')
        self.s2Label.configure(activebackground="#d9d9d9")
        self.s2Label.configure(activeforeground="black")
        self.s2Label.configure(anchor='w')
        self.s2Label.configure(background="#d9d9d9")
        self.s2Label.configure(compound='left')
        self.s2Label.configure(disabledforeground="#a3a3a3")
        self.s2Label.configure(foreground="black")
        self.s2Label.configure(highlightbackground="#d9d9d9")
        self.s2Label.configure(highlightcolor="black")
        self.s2Label.configure(text='''Audio file for sensor 2: test''')

        self.s3Label = tk.Label(self.mainFrame)
        self.s3Label.place(relx=0.041, rely=0.508, height=30, width=315, bordermode='ignore')
        self.s3Label.configure(activebackground="#d9d9d9")
        self.s3Label.configure(activeforeground="black")
        self.s3Label.configure(anchor='w')
        self.s3Label.configure(background="#d9d9d9")
        self.s3Label.configure(compound='left')
        self.s3Label.configure(disabledforeground="#a3a3a3")
        self.s3Label.configure(foreground="black")
        self.s3Label.configure(highlightbackground="#d9d9d9")
        self.s3Label.configure(highlightcolor="black")
        self.s3Label.configure(text='''Audio file for sensor 3: test''')

        self.s4Label = tk.Label(self.mainFrame)
        self.s4Label.place(relx=0.041, rely=0.678, height=40, width=315, bordermode='ignore')
        self.s4Label.configure(activebackground="#d9d9d9")
        self.s4Label.configure(activeforeground="black")
        self.s4Label.configure(anchor='w')
        self.s4Label.configure(background="#d9d9d9")
        self.s4Label.configure(compound='left')
        self.s4Label.configure(disabledforeground="#a3a3a3")
        self.s4Label.configure(foreground="black")
        self.s4Label.configure(highlightbackground="#d9d9d9")
        self.s4Label.configure(highlightcolor="black")
        self.s4Label.configure(text='''Audio file for sensor 4: test''')

        self.s1Label = tk.Label(self.mainFrame)
        self.s1Label.place(relx=0.041, rely=0.169, height=30, width=315, bordermode='ignore')
        self.s1Label.configure(activebackground="#d9d9d9")
        self.s1Label.configure(activeforeground="black")
        self.s1Label.configure(anchor='w')
        self.s1Label.configure(background="#d9d9d9")
        self.s1Label.configure(compound='left')
        self.s1Label.configure(disabledforeground="#a3a3a3")
        self.s1Label.configure(foreground="black")
        self.s1Label.configure(highlightbackground="#d9d9d9")
        self.s1Label.configure(highlightcolor="black")
        self.s1Label.configure(text='''Audio file for sensor 1: test''')

        self.s1Test = tk.Button(self.mainFrame)
        self.s1Test.place(relx=0.837, rely=0.169, height=26, width=47, bordermode='ignore')
        self.s1Test.configure(activebackground="#d9d9d9")
        self.s1Test.configure(activeforeground="black")
        self.s1Test.configure(background="#d9d9d9")
        self.s1Test.configure(command=GUI_support.onTestS1)
        self.s1Test.configure(disabledforeground="#a3a3a3")
        self.s1Test.configure(foreground="black")
        self.s1Test.configure(highlightbackground="#d9d9d9")
        self.s1Test.configure(highlightcolor="black")
        self.s1Test.configure(text='''Test S1''')

        self.s2Test = tk.Button(self.mainFrame)
        self.s2Test.place(relx=0.837, rely=0.339, height=26, width=47, bordermode='ignore')
        self.s2Test.configure(activebackground="#d9d9d9")
        self.s2Test.configure(activeforeground="black")
        self.s2Test.configure(background="#d9d9d9")
        self.s2Test.configure(command=GUI_support.onTestS2)
        self.s2Test.configure(disabledforeground="#a3a3a3")
        self.s2Test.configure(foreground="black")
        self.s2Test.configure(highlightbackground="#d9d9d9")
        self.s2Test.configure(highlightcolor="black")
        self.s2Test.configure(text='''Test S2''')

        self.s3Test = tk.Button(self.mainFrame)
        self.s3Test.place(relx=0.837, rely=0.508, height=26, width=47, bordermode='ignore')
        self.s3Test.configure(activebackground="#d9d9d9")
        self.s3Test.configure(activeforeground="black")
        self.s3Test.configure(background="#d9d9d9")
        self.s3Test.configure(command=GUI_support.onTestS3)
        self.s3Test.configure(disabledforeground="#a3a3a3")
        self.s3Test.configure(foreground="black")
        self.s3Test.configure(highlightbackground="#d9d9d9")
        self.s3Test.configure(highlightcolor="black")
        self.s3Test.configure(text='''Test S3''')

        self.s4Test = tk.Button(self.mainFrame)
        self.s4Test.place(relx=0.837, rely=0.678, height=26, width=47, bordermode='ignore')
        self.s4Test.configure(activebackground="#d9d9d9")
        self.s4Test.configure(activeforeground="black")
        self.s4Test.configure(background="#d9d9d9")
        self.s4Test.configure(command=GUI_support.onTestS4)
        self.s4Test.configure(disabledforeground="#a3a3a3")
        self.s4Test.configure(foreground="black")
        self.s4Test.configure(highlightbackground="#d9d9d9")
        self.s4Test.configure(highlightcolor="black")
        self.s4Test.configure(text='''Test S4''')

        self.buttonFrame = tk.Frame(self.top)
        self.buttonFrame.place(relx=0.02, rely=0.787, relheight=0.19, relwidth=0.961)
        self.buttonFrame.configure(relief='groove')
        self.buttonFrame.configure(borderwidth="2")
        self.buttonFrame.configure(relief="groove")
        self.buttonFrame.configure(background="#d9d9d9")
        self.buttonFrame.configure(highlightbackground="#d9d9d9")
        self.buttonFrame.configure(highlightcolor="black")

        self.loadPresetButton = tk.Button(self.buttonFrame)
        self.loadPresetButton.place(relx=0.755, rely=0.333, height=26, width=107)
        self.loadPresetButton.configure(activebackground="#d9d9d9")
        self.loadPresetButton.configure(activeforeground="black")
        self.loadPresetButton.configure(background="#d9d9d9")
        self.loadPresetButton.configure(disabledforeground="#a3a3a3")
        self.loadPresetButton.configure(foreground="black")
        self.loadPresetButton.configure(command=GUI_support.onLoadPreset)
        self.loadPresetButton.configure(highlightbackground="#d9d9d9")
        self.loadPresetButton.configure(highlightcolor="black")
        self.loadPresetButton.configure(text='''Load from preset''')

        self.connectionLabel = tk.Label(self.buttonFrame)
        self.connectionLabel.place(relx=0.041, rely=0.333, height=11, width=224)
        self.connectionLabel.configure(activebackground="#d9d9d9")
        self.connectionLabel.configure(activeforeground="black")
        self.connectionLabel.configure(anchor='w')
        self.connectionLabel.configure(background="#d9d9d9")
        self.connectionLabel.configure(compound='left')
        self.connectionLabel.configure(disabledforeground="#a3a3a3")
        self.connectionLabel.configure(foreground="black")
        self.connectionLabel.configure(highlightbackground="#d9d9d9")
        self.connectionLabel.configure(highlightcolor="black")
        self.connectionLabel.configure(text='''Bluetooth Connection to Model: Active''')

        self.loadNewButton = tk.Button(self.buttonFrame)
        self.loadNewButton.place(relx=0.541, rely=0.333, height=26, width=97)
        self.loadNewButton.configure(activebackground="#d9d9d9")
        self.loadNewButton.configure(activeforeground="black")
        self.loadNewButton.configure(background="#d9d9d9")
        self.loadNewButton.configure(command=GUI_support.onLoadAudio)
        self.loadNewButton.configure(disabledforeground="#a3a3a3")
        self.loadNewButton.configure(foreground="black")
        self.loadNewButton.configure(highlightbackground="#d9d9d9")
        self.loadNewButton.configure(highlightcolor="black")
        self.loadNewButton.configure(text='''Load new audio''')

def start_up():
    GUI_support.main()

if __name__ == '__main__':
    GUI_support.main()

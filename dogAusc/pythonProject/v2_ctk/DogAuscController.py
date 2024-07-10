import asyncio
import pygame
import tkinter as tk
from tkinter import filedialog
import os

from DogAuscPopup import DogAuscPopup
from PopupController import PopupController

NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

class DogAuscController:
    def __init__(self, model, view):
        self.model = model
        self.view = view 
        pygame.mixer.init()

    # todo: play/pause
    def onTestHeart(self):
        pass

    # todo: play/pause
    def onTestLung(self):
        pass

    def onLoadAudio(self):
        popup = DogAuscPopup(self.view)
        popup_controller = PopupController(self.view, popup, self.model)
        popup.set_controller(popup_controller)
        popup.init_popup()

    # todo: preset creation, need audio
    def onLoadPreset(self, choice):
        self.view.main_label.configure(text= f"Current Active Profile: {choice}")
        print("combobox dropdown clicked:", choice)

    # todo: pressure sensing, volume control, play audio
    def notification_handler(self, sender, data):
        decoded_data = data.decode()
        print(f"Received notification: {decoded_data}")
        
        # Parse the data
        values = [int(x.strip()) for x in decoded_data.split(',')]
        
        # Get the highest value for each pair
        heart_pressure = max(values[0], values[1])
        lung_pressure = max(values[2], values[3])
        print(f"Max Values: Heart: {heart_pressure}, Lung: {lung_pressure}")

    async def startAuscultation(self):
        self.view.update_status("Pending")
        connected = await self.model.connect_to_arduino()
        if connected:
            self.view.update_status("Active")
            await self.model.start_notifications(NOTIFY_CHARACTERISTIC_UUID, self.notification_handler)

            while True:
                await asyncio.sleep(1)
        else:
            self.view.update_status("Inactive")

    async def endAuscultation(self):
        if self.model.client != None and self.model.client.is_connected:
            try:
                await self.model.client.stop_notify(NOTIFY_CHARACTERISTIC_UUID)
                await self.model.client_disconnect()
                self.view.update_status("Inactive")
                print("auscultation ended")
            except Exception as e:
                print(f"Disconnection error: {e}")
            finally:
                self.model.is_connected = False
                print(self.model.is_connected)

    def play_audio(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    


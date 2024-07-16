import asyncio
import sys
import pygame
import time
import os

from DogAuscPopup import DogAuscPopup
from PopupController import PopupController

NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"


class DogAuscController:
    def __init__(self, model, view):
        self.model = model
        self.view = view 

        self.s1_playing = False
        self.s2_playing = False

        pygame.mixer.init()

    def resource_path(self, relative_path):
        base_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(base_path, relative_path)
    
    def onTestHeart(self):
        if self.model.get_s1() != None:
            if self.s1_playing == False:
                if self.s2_playing == True:
                    pygame.mixer.music.pause()
                    self.s2_playing = False

                pygame.mixer.music.load(self.model.get_s1())
                pygame.mixer.music.play()
                self.s1_playing = True
                time.sleep(7)
                pygame.mixer.music.stop()
        else:
            return

    def onTestLung(self):
        if self.model.get_s2() != None:
            if self.s2_playing == False:
                if self.s1_playing == True:
                    pygame.mixer.music.pause()
                    self.s1_playing = False
                    
            pygame.mixer.music.load(self.model.get_s2())
            pygame.mixer.music.play()
            self.s2_playing = True
            time.sleep(7)
            pygame.mixer.music.stop()
        else:
            return

    def onLoadAudio(self):
        popup = DogAuscPopup(self.view)
        popup_controller = PopupController(self.view, popup, self.model)
        popup.set_controller(popup_controller)
        popup.init_popup()

    # todo: preset creation, need audio
    def onLoadPreset(self, choice):
        if choice == "Augie":
            heart_path = self.resource_path(os.path.join("resources", "presets", "augie","AUGIE_HEART.wav"))
            lung_path = self.resource_path(os.path.join("resources", "presets", "augie","AUGIE_LUNG.wav"))

            self.model.set_s1(heart_path)
            self.model.set_s2(lung_path)

            self.view.heart_label.configure(text=f"Heart audio file: {os.path.basename(self.model.get_s1())}")
            self.view.lung_label.configure(text=f"Lung audio file: {os.path.basename(self.model.get_s2())}")

            self.view.main_label.configure(text= f"Current Active Profile: {choice}")
        

    def set_volume(channel, pressure):
        # Map pressure (10-200) to volume (0.0-1.0)
        volume = max(0.0, min(1.0, (pressure - 50) / 90))
        channel.set_volume(volume)
        print(f"Channel volume set to {volume:.2f}")

    # todo: pressure sensing, volume control, play audio
    def notification_handler(self, sender, data):
        decoded_data = data.decode()
        print(f"Received notification: {decoded_data}")
        
        # Parse the data
        values = [int(x.strip()) for x in decoded_data.split(',')]
        
        # Get the highest value for each pair
        heart_pressure = max(values[0], values[1])
        lung_pressure = max(values[2], values[3])

        #apex sensors are 0, 1, (100% volume max), 2, 3 (80% volume max)
        print(f"Max Values: Heart: {heart_pressure}, Lung: {lung_pressure}")

        def set_volume(channel, pressure):
        # Map pressure (10-200) to volume (0.0-1.0)
            volume = max(0.0, min(1.0, (pressure - 10) / 90))
            channel.set_volume(volume)
            print(f"Channel volume set to {volume:.2f}")
        
        set_volume(self.model.s1_py, heart_pressure)
        set_volume(self.model.s2_py, lung_pressure)
        

    async def startAuscultation(self):
        if self.model.get_s1() == None or self.model.get_s2() == None:
            await self.view.update_status("NoFile")
            return
        

        await self.view.update_status("Pending")
        connected = await self.model.connect_to_arduino()
        if connected:
            await self.view.update_status("Active")
            self.model.s1_py = pygame.mixer.Sound(self.model.get_s1())
            self.model.s2_py = pygame.mixer.Sound(self.model.get_s2())

            self.model.s1_py.play(-1)
            self.model.s2_py.play(-1)
            
            await self.model.start_notifications(NOTIFY_CHARACTERISTIC_UUID, self.notification_handler)

            while True:
                await asyncio.sleep(1)
        else:
            await self.view.update_status("Inactive")

    async def endAuscultation(self):
        if self.model.client != None and self.model.client.is_connected:
            try:
                await asyncio.sleep(2)
                await self.model.client.stop_notify(NOTIFY_CHARACTERISTIC_UUID)
                await self.model.client_disconnect()
                await self.view.update_status("Inactive")
                self.model.s1_py.stop()
                self.model.s2_py.stop()
                print("auscultation ended")
            except Exception as e:
                print(f"Disconnection error: {e}")
            finally:
                self.model.is_connected = False
                print(self.model.is_connected)
    


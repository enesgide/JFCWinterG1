import pygame
from tkinter import filedialog
import tkinter as tk
import asyncio
import os

NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

class DogAuscController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pygame.mixer.init()

    def onTestS1(self):
        pass

    def onTestS2(self):
        pass

    def onTestS3(self):
        pass

    def onTestS4(self):
        pass

    def onLoadAudio(self):
        self.view.s1_label.config(text="Audio file for sensor 1: Wa")
        self.view.s2_label.config(text="Audio file for sensor 2: Wa")
        self.view.s3_label.config(text="Audio file for sensor 3: Wee")
        self.view.s4_label.config(text="Audio file for sensor 4: Woo")

    def onLoadPreset(self):
        pass

    async def startAuscultation(self):
        self.view.update_status("Pending")
        connected = await self.model.connect_to_arduino()
        if connected:
            def notif_handler(sender, data):
                print(data.decode().split(','))
            self.view.update_status("Active")
            await self.model.start_notifications(NOTIFY_CHARACTERISTIC_UUID, notif_handler)

            while True:
                await asyncio.sleep(1)
        else:
            self.view.update_status("Inactive")
        await self.model.client_disconnect()



    async def endAuscultation(self):
        if self.model.client != None:
            try:
                await self.model.client.stop_notify(NOTIFY_CHARACTERISTIC_UUID)
                await self.model.client_disconnect()
                self.view.update_status("Inactive")
                print("auscultation ended")
            except Exception as e:
                print(f"Disconnection error: {e}")
            finally:
                self.model.is_connected = False


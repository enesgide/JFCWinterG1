import asyncio
import pygame
import time
import os

from DogAuscPopup import DogAuscPopup
from PopupController import PopupController

# Variable that represents the specific details for the model's Arduino
NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

# Controller class that updates the model and view based on user interaction
class DogAuscController:

    # __init__(self, model, view)
    # initialises the Controller class, setting the model and view as attributes and initialises the pygame mixer object.

    # params:
    # self = the class instance
    # model = the Model instance
    # view = the View instance

    # returns: None
    
    def __init__(self, model, view):
        self.model = model
        self.view = view 

        pygame.mixer.init()

    # resource_path(self, relative_path):
    # method that ensures each method that calls resources uses the correct relative paths to ensure file loading works regardless of platform

    # params:
    # self = the class instance
    # relative_path = the relative path of a resource file

    # returns: None
    def resource_path(self, relative_path):
        base_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(base_path, relative_path)
    
    # onTestApex(self)
    # method called when the "Test Apex" button is pressed. Plays the apex audio for 7s

    # params:
    # self = the class instance

    # returns: None
    
    def onTestApex(self):
        if self.model.get_s1() != None:
            if self.model.s1_playing == False:
                if self.s2_playing == True:
                    pygame.mixer.music.pause()
                    self.model.s2_playing = False

                pygame.mixer.music.load(self.model.get_s1())
                pygame.mixer.music.play()
                self.s1_playing = True
                time.sleep(7)
                pygame.mixer.music.stop()
        else:
            return
        
    # onTestNonApex(self)
    # method called when the "Test non apex" button is pressed. Plays the non apex audio for 7s

    # params:
    # self = the class instance

    # returns: None

    def onTestNonApex(self):
        if self.model.get_s2() != None:
            if self.model.s2_playing == False:
                if self.model.s1_playing == True:
                    pygame.mixer.music.pause()
                    self.model.s1_playing = False
                    
            pygame.mixer.music.load(self.model.get_s2())
            pygame.mixer.music.play()
            self.s2_playing = True
            time.sleep(7)
            pygame.mixer.music.stop()
        else:
            return

    # onLoadAudio(self)
    # method that opens the DogAuscPopup, which is a separate frame that facilitates file loading functionality

    # params:
    # self = the class instance

    # returns: None

    def onLoadAudio(self):
        popup = DogAuscPopup(self.view)
        popup_controller = PopupController(self.view, popup, self.model)
        popup.set_controller(popup_controller)
        popup.init_popup()

    def set_volume(channel, pressure):
        # Map pressure (10-100) to volume (0.0-1.0)
        volume = max(0.0, min(1.0, (pressure - 50) / 90))
        channel.set_volume(volume)
        print(f"Channel volume set to {volume:.2f}")

    # notification_handler(self, sender, data)
    # the method that continuously reads pressure data from the arduino and calls set_volume() accordingly.
    # sender is used as a parameter as it is required by the notification_reader, but is not used.
    # can be used in debugging scenarios to identify the uuid of the bluetooth module you are currently communicating with.

    # Contains another method set_volume which is only used in this scope

    # param:
    # self = the class instance
    # sender = the sender of the data 
    # data = the data received

    # returns: None

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

        # set_volume(channel, pressure)
        # method that sets a pygame.mixer.Sound instance's volume based on Arduino pressure sensor readings

        # params:
        # channel = the pygame.mixer.Sound instance
        # pressure = the pressure reading from the Arduino as an int

        #returns : None

        def set_volume(channel, pressure):
        # Map pressure (10-100) to volume (0.0-1.0)
            volume = max(0.0, min(1.0, (pressure - 10) / 90))
            channel.set_volume(volume)
            print(f"Channel volume set to {volume:.2f}")
        
        set_volume(self.model.s1_py, heart_pressure)
        set_volume(self.model.s2_py, lung_pressure)
        
    # startAuscultation(self)
    # method that initiates the identification and connection process between the model and the Arduino bluetooth module, and starts the audio and notification loop, when the 
    # associated button is pressed.

    # params:
    # self = the class instance

    # returns: None

    async def startAuscultation(self):
        if self.model.get_s1() == None or self.model.get_s2() == None:
            await self.view.update_status("NoFile")
            return

        await self.view.update_status("Pending")
        connected = await self.model.identify_arduino()
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

    # endAuscultation(self)
    # method that disconnects the model from the Arduino and pauses the audio streams playing, effectively ending the auscultation process.

    # params:
    # self = the class instance

    # returns: None

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
    


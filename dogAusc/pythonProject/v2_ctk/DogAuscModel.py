import asyncio
from bleak import BleakClient, BleakScanner

# Variables that represent the specific details for the model's Arduino
ARDUINO_NAME = "DogAus"
REQUEST_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1215"
NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

# Class that represets the business logic associated with the Auscultation Model
class DogAuscModel:

    # __init__(self, root)
    # inits all the attributes required by the Model class, which involves connection status, audio file paths, Bluetooth client, instances of 
    # Pygame's sound object to be played and booleans representing which sound file is being played.

    # params: 
    # self = the class instance

    # returns: None

    def __init__(self):
        self.is_connected = False
        self.s1_audio = None
        self.s2_audio = None
        self.client = None

        self.s1_py = None
        self.s2_py = None

        
        self.s1_playing = False
        self.s2_playing = False

    # set_s1(self, audio)
    # setter method for s1 (apex) file path

    # params:
    # self = the class instance
    # audio = audio file path as a String

    # returns: None

    def set_s1(self, audio):
        self.s1_audio = audio

    # set_s2(self, audio)
    # setter method for s2 (non apex) file path

    # params:
    # self = the class instance
    # audio = audio file path as a String

    # returns: None

    def set_s2(self, audio):
        self.s2_audio = audio

    # get_s1(self, audio)
    # getter method for s1 (apex) file path

    # params:
    # self = the class instance

    # returns: s1_audio, the file path for the apex audio file as a String

    def get_s1(self):
        return self.s1_audio

    # get_s2(self, audio)
    # getter method for s2 (non apex) file path

    # params:
    # self = the class instance

    # returns: s2_audio, the file path for the apex audio file as a String

    def get_s2(self):
        return self.s2_audio

    # connected(self)
    # getter method for the client connection status

    # params:
    # self = the class instance

    # returns: is_connected, client connection status as a boolean

    def connected(self):
        return self.is_connected
    
    # client_dosconnect(self)
    # asynchronous method to disconnect the model from the Arduino client

    # params:
    # self = the class instance

    # returns: None

    async def client_disconnect(self):
        await self.client.disconnect()
        self.is_connected = False

    # identify_arduino(self)
    # asynchronous method that utilises the Bleak library to identify the Arduino UNO R4 WiFi's ESP32 Bluetooth low energy (BLE) module
    # and sets the connection status attribute depending on the operation's success/failure

    # params: 
    # self = the class instance

    # returns: connection status as a Boolean

    async def identify_arduino(self):
        #scan for devices
        device = None
        print("Scanning for devices...")
        devices = await BleakScanner.discover()
        for d in devices:
            print(f"Found device: {d.name}, Address: {d.address}")
            if d.name == ARDUINO_NAME:
                device = d
                break
        if device is None:
            print(f"Device {ARDUINO_NAME} not found")
            return

        print(f"Connecting to {device.name} at {device.address}...")

        #establis connection with module using BleakClient
        try:
            async with BleakClient(device.address, timeout=30.0) as client:
                self.client = client
                print(f"Connected to {device.name}")
                write_data = "READ".encode()  # Convert string to bytes
                await client.write_gatt_char(REQUEST_CHARACTERISTIC_UUID, write_data)
                print(f"Sent data: {write_data}")
                self.is_connected = True
                return True
        except asyncio.TimeoutError:
            print("Connection to device timed out")
            self.is_connected = False
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            self.is_connected = False
            return False
        

    # start_notifications(self, char_uuid, callback):
    # begins notification loop after connecting to the client, using the callback method

    # params:
    # char_uuid = the UUID of the bluetooth client to connect to
    # callback = the callback method to be called in the notification loop

    # returns: None

    async def start_notifications(self, char_uuid, callback):
        await self.client.connect()
        while self.is_connected:
            # Read from the characteristic
                await self.client.start_notify(NOTIFY_CHARACTERISTIC_UUID, callback)





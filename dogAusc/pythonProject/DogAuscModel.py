import os
import asyncio
from bleak import BleakClient, BleakScanner
import time

ARDUINO_NAME = "DogAus"
REQUEST_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1215"
NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

class DogAuscModel:
    def __init__(self):
        self.is_connected = False
        self.s1_audio = None
        self.s2_audio = None
        self.s3_audio = None
        self.s4_audio = None

    def set_s1(self, audio):
        self.s1_audio = audio

    def set_s2(self, audio):
        self.s2_audio = audio

    def set_s3(self, audio):
        self.s3_audio = audio

    def set_s4(self, audio):
        self.s4_audio = audio

    def get_s1(self):
        return self.s1_audio

    def get_s2(self):
        return self.s2_audio

    def get_s3(self):
        return self.s3_audio
    
    def get_s4(self):
        return self.s4_audio
    
    async def notification_handler(self, sender, data):
        print(f"{data.decode().split(',')}")


    def connected(self):
        return self.is_connected
    
    def set_connected(self):
        self.is_connected = True

    def disconnect(self):
        self.is_connected = False

        
    async def connect_to_arduino(self):
        device = None

        # Scan for devices
        print("Scanning for devices...")
        devices = await BleakScanner.discover()
        for d in devices:
            print(f"Found device: {d.name}, Address: {d.address}")
            if d.name == ARDUINO_NAME:
                device = d
                break
        # return
        if device is None:
            print(f"Device {ARDUINO_NAME} not found")
            return 404

        print(f"Connecting to {device.name} at {device.address}...")

        try:
            async with BleakClient(device.address, timeout=30.0) as client:
                print(f"Connected to {device.name}")
                self.is_connected = True

                # Write to the characteristic
                write_data = "READ".encode()  # Convert string to bytes
                await client.write_gatt_char(REQUEST_CHARACTERISTIC_UUID, write_data)
                print(f"Sent data: {write_data}")
                
                while self.is_connected:
                # Read from the characteristic
                    await client.start_notify(NOTIFY_CHARACTERISTIC_UUID, self.notification_handler)
        except asyncio.TimeoutError:
            print("Connection to device timed out")
        except Exception as e:
            print(f"An error occurred: {e}")





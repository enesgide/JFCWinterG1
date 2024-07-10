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
        self.client = None

    def set_s1(self, audio):
        self.s1_audio = audio

    def set_s2(self, audio):
        self.s2_audio = audio

    def get_s1(self):
        return self.s1_audio

    def get_s2(self):
        return self.s2_audio


    def connected(self):
        return self.is_connected

    async def client_disconnect(self):
        await self.client.disconnect()
        self.is_connected = False

        
    async def connect_to_arduino(self):
        device = None
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
            return

        print(f"Connecting to {device.name} at {device.address}...")

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
        
    async def start_notifications(self, char_uuid, callback):
        await self.client.connect()
        while self.is_connected:
            # Read from the characteristic
                await self.client.start_notify(NOTIFY_CHARACTERISTIC_UUID, callback)





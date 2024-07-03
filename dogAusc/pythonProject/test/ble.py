import asyncio
import bleak
from bleak import BleakClient, BleakScanner
import time


ARDUINO_NAME = "DogAus"
REQUEST_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1215"
NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

#cvconnect to the arduino device 
async def connect_to_arduino():
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
        return

    print(f"Connecting to {device.name} at {device.address}...")

    try:
        async with BleakClient(device.address, timeout=5.0) as client:
            print(f"Connected to {device.name}")

            # Write to the characteristic
            write_data = "READ".encode()  # Convert string to bytes
            await client.write_gatt_char(REQUEST_CHARACTERISTIC_UUID, write_data)
            print(f"Sent data: {write_data}")
            
            while True:
            # Read from the characteristic
                await client.start_notify(NOTIFY_CHARACTERISTIC_UUID, notification_handler)
    except asyncio.TimeoutError:
        print("Connection to device timed out")
    except Exception as e:
        print(f"An error occurred: {e}")



def notification_handler(sender, data):
    print(f"Received notification from {sender}: {data.decode()}")


# Run the communication function
asyncio.run(connect_to_arduino())



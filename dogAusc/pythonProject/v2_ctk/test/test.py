import pygame
import asyncio
from bleak import BleakClient, BleakScanner

# Constants
ARDUINO_NAME = "DogAus"
REQUEST_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1215"
NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sounds
heart_sound = pygame.mixer.Sound("Demo.wav")
lung_sound = pygame.mixer.Sound("Demo2.wav")

# Start playing sounds on infinite loop
heart_channel = heart_sound.play(-1)
lung_channel = lung_sound.play(-1)

def set_volume(channel, pressure):
    # Map pressure (10-200) to volume (0.0-1.0)
    volume = max(0.0, min(1.0, (pressure - 10) / 190))
    channel.set_volume(volume)
    print(f"Channel volume set to {volume:.2f}")

async def connect_to_arduino():
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
    try:
        async with BleakClient(device.address, timeout=30.0) as client:
            print(f"Connected to {device.name}")
            # Write to the characteristic
            write_data = "READ".encode()  # Convert string to bytes
            await client.write_gatt_char(REQUEST_CHARACTERISTIC_UUID, write_data)
            print(f"Sent data: {write_data}")
            
            # Start notification
            try:
                await client.start_notify(NOTIFY_CHARACTERISTIC_UUID, notification_handler)
                print("Notifications started")
            except Exception as e:
                print(f"Failed to start notifications: {e}")
            
            # Keep the connection alive
            while True:
                await asyncio.sleep(1)

    except asyncio.TimeoutError:
        print("Connection to device timed out")
    except Exception as e:
        print(f"An error occurred: {e}")

def notification_handler(sender, data):
    decoded_data = data.decode()
    print(f"Received notification: {decoded_data}")
    
    # Parse the data
    values = [int(x.strip()) for x in decoded_data.split(',')]
    
    # Get the highest value for each pair
    heart_pressure = max(values[0], values[1])
    lung_pressure = max(values[2], values[3])
    
    # Set the volume for each channel
    set_volume(heart_channel, heart_pressure)
    set_volume(lung_channel, lung_pressure)

# Run the communication function
asyncio.run(connect_to_arduino())

# Keep the script running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
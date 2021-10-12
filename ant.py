# Entry point of the app, the main app will be run here
import itertools

from pynput.keyboard import Key, Listener

from device import Device
from server import Server


def devices_and_server_setup():
    # Create instances of Device
    devices = [Device(8), Device(12), Device(9), Device(15)]
    # create an instance of the server
    server1 = Server(devices)
    return server1


def program_menu():
    print("Press 'a'\t\t: to show all devices on this server.")
    print("Press 'space bar'\t: to automatically assign a job.")
    print("Press 'b'\t\t: to manually assign a job.")


def app():
    server = devices_and_server_setup()

    # display menu
    program_menu()


    # Listen to Keyboard
    def on_press(key):
        try:
            if key.char == 'a':
                print(server)
            elif key.char == 'b':
                print("b pressed ...")
        except AttributeError:
            if key == Key.space:
                print("space pressed")

    def on_release(key):
        if key == Key.esc:
         # stop the listener
         return False

    # Listen to key entry
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    app()

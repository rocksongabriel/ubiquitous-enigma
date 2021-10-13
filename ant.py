# Entry point of the app, the main app will be run here
import itertools

from pynput.keyboard import Key, Listener, Controller

from device import Device
from server import Server
from rich.console import Console

console = Console()
keyboard = Controller()

# variables

# counter to increase the automatic job creation
counter = itertools.count(1)


# keybord utils
def clear_input_key():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    console.print()

def devices_and_server_setup():
    # Create instances of Device
    devices = [Device(8), Device(12), Device(9), Device(15)]
    # create an instance of the server
    server1 = Server(devices)
    return server1


def program_menu():
    console.print("\nPress 'm'\t\t: to show this menu.")
    console.print("Press 's'\t\t: to show all devices on this server.")
    console.print("Press 'a'\t\t: to add a device to this server.")
    console.print("Press 'space bar'\t: to automatically assign a job.")
    console.print("Press 'b'\t\t: to manually assign a job.")
    console.print("Press 'esc' (escape key) to quit the server.")



def manual_job_creation(server):
    """This function will automatically assign a given job_id to a device"""
    clear_input_key()
    job_id = int(input("Enter the 'job id' of the job you want to assign: "))
    console.print("\n")
    server.assign_job(job_id)

def add_device_to_server(server):
    """Add a device to the running server"""
    clear_input_key()
    processing_power = int(input("Enter the processsing power of the device you want to add to this server: "))
    device = Device(processing_power)
    server.add_device(device)
    console.print(f"Device: ({device}) has been added to the server.")


# main application entry
def app():
    server = devices_and_server_setup()

    # display menu
    program_menu()


    # Listen to Keyboard
    def on_press(key):
        try:
            if key.char == 's':
                clear_input_key()
                server.show_devices() # display all devices
            elif key.char == 'a':
                add_device_to_server(server) # add new device to the server
            elif key.char == 'b':
                manual_job_creation(server) # manually create a job, and let the server assign a device
            elif key.char == 'm':
                clear_input_key()
                program_menu()
        except AttributeError:
            if key == Key.space:
                global counter
                clear_input_key()
                server.assign_job(next(counter)) # automatically assign next next

    def on_release(key):
        if key == Key.esc:
         # stop the listener
         return False

    # Listen to key entry
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    app()

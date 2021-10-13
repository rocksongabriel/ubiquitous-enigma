# Entry point of the app, the main app will be run here
import itertools
import time

from pynput.keyboard import Controller, Key, Listener
from rich.console import Console
from rich.table import Table

from device import Device
from server import Server

console = Console()
keyboard = Controller()

# variables

# counter to increase the automatic job creation
counter = itertools.count(1)


# keybord utils
def clear_input_key():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(.100) # give the pynput some time to clear the key the user pressed from the terminal
    console.print()

def devices_and_server_setup():
    # Create instances of Device
    devices = [Device(8), Device(12), Device(9), Device(15)]
    # create an instance of the server
    server1 = Server(devices)
    return server1

def server_start_info():
    console.print("\n[bold yellow]Server running ...[bold yellow]")

def program_menu():
    table = Table(title="[bold yellow]Menu of Ant Colony Optimization Terminal Program.[bold yellow]")

    table.add_column("Command", justify="center", style="cyan", no_wrap=True)
    table.add_column("Purpose", style="blue", no_wrap=True)

    table.add_row("Press 'a'", "[bold blue]add a device to this server.[bold blue]")
    table.add_row("Press 'b'", "[bold blue]to manually assign a job.[bold blue]")
    table.add_row("Press 'd", "[bold blue]show all devices on this server.[bold blue]")
    table.add_row("Press 'm'", "[bold blue]show this menu.[bold blue]")
    table.add_row("Press 's'", "[bold blue]show the status of the server.[bold blue]")
    table.add_row("Press 'space bar'", "[bold blue]automatically assign a job.[bold blue]")
    table.add_row("Press 'esc' (escape key)", "[bold red]quit the server and stop the program.[bold red]")

    console.print(table)

    console.print("[green]Waiting for your input ... [/green]")


def manual_job_creation(server):
    """This function will automatically assign a given job_id to a device"""
    clear_input_key()
    while True:
        try:
            job_id = int(input("Enter the 'job id' of the job you want to assign: "))
            server.assign_job(job_id)
            break
        except ValueError:
            console.print("[red bold]Please enter integer only ...[/red bold]")
            continue 

def add_device_to_server(server):
    """Add a device to the running server"""
    clear_input_key()
    while True:
        try:
            processing_power = float(input("Enter the processsing power of the device you want to add to this server: "))
            device = Device(processing_power)
            server.add_device(device)
            server.show_current_status()
            break
        except ValueError:
            console.print("[yellow red]Please enter decimal or integer only ...[/yellow red]")
            continue    


# main application entry
def app():
    server = devices_and_server_setup()

    # display server start info
    server_start_info()
    # display the status of the server
    server.show_current_status()
    # display menu
    program_menu()


    # Listen to Keyboard
    def on_press(key):
        try:
            if key.char == 'd':
                clear_input_key()
                server.show_devices() # display all devices
            elif key.char == 'a':
                add_device_to_server(server) # add new device to the server
            elif key.char == 'b':
                manual_job_creation(server) # manually create a job, and let the server assign a device
            elif key.char == 's': 
                clear_input_key()
                server.show_current_status() # display the current status of the server
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

# definition of the server and it's functionality


class Server:
    """
    Create a device, passing to the constructor the initial devices
    """
    def __init__(self, devices=[]):
        self.devices = devices
    
    def add_device(self, device):
        self.devices.append(device)

    def add_devices(self, devices):
        self.devices.extend(devices)

    @property
    def get_devices(self):
        """print the devices by their IDs"""
        return [device.device_id for device in self.devices]

    @property
    def get_number_of_devices(self):
        """get the total number of devices connected to this server"""
        return len(self.devices)

    def assign_job(self, job_id):
        if len(self.devices < 1):
            print("There are no devices connected to the server, please connect a device ...")
        else:
            pass
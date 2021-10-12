# definition of the server and it's functionality
import operator


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
        return self.devices
    
    def remove_all_devices(self):
        """disconnect all devices from the server"""
        self.devices = []

    @property
    def get_number_of_devices(self):
        """get the total number of devices connected to this server"""
        return len(self.devices)

    def assign_job(self, job_id):
        if not self.devices:
            print("There are no devices connected to the server, please connect a device ...")
        else:
            pass

    def sort_devices(self):
        """This method will sort devices on this server according to pheromone level"""
        return sorted(self.get_devices, key=operator.attrgetter("get_pheromone_level"), reverse=True)

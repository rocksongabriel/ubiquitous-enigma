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
            # device to assign job to
            device = self.sort_devices()[0]
            # assign currently assigned job
            device.set_current_assigned_job(job_id)
            # increase the device's number of tasks
            device.increase_number_of_tasks()
            # recalculate the pheromone level of the device
            device.calculate_pheromone_level()

    def sort_devices(self):
        """This method will sort devices on this server according to pheromone level"""
        return sorted(self.get_devices, key=operator.attrgetter("get_pheromone_level"), reverse=True)

    @staticmethod
    def display_info_on_assigned_job(device, job_id):
        print(f"Job with Job ID: {job_id} has been assigned to device with Device ID: {device.device_id}")
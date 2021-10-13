# definition of the server and it's functionality
import operator
import pprint
from rich.console import Console

console = Console()


class Server:
    """
    Create a device, passing to the constructor the initial devices
    """
    def __init__(self, devices=[]):
        self.devices = devices
        self.all_jobs = {} # the key is the job's ID, the value is the assigned Device
    
    # managing devices interface 

    def add_device(self, device):
        self.devices.append(device)

    def add_devices(self, devices):
        self.devices.extend(devices)

    @property
    def get_devices(self):
        """return the devices"""
        return self.devices

    def show_devices(self):
        """nicely display the devices on the server"""
        console.print(self.get_devices)
    
    def remove_all_devices(self):
        """disconnect all devices from the server"""
        self.devices = []

    @property
    def get_number_of_devices(self):
        """get the total number of devices connected to this server"""
        return len(self.devices)

    def _sort_devices(self):
        """This method will sort devices on this server according to pheromone level"""
        return sorted(self.get_devices, key=operator.attrgetter("get_pheromone_level"), reverse=True)

    # all jobs managing interface
    def _add_job(self, job_id, assigned_device):
        self.all_jobs[job_id] = assigned_device

    # TODO add ability to reasign jobs, i.e: a particular job can be reassigned

    @property
    def get_all_jobs(self):
        return self.all_jobs

    def show_all_jobs(self):
        pprint.pprint(self.get_all_jobs)

    # job assignment interface

    def assign_job(self, job_id):
        if not self.devices:
            console.print("There are no devices connected to the server, please connect a device ...")
        else:
            device = self._sort_devices()[0] # device to assign job to
            device.set_current_assigned_job(job_id) # assign currently assigned job
            device.increase_number_of_tasks() # increase the device's number of tasks
            device.calculate_pheromone_level() # recalculate the pheromone level of the device
            if job_id not in self.get_all_jobs.keys():
                self._add_job(job_id, device) # add job to all jobs
                self.display_info_on_assigned_job(device, job_id)
            else:
                console.print(
                    f"Job ID: [bold blue]{job_id}[/bold blue] is currently assigned to: Device with ID: {self.get_all_jobs[job_id].device_id}"
                    )
                console.print(
                    f"Status of device: {device.get_device_status()}\n"
                )


    @staticmethod
    def display_info_on_assigned_job(device, job_id):
        device_status = {
            "Pheromone Level": device.get_pheromone_level, 
            "Number of Tasks": device.get_number_of_tasks
        }
        console.print(f"Job with Job ID: [bold red]{job_id}[/bold red] has been assigned to device with Device ID: [bold red]{device.device_id}[/bold red], \nCurrent Status of Device: {device_status}\n")

    def __repr__(self):
        return f"Server(devices={self.devices})"

    def __str__(self):
        return f"Server: Devices = {self.devices}"
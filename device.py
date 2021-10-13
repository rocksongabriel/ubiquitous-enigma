# definition of the Device and it's functionality
import uuid
from rich.console import Console

console = Console()


class Device:
    """
    Create a device, passing the constructor the device's processing power
    """

    def __init__(self, processing_power):
        self.device_id = uuid.uuid4() # a devices id is unique, so it is generated when the devices is being added to the server
        self.processing_power = processing_power
        self.number_of_tasks = 0
        self.pheromone_level = 0
        self.calculate_pheromone_level() # calculate the pheromone level when the device is created
        self.current_assigned_job = 0 # zero means no job jas been assigned currently, this will be set by the server

    # number of tasks interface code 

    def increase_number_of_tasks(self):
        self.number_of_tasks += 1

    @property
    def get_number_of_tasks(self):
        return self.number_of_tasks

    # pheromone level interface code

    def calculate_pheromone_level(self):
        """calculate the pheromone level based on the processing power and the assigned tasks"""
        self.pheromone_level =  self.processing_power / (1 + self.number_of_tasks)
    
    @property
    def get_pheromone_level(self):
        return self.pheromone_level

    # processing power interface 

    @property
    def get_processing_power(self):
        return self.processing_power

    def set_processing_power(self, power):
        self.processing_power = power

    # currently assingned job interface 

    def set_current_assigned_job(self, job_id):
        self.current_assigned_job = job_id

    @property
    def get_current_assigned_job(self):
        return self.current_assigned_job

    def remove_current_assigned_job(self):
        self.current_assigned_job = 0

    # device representations 

    def show_device_details(self):
        return f"Device ID: {self.device_id}, Pheromone Level: {self.get_pheromone_level}, Processing Power: {self.get_processing_power}, Number of Tasks: {self.get_number_of_tasks}"

    def __repr__(self):
        return f"Device(device_id={self.device_id}, processing_power={self.get_processing_power}, pheromone_level={self.get_pheromone_level}, number_of_tasks={self.get_number_of_tasks})"

    def __str__(self):
        return f"(Device ID: {self.device_id}, Pheromone Level: {self.get_pheromone_level}, Processing Power: {self.get_processing_power}, Number of Tasks: {self.get_number_of_tasks})"
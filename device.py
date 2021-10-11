# definition of the Device and it's functionality
import uuid


class Device:
    """
    Create a device, passing the constructor the device's processing power
    """

    def __init__(self, processing_power):
        self.device_id = uuid.uuid4() # a devices id is unique, so it is generated when the devices is being added to the server
        self.processing_power = processing_power
        self.number_of_tasks = 0
        self.pheromone_level = 0
        self.caculate_pheromone_level() # calculate the pheromone level when the device is created
        self.current_assigned_job = 0 # zero means no job jas been assigned currently, this will be set by the server

    def increase_number_of_tasks(self):
        self.number_of_tasks += 1

    @property
    def get_number_of_tasks(self):
        return self.number_of_tasks

    def caculate_pheromone_level(self):
        """calculate the pheromone level based on the processing power and the assigned tasks"""
        self.pheromone_level =  self.processing_power / (1 + self.number_of_tasks)
    
    @property
    def get_pheromone_level(self):
        return self.pheromone_level

    def set_current_assigned_job(self, job_id):
        self.current_assigned_job = job_id

    @property
    def get_current_assigned_job(self):
        return self.current_assigned_job

    def remove_current_assigned_job(self):
        self.current_assigned_job = 0

    def show_device_details(self):
        return f"Device ID: {self.device_id}, Processing Power: {self.processing_power}, Number of Tasks: {self.number_of_tasks}, Pheromone Level: {self.pheromone_level}"

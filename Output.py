from abc import ABC, abstractclassmethod

class OutputData(ABC):
    def __init__(self, output_type):
        self.output_type = output_type

    @abstractclassmethod
    def output_data(self):
        pass

class WriteToFile(OutputData):
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    def output_data(self):
        print("I am printing to file")
        
class WriteToDatabase(OutputData):
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    def output_data(self):
        print("I am sending to db")
    
        
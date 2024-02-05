from abc import ABC, abstractclassmethod

class OutputData(ABC):

    @abstractclassmethod
    def output_data(self):
        pass

class WriteToFile(OutputData):
    #def __init__(self, temperature, humidity):
        #self.temperature = temperature
        #self.humidity = humidity

    def output_data(self,data):
        print("I am printing to file")
        
class WriteToDatabase(OutputData):
    #def __init__(self):
        
    def output_data(self,data):
        print("I am sending to db")
    
class DataOutputFactory:
    data_output_types = {
        'file': WriteToFile,
        'cosmos_db': WriteToDatabase
    }

    def create_data_output_method(self,data_output_type):
        data_output_class = self.data_output_types.get(data_output_type.lower())
        if data_output_class:
            return data_output_class()
        else:
            raise ValueError("Invalid data output type")       
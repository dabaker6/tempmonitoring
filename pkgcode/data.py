from abc import ABC, abstractmethod
from typing import Dict

#@abstract method provides the interface
#use this to pass data to output, enforce that a dictionary is needed?

class Data(ABC):
    def __init__(self, temperature, humidity):
        self.__set_temperature(temperature)
        self.__set_humidity(humidity)
    
    @abstractmethod
    def data(self) -> Dict[str,float]:
        pass

    def __set_temperature(self, temperature):
        if not isinstance(temperature,float):
            raise ValueError("temperature must be of type: float")
        self.temperature = temperature

    def __set_humidity(self, humidity):
        if not isinstance(humidity,float):
            raise ValueError("humidity must be of type: float")
        self.humidity = humidity

class DataToSend(Data):

    def data(self):
        
        data = dict(
            temperature=self.temperature,
            humidity=self.humidity
        )

        return data
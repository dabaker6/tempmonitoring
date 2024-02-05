from abc import ABC, abstractmethod
import time
import random
from typing import Dict
from pkgcode.data import DataToSend
from maincode.configmanager import ConfigManager
#@abstract method provides the interface
#use this to pass data to output, enforce that a dictionary is needed?

class DataGeneration(ABC):
    @abstractmethod
    def input_data(self):
        pass

class DHTSensor(DataGeneration):
    
    try:
        import RPi.GPIO as GPIO
        import pkgcode.Freenove_DHT as DHT
    except ImportError:
        print("module not available")

    def __init__(self):
        config_manager = ConfigManager()
        dht_pin = config_manager.config.get('PARAMETERS','DHTPin')
        self.__dht = DHT.DHT(dht_pin)   #create a DHT class object

    def input_data(self):
        
        for i in range(0,15):            
            chk = self.__dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print(i)
            if (chk is self.__dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print("DHT11,OK!")
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(self.__dht.humidity,self.__dht.temperature))

        return(DataToSend(self.__dht.temperature,self.__dht.humidity))

class RandomData(DataGeneration):
    
    def input_data(self):
            
        temperature = 19 + (random.randint(0,9)/100)
        humidity = 80 + (random.randint(0,9)/100)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(humidity,temperature))
        
        return DataToSend(temperature, humidity)

class SensorFactory:
    sensor_types = {
        'sensor': DHTSensor,
        'random': RandomData
    }

    def create_sensor(self,sensor_type):
        sensor_class = self.sensor_types.get(sensor_type.lower())
        if sensor_class:
            return sensor_class()
        else:
            raise ValueError("Invalid sensor type")

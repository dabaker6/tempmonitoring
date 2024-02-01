from abc import ABC, abstractmethod
import time
import random

class DataGenerationMethod(ABC):
    @abstractmethod
    def input_data(self):
        pass

class GenerateDataFromSensor(DataGenerationMethod):
    
    try:
        import RPi.GPIO as GPIO
        import Freenove_DHT as DHT
    except ImportError:
        print("module not available")

    def input_data(self):
        dht = DHT.DHT(DHTPin)   #create a DHT class object
        counts = 0 # Measurement counts
        while(True):
            counts += 1
            print("Measurement counts: ", counts)
            for i in range(0,15):            
                chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print(i)
                if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                    print("DHT11,OK!")
                    break
                time.sleep(0.1)
            print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
            time.sleep(2)

class GenerateDataFromRandom(DataGenerationMethod):
    
    def input_data(self):
        counts = 0
        while(True):
            counts +=1
            print("Measurement counts: %d" %counts)
            temperature = 19 + (random.randint(0,9)/100)
            humidity = 80 + (random.randint(0,9)/100)
            print("Humidity : %.2f, \t Temperature : %.2f \n"%(humidity,temperature))
            time.sleep(2)

class GenerateDataFactory:
    data_generation_types = {
        'sensor': GenerateDataFromSensor,
        'random': GenerateDataFromRandom
    }

    def create_data_generation_method(self,data_generation_type):
        data_generation_class = self.data_generation_types.get(data_generation_type.lower())
        if data_generation_class:
            return data_generation_class()
        else:
            raise ValueError("Invalid data generation type")

if __name__ == '__main__':
    print ('Program is starting ... ')
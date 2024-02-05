import sys
sys.path.append('../tempmonitoring')

from pkgcode.input import SensorFactory
from pkgcode.output import DataOutputFactory
from maincode.configmanager import ConfigManager

import time

class GenerateData():
    
    config_manager = ConfigManager()
    sensor_type = config_manager.config.get('PARAMETERS','sensor_type')
    output_type = config_manager.config.get('PARAMETERS','data_output_type')
    sensor_factory = SensorFactory()
    sensor = sensor_factory.create_sensor(sensor_type)
    data_output_factory = DataOutputFactory()
    data_output = data_output_factory.create_data_output_method(output_type)
    
    def loop(self):

        counts = 0
        while(True):
            counts+=1
            print("Measurement counts: %d" %counts)
            data = self.sensor.input_data()
            self.data_output.output_data(data)
            time.sleep(2)

if __name__ == '__main__':
    print ('Program is starting ....')

    try:
        data_generation = GenerateData()        
        data_generation.loop()
    except KeyboardInterrupt:
        #GPIO.cleanup()
        exit()  

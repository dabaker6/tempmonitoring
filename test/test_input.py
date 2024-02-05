import unittest
import sys
sys.path.append('../tempmonitoring')
from pkgcode.input import SensorFactory, RandomData
from pkgcode.data import DataToSend

class Input(unittest.TestCase):
    
    def setUp(self):
        sensor_type = 'random'
        
        sensor_factory = SensorFactory()
        
        self.sensor = sensor_factory.create_sensor(sensor_type)

    def test_sensor_factory(self):
        
        self.assertIsInstance(self.sensor,RandomData)

    def test_sensor_input_class(self):
        data = self.sensor.input_data()
        self.assertIsInstance(data,DataToSend)

    def test_sensor_input_values(self):
        data = self.sensor.input_data()
        
        self.assertIsInstance(data.temperature,float)
        self.assertIsInstance(data.humidity,float)
        self.assertIsInstance(data.timestamp,float)
        
if __name__ == '__main__':
    unittest.main()        

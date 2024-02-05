import unittest
import sys
sys.path.append('/home/david/repos/tempmonitoring')
from pkgcode.data import DataToSend
from datetime import datetime

class Data(unittest.TestCase):

    

    def test_temperature_return(self):
        
        temperature = 20.0
        humidity = 80.0

        data = DataToSend(temperature,humidity)
        
        self.assertEqual(data.temperature, temperature,'the temperature is wrong')
        
    def test_humidity_return(self):
        
        temperature = 20.0
        humidity = 80.0
        
        data = DataToSend(temperature,humidity)
        
        self.assertEqual(data.humidity, humidity, 'the humidity is wrong')

    def test_timestamp_return(self):
        
        temperature = 20.0
        humidity = 80.0
        
        now = datetime.now().timestamp()

        data = DataToSend(temperature,humidity)
        
        self.assertAlmostEqual(data.timestamp, now, places=4,msg='the timestamp is wrong')
    
    def test_temperature_input(self):
        temperature = "20"
        humidity = 80.5
        with self.assertRaises(ValueError) as context:
            DataToSend(temperature,humidity)

        self.assertEqual(str(context.exception), "temperature must be of type: float")

    def test_humidity_input(self):
        temperature = 20.4
        humidity = "80"
        with self.assertRaises(ValueError) as context:
            DataToSend(temperature,humidity)

        self.assertEqual(str(context.exception), "humidity must be of type: float")

if __name__ == '__main__':
    unittest.main()
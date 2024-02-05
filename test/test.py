import unittest
import sys
sys.path.append('/home/david/repos/tempmonitoring')
from pkgcode.data import DataToSend

class TestData(unittest.TestCase):

    def test_temperature_return(self):
        
        temperature = 20
        humidity = 80
        
        data = DataToSend(temperature,humidity)
        
        self.assertEqual(data.temperature, temperature,'the temperature is wrong')
        
    def test_humidity_return(self):
        
        temperature = 20
        humidity = 80
        
        data = DataToSend(temperature,humidity)
        
        self.assertEqual(data.humidity, humidity, 'the humidity is wrong')
    
    def test_temperature_input(self):
        temperature = "20"
        humidity = 80
        with self.assertRaises(ValueError) as context:
            DataToSend(temperature,humidity)

        self.assertEqual(str(context.exception), "temperature must be an integer")

    def test_humidity_input(self):
        temperature = 20
        humidity = "80"
        with self.assertRaises(ValueError) as context:
            DataToSend(temperature,humidity)

        self.assertEqual(str(context.exception), "humidity must be an integer")

if __name__ == '__main__':
    unittest.main()
import unittest
import sys
sys.path.append('../tempmonitoring')
from pkgcode.output import DataOutputFactory, WriteToFile

class Input(unittest.TestCase):
    
    def setUp(self):
        
        output_type = 'file'
        
        output_factory = DataOutputFactory()
        
        self.output_data = output_factory.create_data_output_method(output_type)
    
    def test_data_output_factory(self):

        self.assertIsInstance(self.output_data,WriteToFile)

if __name__ == '__main__':
    unittest.main()        

import sys
from input import GenerateDataFactory  

if __name__ == '__main__':
    print ('Program is starting ....')
    DHTPin = int(sys.argv[1])
    dataGenerationType = str(sys.argv[2])
    try:
        factory = GenerateDataFactory()
        gendata = factory.create_data_generation_method(dataGenerationType)
        gendata.input_data()
        
    except KeyboardInterrupt:
        #GPIO.cleanup()
        exit()  

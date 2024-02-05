from input import GenerateDataFactory  
from configmanager import ConfigManager
from data import DataToSend

if __name__ == '__main__':
    print ('Program is starting ....')
    
    #datatoSend = DataToSend(20,80)

    #print(datatoSend.data())

    #exit()

    config_manager = ConfigManager()
    
    DHTPin = config_manager.config.get('PARAMETERS','DHTPin')
    dataGenerationType = config_manager.config.get('PARAMETERS','dataGenerationType')
    try:
        factory = GenerateDataFactory()
        gendata = factory.create_data_generation_method(dataGenerationType)
        gendata.input_data()
        
    except KeyboardInterrupt:
        #GPIO.cleanup()
        exit()  

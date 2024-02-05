import configparser

class ConfigManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = configparser.ConfigParser()
            try:
                filename = 'maincode/config.ini'
                cls._instance._config.read_file(open(filename))
            except FileNotFoundError:
                print('file: %s not found, please amend and try again' %filename)
                print('exiting')
                exit()
        return cls._instance
    
    @property
    def config(self):
        return self._config
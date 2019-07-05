import configparser

class Config: 
    """Extract configuration from ini"""
    
    def __init__(self):
        self.config = configparser.ConfigParser()
    
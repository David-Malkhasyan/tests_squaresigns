import configparser

config = configparser.RawConfigParser
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL(self):
        url = config.get('common info dev', 'baseURL')

    @staticmethod
    def getUserEmail(self):
        url = config.get('common info dev', 'userEmail')

    @staticmethod
    def getPassword(self):
        url = config.get('common info dev', 'password')
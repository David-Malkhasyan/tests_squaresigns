import configparser

config = configparser.RawConfigParser
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url(self):
        url = config.get('common info dev', 'baseURL')

    @staticmethod
    def get_user_email(self):
        user_email = config.get('common info dev', 'userEmail')

    @staticmethod
    def get_password(self):
        passwrod = config.get('common info dev', 'password')

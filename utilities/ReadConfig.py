import configparser
from utilities import ProjectRoot

config = configparser.RawConfigParser()
project_root = ProjectRoot.get_project_root()
config.read(project_root + '/Configuration/config.ini')


class ReadConfig:

    @staticmethod
    def get_application_url() -> str:
        app_url = config.get('Basic Info', 'application_url')
        return app_url

    @staticmethod
    def get_login_username() -> str:
        username = config.get('Basic Info', 'username')
        return username

    @staticmethod
    def get_login_pwd() -> str:
        pwd = config.get('Basic Info', 'password')
        return pwd

    @staticmethod
    def get_chromedriver_path() -> str:
        chrome_path = config.get('Drivers Info', 'chromedriver_path')
        return project_root + chrome_path

    @staticmethod
    def get_firefoxdriver_path() -> str:
        firefox_path = config.get('Drivers Info', 'firefoxdriver_path')
        return project_root + firefox_path

    @staticmethod
    def get_edgedriver_path() -> str:
        edge_path = config.get('Drivers Info', 'edgedriver_path')
        return project_root + edge_path

    @staticmethod
    def get_logfile_path() -> str:
        log_path = config.get('Log File Info', 'logfile_path')
        return project_root + log_path



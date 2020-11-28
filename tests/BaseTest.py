import pytest
import logging
from utilities.ReadConfig import ReadConfig

log_path = ReadConfig.get_logfile_path()


@pytest.mark.usefixtures('setup')
class Base:

    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        file_handler =logging.FileHandler(log_path)

        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        return logger





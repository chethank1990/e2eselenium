import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures( "setup" )
class BaseClass:

    def selectDropDown(self,dropdownlocator,text):
        dropdown = Select(dropdownlocator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]                                                        # some log pulling method
        logger = logging.getLogger(loggerName)                                                    # defining logger service & linking with pulling method
        fileHandler = logging.FileHandler('logfile.log')                                          # where logger should log
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")       # what is present in the log
        fileHandler.setFormatter(formatter)                                                       # connection between filehandler & formatter
        logger.addHandler(fileHandler)                                                            # link logger and filehandler
        logger.setLevel(logging.DEBUG)                                                            # setting log level
        return logger
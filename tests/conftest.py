import pytest
from selenium import webdriver
from utilities.ReadConfig import ReadConfig

chromedriver_path = ReadConfig.get_chromedriver_path()
app_url = ReadConfig.get_application_url()

driver = None


@pytest.fixture
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(app_url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    request.cls.driver = driver     # assign this driver to the calling class's driver
    yield
    driver.quit()



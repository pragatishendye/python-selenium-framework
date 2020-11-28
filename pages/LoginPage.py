from pages.HomePage import HomePage


class LoginPage:

    __username = 'uid'
    __password = 'password'
    __login_button = 'btnLogin'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, uname):
        user_name = self.driver.find_element_by_name(self.__username)
        user_name.clear()
        user_name.send_keys(uname)

    def enter_password(self, pwd):
        passwd = self.driver.find_element_by_name(self.__password)
        passwd.clear()
        passwd.send_keys(pwd)

    def click_login(self) -> HomePage:
        self.driver.find_element_by_name(self.__login_button).click()
        return HomePage(self.driver)


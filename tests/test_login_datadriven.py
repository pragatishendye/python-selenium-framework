from tests.BaseTest import Base
from pages.LoginPage import LoginPage
import pytest

num = 1


class TestLoginDD(Base):

    #@pytest.mark.parametrize('username, password', [('mngr293774', 'zAtujUs'), ('mngr293774', ''), ('', 'zAtujUs'),
                                            #('', '')])
    @pytest.mark.parametrize('username, password', [('mngr293774', 'zAtujUs')])
    def test_login_dd(self, username, password):
        global num
        log = Base.get_logger()
        log.info('**********Running Data-driven Login Test**********')
        lp = LoginPage(self.driver)
        log.info(f'Testing with data set {num}...')
        lp.enter_username(username)
        lp.enter_password(password)
        hp = lp.click_login()
        log.info('Logging in...')
        if 'Welcome To Manager\'s Page' in hp.get_welcome_text():
            log.info('Logged in successfully...')
            hp.click_logout()
            TestLoginDD.go_home(self.driver)
        else:
            log.info('Could not log in')
            self.driver.refresh()

        num += 1


    @staticmethod
    def go_home(driver):
        driver.get('http://demo.guru99.com/V4/index.php')








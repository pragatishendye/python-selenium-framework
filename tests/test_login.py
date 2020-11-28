from tests.BaseTest import Base
from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig

username = ReadConfig.get_login_username()
password = ReadConfig.get_login_pwd()


class TestLogin(Base):

    def test_login(self):
        log =Base.get_logger()
        lp = LoginPage(self.driver)
        log.info('**********Running Login Test**********')
        log.info('Entering username...')
        lp.enter_username(username)
        log.info('Entering password...')
        lp.enter_password(password)
        hp = lp.click_login()
        log.info('Logging in...')
        assert 'Welcome To Manager\'s Page' in hp.get_welcome_text(), 'Incorrect welcome text'
        assert hp.get_homepage_title() == 'Guru99 Bank Manager HomePage'
        log.info('Successfully logged in and landed on home page...')
        log.info('**********Login Test Passed**********')


    def test_alert(self):
        log = Base.get_logger()
        lp = LoginPage(self.driver)
        log.info('**********Running Login Test**********')
        log.info('Entering username...')
        lp.enter_username(username)
        log.info('Entering password...')
        lp.enter_password(password)
        hp = lp.click_login()





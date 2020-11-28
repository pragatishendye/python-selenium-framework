from tests.BaseTest import Base
from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig

username = ReadConfig.get_login_username()
password = ReadConfig.get_login_pwd()


class TestHomePage(Base):

    def test_homepagelinks(self):
        log = Base.get_logger()
        lp = LoginPage(self.driver)
        log.info('**********Running Home Page Links Test**********')
        log.info('Logging into application...')
        lp.enter_username(username)
        lp.enter_password(password)
        hp = lp.click_login()

        assert hp.get_homepage_title() == 'Guru99 Bank Manager HomePage'
        log.info('Successfully logged in and landed on home page...')

        expected_numberOf_links = 15

        expected_links_text = ['Manager', 'New Customer', 'Edit Customer', 'Delete Customer', 'New Account',
                               'Edit Account', 'Delete Account', 'Deposit', 'Withdrawal', 'Fund Transfer', 'Change Password',
                               'Balance Enquiry', 'Mini Statement', 'Customised Statement', 'Log out']

        assert hp.get_numberOf_links() == expected_numberOf_links
        log.info('Verified number of links on home page...')

        actual_links_text = hp.get_links_text()
        assert actual_links_text == expected_links_text
        log.info('Verified links on home page...')
        log.info('**********Home Page Links Test Passed**********')





from tests.BaseTest import Base
from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig

username = ReadConfig.get_login_username()
password = ReadConfig.get_login_pwd()


class TestEditCustomer(Base):

    def test_edit_customer_state(self):
        log = Base.get_logger()
        lp = LoginPage(self.driver)
        log.info('**********Running Edit Customer State Test**********')
        log.info('Logging into application...')
        lp.enter_username(username)
        lp.enter_password(password)
        hp = lp.click_login()

        new_state = 'England'
        log.info('Clicking on Edit Customer...')
        ec = hp.click_edit_customer()
        ec.enter_cust_id('26285')
        log.info('Entered customer ID...')
        nc = ec.click_submit()
        nc.enter_cust_state(new_state)
        log.info('Modified the state value...')
        ncr = nc.click_form_submit()
        log.info('Submitted the change...')

        assert ncr.get_status_msg() == 'Customer details updated Successfully!!!'
        assert ncr.get_cust_state() == new_state
        log.info('Customer state updated successfully...')
        log.info('**********Edit Customer State Test Passed**********')

        # 26285 - Pavani
        # 68098 - Tommy




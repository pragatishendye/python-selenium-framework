from tests.BaseTest import Base
from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig

username = ReadConfig.get_login_username()
password = ReadConfig.get_login_pwd()


class TestAddNewCustomer(Base):

    def test_add_new_customer(self):
        log = Base.get_logger()
        lp = LoginPage(self.driver)
        log.info('**********Running Add New Customer Test**********')
        log.info('Logging into application...')
        lp.enter_username(username)
        lp.enter_password(password)
        hp = lp.click_login()
        log.info('Clicking on New Customer link...')

        nc = hp.click_new_customer()
        log.info('Entering customer details...')
        nc.enter_cust_name('Tommy')
        nc.enter_cust_gender()
        nc.enter_cust_dob('23061978')
        nc.enter_cust_address('1290 Treetop view')
        nc.enter_cust_city('Paris')
        nc.enter_cust_state('France')
        nc.enter_cust_pincode('365422')
        nc.enter_cust_phonenumber('9845339211')
        nc.enter_cust_email('qhg12@rediffmail.com')
        nc.enter_cust_password('test123')
        log.info('Submitting the form...')
        ncr = nc.click_form_submit()

        assert ncr.get_status_msg() == 'Customer Registered Successfully!!!'
        log.info('Successfully registered the customer...')
        new_cust_id = ncr.get_new_cust_id()
        print('A new customer with ID {} has been registered'.format(new_cust_id))
        log.info(f'A new customer with ID {new_cust_id} has been registered...')
        log.info('**********Add New Customer Test Passed**********')



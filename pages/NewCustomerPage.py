from pages.NewCustomerRegisteredPage import NewCustRegistered


class NewCustomer:

    __cust_name = 'name'
    __cust_gender = "//input[@value='f']"
    __cust_dob = 'dob'
    __cust_address = 'addr'
    __cust_city = 'city'
    __cust_state = 'state'
    __cust_pincode = 'pinno'
    __cust_phone = 'telephoneno'
    __cust_email = 'emailid'
    __cust_pwd = 'password'
    __custform_submit = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_cust_name(self, name):
        cname = self.driver.find_element_by_name(self.__cust_name)
        cname.clear()
        cname.send_keys(name)

    def enter_cust_gender(self):
        self.driver.find_element_by_xpath(self.__cust_gender).click()

    def enter_cust_dob(self, date):
        self.driver.find_element_by_id(self.__cust_dob).send_keys(date)

    def enter_cust_address(self, address):
        addr = self.driver.find_element_by_name(self.__cust_address)
        addr.clear()
        addr.send_keys(address)

    def enter_cust_city(self, city):
        city_name = self.driver.find_element_by_name(self.__cust_city)
        city_name.clear()
        city_name.send_keys(city)

    def enter_cust_state(self, state):
        state_name = self.driver.find_element_by_name(self.__cust_state)
        state_name.clear()
        state_name.send_keys(state)

    def enter_cust_pincode(self, pin):
        pincode = self.driver.find_element_by_name(self.__cust_pincode)
        pincode.clear()
        pincode.send_keys(pin)

    def enter_cust_phonenumber(self, number):
        ph = self.driver.find_element_by_name(self.__cust_phone)
        ph.clear()
        ph.send_keys(number)

    def enter_cust_email(self, email):
        emailid = self.driver.find_element_by_name(self.__cust_email)
        emailid.clear()
        emailid.send_keys(email)

    def enter_cust_password(self, pwd):
        passwd = self.driver.find_element_by_name(self.__cust_pwd)
        passwd.clear()
        passwd.send_keys(pwd)

    def click_form_submit(self):
        self.driver.find_element_by_xpath(self.__custform_submit).click()
        return NewCustRegistered(self.driver)





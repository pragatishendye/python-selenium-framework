from pages.NewCustomerPage import NewCustomer


class EditCustomer:

    __cust_id = 'cusid'
    __submit_button = 'AccSubmit'

    def __init__(self, driver):
        self.driver = driver

    def enter_cust_id(self, id):
        self.driver.find_element_by_name(self.__cust_id).send_keys(id)

    def click_submit(self):
        self.driver.find_element_by_name(self.__submit_button).click()
        return NewCustomer(self.driver)


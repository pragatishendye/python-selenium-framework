class NewCustRegistered:

    __newcust_id = "//td[(text()='Customer ID')]/following-sibling::td"
    __status_msg = 'p.heading3'
    __cust_state = "//td[text()='State']/following-sibling::td"

    def __init__(self, driver):
        self.driver = driver

    def get_new_cust_id(self) -> str:
        return self.driver.find_element_by_xpath(self.__newcust_id).text

    def get_status_msg(self) -> str:
        return self.driver.find_element_by_css_selector(self.__status_msg).text

    def get_cust_state(self) -> str:
        return self.driver.find_element_by_xpath(self.__cust_state).text


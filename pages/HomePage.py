from pages.NewCustomerPage import NewCustomer
from pages.EditCustomer import EditCustomer


class HomePage:

    __welcome_text = 'heading3'
    __page_links = "//ul[@class='menusubnav']/li/a"

    def __init__(self, driver):
        self.driver = driver

    def get_welcome_text(self):
        return self.driver.find_element_by_class_name(self.__welcome_text).text

    def get_homepage_title(self):
        return self.driver.title

    def get_numberOf_links(self):
        return len(self.driver.find_elements_by_xpath(self.__page_links))

    def get_links_text(self) -> list:
        links = self.driver.find_elements_by_xpath(self.__page_links)
        links_text = list()
        for link in links:
            links_text.append(link.text)
        return links_text

    def click_new_customer(self) -> NewCustomer:
        self.__click_link('New Customer')
        return NewCustomer(self.driver)

    def click_edit_customer(self) -> EditCustomer:
        self.__click_link('Edit Customer')
        return EditCustomer(self.driver)

    def click_logout(self):
        self.__click_link('Log out')

    def __click_link(self, link_text):
        self.driver.find_element_by_link_text(link_text).click()




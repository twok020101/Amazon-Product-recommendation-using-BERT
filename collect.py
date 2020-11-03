"""File that searches for the input and calls for verification
    This is developed using selenium.
    """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
import check_name


"""Intilization of selenium and connectiong it to browser"""

driver=webdriver.Edge("C:\Program Files (x86)\msedgedriver")
driver.get("https://www.amazon.in")

class webby(object):

    def search(self,name):
        """Searches for the given input on www.amazon.in"""
        driver.implicitly_wait(5)
        self.search=driver.find_element_by_id("twotabsearchtextbox")
        self.search.clear()
        self.search.send_keys(name)
        self.search.send_keys(Keys.RETURN)
        print("Search over")


    def best_seller(self):
        """Searches for the link that connects to the top 100 best selling product"""
        driver.implicitly_wait(5)
        self.links=[]
        self.final=[]
        self.elems = driver.find_elements_by_class_name("a-link-normal")
        for self.elem in self.elems:
            self.links.append(self.elem.get_attribute("href"))
        for self.link in self.links:
            if "bestsellers" in self.link:
                self.final.append(self.link)

        return (self.final)

    def runner(self,name):
        """Used from running from main"""
        webby.search(self,name)
        x=webby.best_seller(self)
        print(x)
        print("Best seller links")
        if (x!=[]):
            print("Entering check_name")
            check_name.checker.collect(self,x,name)
        else:
            quit()










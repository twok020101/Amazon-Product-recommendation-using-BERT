"""File that checks whether that link found represents correct product"""
import selenium
from selenium import webdriver
import link_collector

driver=webdriver.Edge("C:\Program Files (x86)\msedgedriver")

class checker(object):

    def collect(self,links,name):
        """Connects to other files and gets the link found in collect
        :param links list of all the best seller links
        :returns correct link"""
        driver.implicitly_wait(5)
        self.test=[]
        print(name)
        for self.link in links:
            driver.implicitly_wait(5)
            driver.get(self.link)
            if (checker.check(self,name)):
                self.test.append(self.link)
        print(self.test)
        if (self.test!=[]):
            print("Entering link collector")
            link_collector.collector.collect(self,self.test,name)
        else:
            quit()


    def check(self,name):
        """Checks whether the link represnts the correct product
        :returns bool"""
        flag=False
        t=driver.find_elements_by_xpath("//*[@id='zg-right-col']/h1/span")
        for elem in t:
            if (name)in(elem.text):
                flag=True
        return flag

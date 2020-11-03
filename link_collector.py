"""File that collects all links from the correct product best seller website after"""
import selenium
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
import time
import comment_collector

driver=wb.Edge("C:\Program Files (x86)\msedgedriver")

class collector(object):

    def collect(self,links,name):
        """Connects the file and returns the final list of links
        :param link - Website from where all links have to be obtained
        :returns list of links of products"""
        self.f_link=[]
        for link in links:
            print(links)
            print(link)
            driver.implicitly_wait(5)
            driver.get(link)
            t=collector.working(self)
            for self.l in t[0:6]:
                self.f_link.append(self.l)
            print(f"Appened from {link}")
        print("Entering comment collector")
        comment_collector.collector.collect(self,self.f_link,name)


    def working(self):
        """Function that retrives all the links of the products
        :returns list of links of products"""
        listOflinks =[]
        condition =True
        count=0
        while condition:
            time.sleep(3)
            for i in range (5):
                productInfoList=driver.find_elements_by_xpath(f"//*[@id='zg-ordered-list']/li[{i}]/span/div/span")

                for el in productInfoList:
                    pp2=el.find_element_by_tag_name('a')
                    listOflinks.append(pp2.get_property('href'))
            condition=False
            # try:
            #     driver.find_element_by_class_name('a-last').find_element_by_tag_name('a').get_property('href')
            #     driver.find_element_by_class_name('a-last').click()
            # except:
            #     condition=False\
        return listOflinks


if __name__ == '__main__':
    t=collector()
    x=t.collect("https://www.amazon.in/gp/bestsellers/boost/ref=zg_b_bs_boost_1")
    for link in x:
        print(link)


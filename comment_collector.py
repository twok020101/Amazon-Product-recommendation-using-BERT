import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
import collect
import gdrive



driver=webdriver.Edge("C:\Program Files (x86)\msedgedriver")
Data={}


class collector(object):


    def collect(self,links,file_name):
        print("In comment collector")
        for link in links:
            print(link)
            driver.implicitly_wait(3)
            driver.get(link)
            n=driver.find_element_by_xpath("//*[@id='productTitle']")
            name=n.text
            Data[f"{name}"]=[]
            z=driver.find_elements_by_id("cm-cr-dp-review-list")
            for i in z:
                base_comments=i.find_elements_by_class_name("a-expander-collapsed-height")
                for c in base_comments:
                    comments=c.find_elements_by_class_name("a-expander-content")
                    for elem in comments:
                        Data[f"{name}"].append(elem.text)
        collector.convert(self,file_name)

    def convert(self,name):
        if os.path.exists(f"{name}.csv"):
            os.remove(f"{name}.csv")
        df = pd.DataFrame.from_dict(Data, orient="index")
        df=df.transpose()
        df.to_csv(f"{name}.csv")
        gdrive.gg(name)



if __name__ == '__main__':
    t=collector()
    t.collect("https://www.amazon.in/ASGARD-Certified-Fabric-Protective-PACKAGING/dp/B08B1W5QN5/ref=zg_bs_boost_1?_"
              "encoding=UTF8&psc=1&refRID=H0V625YCN1VGPAR8YZEC")




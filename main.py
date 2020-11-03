"""Main function"""
import collect
from comment_collector import collector
import os
import gdrive_download
import mailer
import time

if __name__ == '__main__':
    condition=True
    product_list=["Masks","Sanitizer","Gloves","Thermometer"]
    while condition:
        for product in product_list:
            print(product)
        choice=str(input("Please Enter product name: "))
        if (choice in product_list):
            condition=False
            name=choice
        elif (choice==""):
            print("No entry selected")
            exit()
        else:
            print("Please choose from above products")
    z=collect.webby()
    z.runner(name)
    gdrive_download.gg(name)

    email=input("Please enter you email id: ")
    mailer.mail(email,name)







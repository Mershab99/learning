from selenium import webdriver
from time import sleep


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='G:/selenium/chromedriver.exe')
        self.driver.get("http://google.com")
        sleep(2)
        #quote = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[7]/div[2]/div/p/span[1]')
        #author = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[7]/div[2]/div/p/span[2]/span[1]')
        x = 1


Scraper()

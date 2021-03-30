import os
import sys
from time import sleep

import requests
from selenium import webdriver


class YouTubeDownloader:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.environ.get('WEBDRIVER'))

        for x in sys.argv:
            if x.__contains__(".py"):
                continue
            self.driver.get(os.environ.get('YT_DOWNLOADER_URL'))
            self.download(x)

    def download(self, link):
        # FILL WITH VALUE
        self.driver.find_element_by_xpath('/html/body/div/div[1]/form/input').send_keys(link)
        # CLICK THE CONVERT BUTTON
        self.driver.find_element_by_xpath('/html/body/div/div[1]/form/button').click()
        sleep(5)
        title = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div/h3').text
        creator = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div/p[1]').text
        # CLICK THE 'Find Link' button
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div/div/div[1]/button').click()
        sleep(5)
        # GET DOWNLOAD URL
        download_url = self.driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/div/div/div/div/div/div[1]/a[1]').get_attribute('href')
        # make download request
        req = requests.get(download_url, allow_redirects=True)
        # construct download path
        path = os.environ.get('DOWNLOAD_FOLDER', default='') + title + ' - ' + creator + '.mp4'
        file = open(path, "wb")
        file.write(req.content)


YouTubeDownloader()

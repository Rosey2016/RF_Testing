#!-*- coding:utf-8 -*-
import requests,time,unittest
from bs4 import BeautifulSoup
from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class beautifulSoupTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.url = 'https://www.baidu.com/'
        # 脚本运行时，错误的信息将打到这个列表中
        self.verificationErrors = []
        # 是否接受下一个A警告
        self.accept_next_alert = True

    def testCrawler(self):
        driver = self.driver
        driver.get(self.url)
        print 'Now access %s' % (self.url)
        time.sleep(2)

        req = requests.get(self.url).content
        time.sleep(2)
        soup = BeautifulSoup(req, 'html.parser', from_encoding='utf-8')
        print soup.prettify()
        print soup.p.prettify()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

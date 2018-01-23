#!-*- coding:utf-8 -*-
import requests,time,unittest
import urllib2,re
from bs4 import BeautifulSoup
from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class baiduTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.url = 'http://www.baidu.com'
        self.user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        self.headers={'User-Agent':self.user_agent}
        # 脚本运行时，错误的信息将打到这个列表中
        self.verificationErrors = []
        # 是否接受下一个A警告
        self.accept_next_alert = True

    def testCrawler(self):
        driver = self.driver
        driver.get(self.url)
        print 'Now access %s' % (self.url)
        time.sleep(2)

        try:
            request = urllib2.Request(self.url, headers=self.headers)
            response = urllib2.urlopen(request)
            #print response.read()
            content = response.read().decode('utf-8')

            pattern = re.compile("<a href=(.*?) name=.*? class=.*?>(.*?)</a>", re.S)
            items = re.findall(pattern, content)
            for item in items:
                print item[1].encode('utf-8')

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "code"):
                print e.reason


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import testing4_tool
import os
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider(unittest.TestCase):

    #页面初始化
    def setUp(self):
        self.siteURL = 'http://www.meishij.net/shicai/shucai_list'
        self.tool = testing4_tool.Tool()
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        self.headers = {'User-Agent': self.user_agent}

    #获取索引页面的内容
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    #获取索引界面的信息，list格式
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="listtyle1".*?<div class="img".*?<a href="(.*?)".*?title="(.*?)".*?<img .*? src="(.*?)"',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            #item[0]是详情页URL，item[1]是食材名称，item[2]是食材图片
            contents.append([item[0],item[1],item[2]])
        return contents

    #获取索引页面的详情页
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read()

    #获取食材百科简介
    def getBrief(self,page):
        pattern=re.compile('<div class="sccon_right_con".*?<strong class="title1">(.*?)</strong>.*?<strong class="title2">(.*?)</strong>.*?<p>(.*?)</p>.*?<strong class="title2">(.*?)</strong>.*?<p>(.*?)</p>.*?<strong class="title2">(.*?)</strong>.*?<p>(.*?)</p>.*?<strong class="title2">(.*?)</strong>.*?<p>(.*?)</p>',re.S)
        result = re.search(pattern,page)
        # group(1)是**的百科知识，group(2)是**介绍，group(3)是**介绍详情，group(4)是**的营养价值，group(5)是**的营养价值详情，group（6）是**的食用效果，group（7）是**的食用效果详情，group（8）是**的食用禁忌，group（9）是**的食用禁忌详情
        if result.group(1) is None:
            print u'食材百科内容为空'
        elif result.group(2) is None:
            contents = self.tool.replace(result.group(1))
            return contents
        elif result.group(3) is None:
            contents =  self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))
            return contents
        elif result.group(4) is None:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))
            return contents
        elif result.group(5) is None:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))
            return contents
        elif result.group(6) is None:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))+'\n'+self.tool.replace(result.group(5))
            return contents
        elif result.group(7) is None:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))+'\n'+self.tool.replace(result.group(5))+'\n\n'+self.tool.replace(result.group(6))
            return contents
        elif result.group(8) is None:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))+'\n'+self.tool.replace(result.group(5))+'\n\n'+self.tool.replace(result.group(6))+'\n'+self.tool.replace(result.group(7))
            return contents
        elif result.group(9) is None:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))+'\n'+self.tool.replace(result.group(5))+'\n\n'+self.tool.replace(result.group(6))+'\n'+self.tool.replace(result.group(7))+'\n\n'+self.tool.replace(result.group(8))
            return contents
        else:
            contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))+'\n'+self.tool.replace(result.group(5))+'\n\n'+self.tool.replace(result.group(6))+'\n'+self.tool.replace(result.group(7))+'\n\n'+self.tool.replace(result.group(8))+'\n'+self.tool.replace(result.group(9))
            return contents

        '''
        contents = self.tool.replace(result.group(1))+'\n\n'+self.tool.replace(result.group(2))+'\n'+self.tool.replace(result.group(3))+'\n\n'+self.tool.replace(result.group(4))+'\n'+self.tool.replace(result.group(5))+'\n\n'+self.tool.replace(result.group(6))+'\n'+self.tool.replace(result.group(7))+'\n\n'+self.tool.replace(result.group(8))+'\n'+self.tool.replace(result.group(9))
        #contents = self.tool.replace(result.group(0))
        if result is None:
            print u'食材百科内容为空'
        else:
            return contents
        '''

    # 保存食材百科简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print u"正在保存食材百科信息为", fileName
        f.write(content)

    # 保存头像
    def saveIcon(self,iconURL,name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL,fileName)

    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
         u = urllib.urlopen(imageURL)
         data = u.read()
         f = open(fileName, 'wb+')
         f.write(data)
         print u"正在保存Logo为",fileName
         f.close()

    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print u"新建了名字叫做",path,u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为",path,'的文件夹已经创建成功'
            return False

    #将一页食材的信息保存起来
    def savePageInfo(self,pageIndex):
        #获取第pageIndex页列表
        contents = self.getContents(pageIndex)
        time.sleep(2)
        for item in contents:
            # item[0]是详情页URL，item[1]是食材名称，item[2]是食材图片
            print u"爬取链接为",item[0],u"的食材",item[1],u'图片链接：',item[2]
            #详情页面的URL
            detailURL = item[0]
            #得到详情页面html代码
            detailPage = self.getDetailPage(detailURL)
            time.sleep(2)
            #获取食材简介
            brief = self.getBrief(detailPage)
            time.sleep(2)

            self.mkdir(item[1])
            # 保存食材简介
            if brief is not None:
                self.saveBrief(brief, item[1])
            # 保存食材图片
            iconURL = item[2]
            self.saveIcon(iconURL,item[1])

    #传入起止页码，获取页面内容
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u"正在寻找第",i,u"页内容"
            self.savePageInfo(i)

    def testSpider(self):
        # 传入起止页码即可，在此传入了2,10,表示抓取第2到10页的页面
        self.savePagesInfo(1,1)

if __name__ == "__main__":
    unittest.main()
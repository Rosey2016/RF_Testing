# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2,unittest,re,os
import testing4_tool

class xiaMiTextSpider(unittest.TestCase):

    def setUp(self):
        #虾米音乐-台湾福音书房-URL
        self.text = u'台湾福音书房'
        self.baseURL = 'http://www.xiami.com/search/song/page/'
        self.fileURL = 'G:\Python_Spider\Songs'
        self.tool = testing4_tool.Tool()
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        self.headers = {'User-Agent': self.user_agent}

    #获取虾米音乐的内容
    def getPage(self,pageIndex):
        xmURL= self.baseURL + str(pageIndex) +'?spm=a1z1s.3521869.0.0.fvbLc4&key=%E5%8F%B0%E6%B9%BE%E7%A6%8F%E9%9F%B3%E4%B9%A6%E6%88%BF&category=-1'
        print u"虾米歌曲URL ="+xmURL
        request = urllib2.Request(xmURL, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    #获取虾米音乐所有信息，list格式
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile( '<tr data-needpay="0".*?<td class="song_name".*?<a target="_blank" href="(.*?)".*?title="(.*?)".*?<td class="song_artist".*?title="(.*?)".*?<td class="song_album".*?title="(.*?)"',re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            #item[0]是歌曲链接，item[1]歌曲名称，item[2]是艺人，item[3]专辑
            num1 = self.tool.replace(item[0])
            num2 = self.tool.replace(item[1])
            num3 = self.tool.replace(item[2])
            num4 = self.tool.replace(item[3])
            #contents.append([self.tool.replace(item[0]),self.tool.replace(item[1]),self.tool.replace(item[2]),self.tool.replace(item[3])])
            contents.append([num1, num2, num3,num4])
        return contents

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

    # 保存内容
    def saveBrief(self,content):
        fileName =  self.fileURL +  "/" +u'诗歌' + ".txt"
        #f = codecs.open(fileName,'w+','utf-8')
        f = open(fileName,'a+')
        print u"正在保存信息为",fileName
        # 删除超链接标签
        removeU = re.compile('u')
        lists = re.sub(removeU, "", str(content).decode('unicode-escape'))
        f.write(lists+'\n')

    # 传入页面，保存歌曲内容
    def savePageInfo(self,pageIndex):
        self.mkdir(self.fileURL)
        #获取第一页歌曲列表
        contents = self.getContents(pageIndex)
        for item in contents:
            # item[0]歌曲链接，item[1]歌曲名称，item[3]是艺人，item[4]专辑
            print u"艺人",item[2],u"的专辑",item[3],u",中的歌曲",item[1]
            self.saveBrief(item)


    #传入起止页码，获取内容
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u"正在寻找第",i,u"页歌曲"
            self.savePageInfo(i)

    #执行测试
    def testXiaMi(self):
        print 'Start......'
        print self.savePagesInfo(45,46)

if __name__ == "__main__":
    unittest.main()

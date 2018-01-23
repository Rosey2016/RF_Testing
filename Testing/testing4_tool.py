#-*- coding:utf-8 -*-
import re

#处理页面标签类
class Tool:
    #去除img标签,1-7位空格,
    removeImg = re.compile('<img.*?>| {1,7}| ')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #和</span>标签
    removeNbsp = re.compile('</span>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表或&nbsp<td>替换为\t
    replaceTD= re.compile('<td>|&nbsp')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')
    # 将;删除
    removeFuhao = re.compile(';')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.removeNbsp, "", x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        x = re.sub(self.removeFuhao, "", x)
        #strip()将前后多余内容删除
        return x.strip()
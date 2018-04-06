import re
import os
import time
import json
import requests
from pyquery import PyQuery as pq
class yande:
    def __init__(self):
        self.reqx()
        self.has_file('safe')
        self.has_file('other')
        yande.before="https://yande.re/post"
    def reqx(self):
        yande.session=requests.session()
    def main_line(self):
        xurl="https://yande.re/post?page="
        for i in range(9000):
            if i==0:
                pass
            else:
                ourl=xurl+str(i)
                pa=self.url(ourl)
                if pa:
                    oHtml=pq(pa.text) #整张网页
                    liAll=oHtml("#post-list-posts").find("li")
                    for liU in liAll:
                        liUrl=pq(liU).find('a').attr("href")
                        liUrl="https://yande.re"+liUrl #提取网页图片地址
                        liH=self.url(liUrl)
                        if liH:
                            liHtml=pq(liH.text)
                            largeJpgUrl=liHtml("#highres").attr("href") #提取网页JPG大图片地址
                            self.page_save(i)
                            idc=re.findall('\d+',liUrl)
                            id=idc[0] #文件ID
                            imageType=liHtml("#stats").find(".vote-desc").parent().text()#文件类型UL
                            tagAll=liHtml("#tag-sidebar").find("li")
                            tagz=[]
                            dic={}
                            for itag in tagAll:
                                tagz.append(pq(itag).find("a").eq(1).text())
                            file=str(id)+".jpg"
                            if re.findall('Safe',imageType):
                                file='safe/'+file #文件名
                                jsonfile='safe/'+str(id)+".json"#文件地址
                            else:
                                file='other/'+file   #文件名         
                                jsonfile='other/'+str(id)+".json"#文件地址
                            self.file_save(file,largeJpgUrl)
                            if os.path.exists(file):
                                imageSize=os.path.getsize(file)
                                imageSize=self.true_size(imageSize)#文件大小
                                dic['size']=imageSize
                            dic['time']=time.time()
                            dic['tag']=tagz
                            dic['file']=file
                            dic['url']=largeJpgUrl
                            dic['type']=imageType#类型
                            tagJson=json.dumps(dic)
                            print(tagJson)
                            fj=open(jsonfile,'w+')
                            fj.write(tagJson)
                            fj.close()
    def page_save(self,page):
        fie=open('page.ini','w')
        dic={}
        dic['time']=time.time()
        dic['page']=page
        string=json.dumps(dic)
        fie.write(string)
        fie.close()
    def file_save(self,file,url):
        image=self.url(url)
        if image:
            with open(file,'wb') as fd:
                for chunk in image.iter_content(102400):
                    fd.write(chunk)
            fd.close()
    def url(self,url):#判断打开网页
        info=self.go_url(url)
        if hasattr(info,'status_code'):
            if info.status_code==200:
                yande.before=url
                print(url)
                return info
            else:
                return None
        else:
            return None
    def go_url(self,url):
        try:
            header={ "Accept":"text/html,application/xhtml+xml,application/xml;", "Accept-Encoding":"gzip", "Accept-Language":"zh-CN,zh;q=0.8", "Referer":yande.before, "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }
            info=yande.session.get(url,headers=header,timeout=30)
            return info
        except:
            time.sleep(30)
            self.go_url_two(url)
    def go_url_two(self,url):
        try:
            header={ "Accept":"text/html,application/xhtml+xml,application/xml;", "Accept-Encoding":"gzip", "Accept-Language":"zh-CN,zh;q=0.8", "Referer":yande.before, "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }
            info=yande.session.get(url,headers=header,timeout=30)
            return info
        except:
            time.sleep(30)
            self.go_url_three(url)
    def go_url_three(self,url):
        try:
            self.reqx()
            header={ "Accept":"text/html,application/xhtml+xml,application/xml;", "Accept-Encoding":"gzip", "Accept-Language":"zh-CN,zh;q=0.8", "Referer":yande.before, "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }
            info=yande.session.get(url,headers=header,timeout=30)
            return info
        except:
            pass
    def true_size(self,sz):
        if sz>1073741824:
                num=sz//1073741824
                sn=str(num)
                si=sn+"GB"
        elif sz>1048576:
                num=sz//1048576
                sn=str(num)
                si=sn+"MB"
        elif sz>1024:
                num=sz//1024
                sn=str(num)
                si=sn+"KB"
        else:
                sn=str(sz)
                si=sn+"B"
        return si    
    def has_file(self,dir):
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

c=yande()
c.main_line()

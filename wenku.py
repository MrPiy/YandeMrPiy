import json
import re
import requests
from pyquery import PyQuery as pq

urlx="http://www.8wenku.com/book/"
purl="http://www.8wenku.com"
for i in range(10000):
    if i<39:
        pass
    else:
        url=urlx+str(i)
        info=requests.get(url)
        html=pq(info.text)
        head=html("head").find('title').text()
        print(head)
        if re.findall('Application',head):
            pass
        else:
            book={}
            book['title']=html(".abook").find('h2').text()
            book['state']=html(".abook").find('.state').text()
            book['desc']=html(".abook").find('.desc').text()
            book['count']=html(".abook").find('.info>li:eq(0)').text()
            book['time']=html(".abook").find('.info>li:eq(1)').text()
            content={}
            juan=html(".section_list").find('.hd')
            for j in juan:
                onekey=pq(j).find('h3').text()
                li=pq(j).next(".bd").find("li")
                oneone={}
                one=[]#每卷的内容
                for l in li:
                    oneone['title']=pq(l).text()#每卷中的章节标题
                    oneone['url']=pq(l).find('a').attr("href")#每卷的地址
                    oneone['url']=purl+oneone['url']
                    two=requests.get(oneone['url'])
                    hw=pq(two.text)
                    post=hw(".article-body").html()
                    oneone['post']=post.replace("最新最全的日本动漫轻小说 轻小说文库(http://www.8wenku.com) 为你一网打尽！",'')
                    one.append(oneone.copy())
                content[onekey]=one
            boid=re.findall(r"\d+$",url)
            book['id']=boid[0]
            book['content']=content
            f=open("8wenku/"+book['title']+".json",'w')
            f.write(json.dumps(book))
            f.close()
            
        


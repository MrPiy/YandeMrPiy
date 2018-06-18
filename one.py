import requests
import re
from pyquery import PyQuery as pq

se=requests.Session()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
info=se.get('https://nyaa.si/?p=21',verify=False,headers=headers)
html=pq(info.text)
successTr=html(".success")
defaultTr=html(".default")
allone=[]
for i in successTr:
    one={}
    one['type']='success'
    one['title']=pq(i).find("td").eq(0).find('a').attr("title")
    one['href']=pq(i).find("td").eq(1).find('a').attr("href")
    one['name']=pq(i).find("td").eq(1).find('a').text()
    if pq(i).find(".fa-download"):
        one['download']=pq(i).find(".fa-download").parent().attr("href")
    else:
        one['download']=''
    if pq(i).find(".fa-magnet"):
        one['magnet']=pq(i).find(".fa-magnet").parent().attr("href")
    else:
        one['magnet']=''
    one['size']=pq(i).find("td").eq(3).text()
    one['date']=pq(i).find("td").eq(4).text()
    allone.append(one)
for i in defaultTr:
    one={}
    one['type']='default'
    one['title']=pq(i).find("td").eq(0).find('a').attr("title")
    one['href']=pq(i).find("td").eq(1).find('a').attr("href")
    one['name']=pq(i).find("td").eq(1).find('a').text()
    if pq(i).find(".fa-download"):
        one['download']=pq(i).find(".fa-download").parent().attr("href")
    else:
        one['download']=''
    if pq(i).find(".fa-magnet"):
        one['magnet']=pq(i).find(".fa-magnet").parent().attr("href")
    else:
        one['magnet']=''
    one['size']=pq(i).find("td").eq(3).text()
    one['date']=pq(i).find("td").eq(4).text()
    allone.append(one)
print(allone)

import os
import re
import json
import time
import requests
from pyquery import PyQuery as pq

session=requests.session()
url="https://yande.re/post?page="
def true_size(sz):
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
def filedir(di):      
    if os.path.exists(di):
    	pass
    else:
    	os.mkdir(di)

filedir('safe')
filedir('other')
for pnum in range(666):
    turl=url+str(pnum)
    pa=session.get(turl)
    oHtml=pq(pa.text)
    liAll=oHtml("#post-list-posts").find("li")
    for liU in liAll:
        liUrl=pq(liU).find('a').attr("href")
        liUrl="https://yande.re"+liUrl
        liH=session.get(liUrl)
        liHtml=pq(liH.text)
        largeJpgUrl=liHtml("#highres").attr("href")
        #image
        idc=re.findall('\d+',liUrl)
        id=idc[0]
        #id
        imageType=liHtml("#stats").find(".vote-desc").parent().text()
        # imageSize=liHtml("#stats").find(".vote-desc").parent().prev().text()
        tagAll=liHtml("#tag-sidebar").find("li")
        tagz=[]
        for itag in tagAll:
	        tagz.append(pq(itag).find("a").eq(1).text())
        tagz.append(imageType)
        file=str(id)+".jpg"
        if re.findall('Safe',imageType):
            file='safe/'+file
            jsonfile='safe/'+str(id)+".json"
        else:
            file='other/'+file            
            jsonfile='other/'+str(id)+".json"
        image=session.get(largeJpgUrl)
        with open(file,'wb') as fd:
            for chunk in image.iter_content(102400):
                fd.write(chunk)
        fd.close()
        imageSize=os.path.getsize(file)
        imageSize=true_size(imageSize)
        tagz.append(imageSize)
        tagz.append(largeJpgUrl)
        tagJson=json.dumps(tagz)
        fj=open(jsonfile,'w+')
        fj.write(tagJson)
        fj.close()
        print("image:"+file+" size:"+imageSize+" Done!")
        


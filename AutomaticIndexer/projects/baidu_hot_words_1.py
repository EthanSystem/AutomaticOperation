#coding:utf-8
import urllib,urllib2
import re
import threading
from urllib import quote
import HTMLParser
 
wordList = set()
wordsList = set()
def strip_tags(html):
    html = html.strip()    
    html = html.strip("\n")    
    result = []    
    parse = HTMLParser.HTMLParser()   
    parse.handle_data = result.append    
    parse.feed(html)    
    parse.close()    
    return "".join(result)
 
def getBaiduTopWords():
    url = "http://top.baidu.com/boards"
    webcontent = urllib.urlopen(url).read()
    
    idList = re.findall('href="\./buzz\?b=(\d+)?"',webcontent)
    idSet = set(idList)  
    for i in range(10):
        print "Thread %s Start..."%(i+1)
        t = threading.Thread(target=doGetWords,args=(idSet,))
        t.start()
        t.join(1)
 
def doGetWords(idSet):
    while len(idSet) > 0:
        print "idSet length ",len(idSet)
        try:
            uid = idSet.pop()
            print "id = ",uid
            url = 'http://top.baidu.com/buzz?b='+uid
            webcontent = urllib.urlopen(url).read()
            words = re.findall('<a class="list-title".*?">(.*?)</a>',webcontent)
            print len(words),"words found."
            wordList.update(words) 
        except Exception,e:
            print e
            #retry
            idSet.add(uid)
            continue
        
    print "threading activeCount",threading.activeCount()
    if threading.activeCount() == 2:
        print len(wordList),"words found in total."
        print wordList
        print threading.enumerate()
        for i in range(10):
            print "Thread %s Start..."%(i+1)
            t = threading.Thread(target=getWords,args=())
            t.start()
            t.join(1)
 
def getWords():
    while len(wordList) > 0:
        try:
            keyword = wordList.pop()
            req = urllib2.Request("http://tool.chinaz.com/baidu/words.aspx")
            req.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3)")
            req.add_header("Referer","http://tool.chinaz.com/baidu/words.aspx")
            data = "kw="+quote(keyword.decode("gbk").encode("utf8"))
            print data
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())   
            response = opener.open(req, data)
            html = response.read()
            kw = re.findall('<td class="kw">(.*?)</td>',html)
            kw = map(strip_tags,kw)
            print len(kw)
            if len(kw) == 0:
                wordsList.add(keyword)
            else:
                wordsList.update(kw)
        except:
            wordList.add(keyword)
            
    print "getWords threading activeCount",threading.activeCount()        
    f = open("words.inc", "w")
    f.writelines(wordsList)
    f.close()
            
getBaiduTopWords()


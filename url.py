import requests
from urlextract import URLExtract  #一个可以直接从源代码提取链接的库
def getInput():
    url = input("请输入网页链接：")
    setdepth = eval(input("请设置爬虫的深度："))
    return url,setdepth

def getHTMLText(url):  #获取一个页面所有源代码的函数
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        return ""

def getURL(text):   #从打印的文本中获得链接并储存到表格urls中
    extractor = URLExtract()
    urls = extractor.find_urls(text)  
    if len(urls) !=0: print(urls) #排除空表格
    return urls

def getnURL(urln,depth,setdepth):   #建立递归函数
    depth += 1
    if depth <= setdepth:
        for i in range(len(urln)):
            newtext = getHTMLText(urln[i])
            getnURL(getURL(newtext),depth,setdepth)
    
def runURL():
    depth = 0
    url, setdepth = getInput()
    text = getHTMLText(url)
    urls = getURL(text)
    getnURL(urls,depth,setdepth)

if __name__ == '__main__':

    runURL()
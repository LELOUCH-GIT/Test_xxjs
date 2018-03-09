'''
协程 并发 爬网页
使用urllib 和 gevent 的时候，一般要添加一个人补丁monkey
'''

from urllib import request
from gevent import monkey
import gevent
import bs4
#把当前程序的所有 io 操作的做了标记
monkey.patch_all()

def Myspider(url):
    print('get :%s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    soup = bs4.BeautifulSoup(data, "html.parser")
    for p in soup.find_all('p'):
        if p.string:
            print(p.string)

filename = "URL.txt"
Str = []
with open(filename,'r') as file_to_read:
    while True:
        line = file_to_read.readline()
        if not line:
            break
        Str.append(line.strip())
glist = []
for str in Str:
    glist.append(gevent.spawn(Myspider,str))
gevent.joinall(glist)
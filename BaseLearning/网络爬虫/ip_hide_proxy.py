#创建代理ip
import urllib.request
import random

#url = 'http://www.whatismyip.com.tw'#查询当前ip的网址
url = 'https://www.ip.cn/'#查询当前ip的网址

iplist = ['110.52.235.190:9999','113.13.177.75:9999','110.189.152.86:30763']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)

#opener与urlrequest相同，都是一个opener,这里同样可以修改header
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)

#暂时依旧有bug url无法访问,用另一个查询ip的网址但无法隐藏我的ip

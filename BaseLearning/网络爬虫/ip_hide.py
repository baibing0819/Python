#关于访问服务器出现的问题：
'''
    一、服务器一般通过检测user-agent来判断访问者是代码还是人，可以
    通过urllib.request.Request(url,data= None,headers={})来修改header
    从而实现'隐藏'
    二、由于用python代码访问服务器，例如爬取网页内容，批量下载照片，
    此时即使修改了headers,服务器也会采取屏蔽行为，例如检测到过于频繁
    访问的ip，会弹出验证码检测访问者是否为代码...高频率的访问行为并
    不像人为访问，会导致服务器会屏蔽该ip，导致代码无法继续正常完成
    功能...  
    
这样
有两种办法解决：
1、采用延时的办法，利用time模块间歇性访问服务器
2、利用代理，通过多个代理ip同时访问服务器，这样服务器检测到的是代理ip，
而不是代码真实的ip,从而可以有效的高频率访问服务器'''

#代理
'''
-参数是一个字典{'类型':'代理ip:端口号'}
-定制、创建一个openner
    openner = urllib.request.build_openner(proxy_support)
-安装openner
    urllib.request.install_openner(openner)
-调用openner
    openner.open(url)
'''
#代码：

import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
content = input('请输入要翻译的内容：')
#修改header用于隐藏方法一：
'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36'
'''

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data[ 'ue'] = 'UTF-8'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')

#req = urllib.request.Request(url,data,head)#返回一个object对象
#修改header用于隐藏方法二：
req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36')

response = urllib.request.urlopen(req)#将编码后的data'post'到URL，即提交数据
html = response.read().decode('utf-8')#接收客户端回应的数据（先解码,解码为json类型的字符串），response是上面方法返回的类文件对象，可以读取其中的内容
target = json.loads(html)#将已编码的 JSON 字符串解码为 Python 对象
print('翻译结果为：%s'%target['translateResult'][0][0]['tgt'])

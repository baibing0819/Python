import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
content = input('请输入要翻译的内容：')

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data[ 'ue'] = 'UTF-8'
data['typoResult'] = 'true'
'''
data['from'] = 'AUTO'
data['to']= ' AUTO ' 
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = 'fanyideskweb' 
data['sign'] = 'b4cb36f7d98fea71c082c11a55b97a72' 
data['ts'] = '1548039740875'
data['bv'] = '
data['action'] = 'FY_BY_CLICKBUTTION'
'''

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)#将编码后的data'post'到URL，即提交数据
html = response.read().decode('utf-8')#接收客户端回应的数据（先解码,解码为json类型的字符串），response是上面方法返回的类文件对象，可以读取其中的内容
target = json.loads(html)#将已编码的 JSON 字符串解码为 Python 对象
print('翻译结果为：%s'%target['translateResult'][0][0]['tgt'])

#bug清单
'''话不多说直接上链接（http://blog.csdn.net/nunchakushuang/article/details/75294947）因为有道翻译有反爬虫机制，所以简单的爬肯定不行，但是这一篇博客只是告诉我们有道的JS反爬虫代码，完全运行后还需要改你得到的POST请求的URL 
我的URL：http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule 
需要修改成http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule 
就是把_o去掉，而且这样的请求只能是用于英文翻译汉文，如果有大牛知道另外的完全的方法 
请别忘了告诉我一声哈…………^_^ '''

#知识清单
'''
urllib.urlopen(url[, data[, proxies]]) :创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。
参数url表示远程数据的路径，一般是网址；
参数data表示以post方式提交到url的数据(玩过web的人应该知道提交数据的两种方式：post与get。如果你不清楚，也不必太在意，一般情况下很少用到这个参数)；
'''



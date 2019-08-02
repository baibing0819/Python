#!/usr/bin/env python
# encoding: utf-8
'''
@author: baibing
@contact: 243061887(qq)
@software: pycharm
@file: server.py
@time: 8/2/19 1:22 PM
@desc:
'''

import tornado.web
'''
tornado 的基础框架模块
'''
import tornado.ioloop
'''
tornado的核心IO循环模块，封装了linux的epoll和BSD的kqueue，是tornado高效的基础
'''

#类比Django中的视图，一个业务处理类
class IndexHandler(tornado.web.RequestHandler):
    #处理get请求的，不能处理post请求
    def get(self,*args,**kwargs):
        #对应http请求的方法，给浏览器响应信息
        self.write("icebai is a good man")

if __name__ == "__main__":
    #实例化一个app对象
    #Application：是tornado web框架的核心应用类，是与服务器对应的接口
    #里面保存了路由映射表，有一个listen方法用于创建一个http服务器的实例
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    #绑定监听端口。 注意：此时服务器并没有开启监听
    app.listen(8000)
    '''
    IOLoop.current():返回当前线程的IOLoop实例
    IOLoop.start():启动IOLoop实例的I/O循环，同时开启监听
    '''
    tornado.ioloop.IOLoop.current().start()
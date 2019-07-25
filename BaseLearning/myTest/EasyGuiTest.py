                            #EasyGui测试
import easygui as g
import sys

while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏^ ^")

    msg = "你觉得EasyGui这个功能怎么样？"
    title = "小游戏互动"
    choices = ["谈恋爱","编程","OOXX","琴棋书画"]

    choice = g.choicebox(msg,title,choices)

    g.msgbox("你的选择是：" + str(choice), "结果")

    msg = "你希望重新开始这个小游戏么？"
    title ="请选择"

    if g.msgbox(msg ,title):
        pass
    else:
        sys.exit(0)

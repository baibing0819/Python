                        #文件内容分割练习

def split_file():
    f = open('F:\\白冰\\Python\\Python练习\\文件操作\\test.txt')

    boss = []       #用list暂存对话
    empolyment = []
    count = 1
    
    for each_line in f:
        if each_line[:6] != '======':       #取每行的前六个字节判断
            (role,word) = each_line.split(':',1)#用：分割，并保存在字典中
            if role == '老板':
                 boss.append(word)
            if role == '员工':
                 empolyment.append(word)

        else:
            boss_file_name = 'boss_' + str(count) + '.txt'
            empolyment_file_name = 'enployment_' + str(count) + '.txt'

            boss_file = open(boss_file_name, 'w')
            empolyment_file = open(empolyment_file_name, 'w')
            
            boss_file.writelines(boss)
            empolyment_file.writelines(empolyment)

            boss = []
            enployment = []
            count += 1
    f.close()

split_file()

#问题记录：
'''关于split()函数，但是出现了一个错误，文本文档中某一行人物说的的内容未加冒号，
导致这个函数出现错误。目前怀疑是因为该行缺少冒号且程序要求用冒号分割成两部分，
但分割过程中出现了换行符，故报错。
    报错内容： (role,word) = each_line.split(':',1)
ValueError: not enough values to unpack (expected 2, got 1)'''

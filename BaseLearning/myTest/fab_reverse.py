                                #斐波那契数列
'''来源：有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ 
　   兔子的规律为数列 1,1,2,3,5,8,13,21,34,55,89,144....
    规律：前两个月兔子对数为1，从第三个月起，每个月的数量为前两个月的数量之和
'''
def fab(n):
    if(n < 1):
        print('输入的月份数值有误')
        return -1
    elif(n == 1 or n == 2):
        return 1
    else:
        return fab(n-1) + fab(n-2)

n = int(input('请输入经过的月份数:'))
result = fab(n)
print('第%d个月后共有%d对兔子 '% (n,result))

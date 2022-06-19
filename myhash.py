def getInputs():
    try:
        x = eval(input("请输入你要转化的数字："))
    except:
        print("输入错误")
        x = eval(input("请输入一个整数："))
    return x

def myHash(x):  #自己定义的哈希函数
    return (x % 7)*2

def runMyHash():
    num = getInputs()
    print("对应的哈希函数值为：")
    print(myHash(num))

if __name__ == '__main__':

    runMyHash()


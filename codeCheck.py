import re
def check(addr):
    f = open(addr, encoding="utf-8") # 返回一个文件对象
    line = f.readline() # 调用文件的 readline()方法
    i = 1
    wrong = 0
    while line:   
        if "for" in line:
            matchObj = re.match('^(\s)(.*)(for)((\s)|(\s)(.*))(.*?)((\s)|(\s)(.*))(in)((\s)|(\s)(.*))(.*?)((\s)|(\s)(.*)|(.*?))[:]$', line)
            #re.match将给出的的正则表达式与line 的内容进行比较，若matchObj == None，则表示正则不匹配
            if matchObj == None:
                wrong += 1
                print("第",i,"行格式有误",line, end = '')
                if ":" not in line:
                    print("第",i,"行缺少“：”",line, end = '')
                if "in" not in line:
                    print("第",i,"行缺少“in”",line, end = '')
        if "if" in line:
            matchObj = re.match('^(\s)(.*)(if)((\s)|(\s)(.*))(.*?)((\s)|(\s)(.*))(==|!=|<=|>=|<|>)((\s)|(\s)(.*))(.*?)((\s)|(\s)(.*)|(.*?))[:]$', line)
            if matchObj == None:
                wrong += 1
                print("第",i,"行格式有误",line, end = '')
                if ":" not in line:
                    print("第",i,"行缺少“：”",line, end = '')
        if "elif" in line:
            matchObj = re.match('^(\s)(.*)(elif)((\s)|(\s)(.*))(.*?)((\s)|(\s)(.*))(==|!=|<=|>=|<|>)((\s)|(\s)(.*))(.*?)((\s)|(\s)(.*)|(.*?))[:]$', line)
            if matchObj == None:
                wrong += 1
                print("第",i,"行格式有误",line, end = '')
                if ":" not in line:
                    print("第",i,"行缺少“：”",line, end = '')     
        if "else" in line:
            matchObj = re.match('^(\s)(.*)(else)((\s)|(\s)(.*)|(.*?))[:]$', line)
            if matchObj == None:
                wrong += 1
                print("第",i,"行格式有误",line, end = '')
                if ":" not in line:
                    print("第",i,"行缺少“：”",line, end = '')
        if "try" in line:
            matchObj = re.match('^(\s)(.*)(try)((\s)|(\s)(.*)|(.*?))[:]$', line)
            numexp = 0 #用于检查是否漏写except
            if matchObj == None:
                wrong += 1
                if ":" not in line:
                    print("第",i,"行缺少“：”",line, end = '')
            j = i
            i=i+1
            line = f.readline()
            while line:
                if "try" in line:
                    if numexp == 0:
                        wrong +=1
                        print("第",j,"行的try缺少except")
                    break
                if "except" in line:
                    matchObj = re.match('^(\s)(.*)(except)((\s)|(\s)(.*)|(.*?))(.*?)[:]$', line)
                    numexp = 1
                    if matchObj == None:
                        wrong += 1
                        if ":" not in line:
                            print("第",i,"行缺少“：”",line, end = '')
                    break        
                i=i+1
                line = f.readline()
            if numexp == 0:
                wrong +=1
                print("第",j,"行的try缺少except")
        i=i+1
        line = f.readline()
    f.close()
    return wrong

def getResult(wrong):
    if wrong == 0:
        print("程序正常运行")
    else:
        print("请修改程序中的错误")

def getInput():
    addr = input("请输入要检查的程序：")
    return addr

def runCodeCheck():
    addr = getInput()
    wrong = check(addr)
    getResult(wrong)

if __name__ == '__main__':
    runCodeCheck()

    
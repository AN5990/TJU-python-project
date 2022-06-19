import myhash,sevenDigitalTubes,processBar,reservedWords,analysisOfSports,url,codeCheck
def getMenu():
    global module
    try :
        module = eval(input('''
功能菜单:
1.哈希函数
2.绘图进度条
3.七段码显示
4.保留字字频统计
5.体育竞技分析
6.爬虫程序
7.语法检查器
请选择：'''))
    except:
        print("输入错误")
        module = eval(input("请输入序号："))

def run():
    while(1):
        getMenu()
        if module == 1:
            myhash.runMyHash()
        if module == 2:
            processBar.processBar_drawDa()
        if module == 3:
            while(1):
                sevenDigitalTubes.runSevenDigitalTubes()
                try :
                    function = eval(input('''
下一步:
1.重新选择功能
2.退出
请选择：'''))
                except:
                    print("输入错误")
                    function = eval(input("请输入序号："))
                if function == 1:
                    continue
                if function == 2:
                    break
        if module == 4:
            reservedWords.runReservedWords()
        if module == 5:
            analysisOfSports.analysisOfSports()
        if module == 6:
            url.runURL()
        if module == 7:
            codeCheck.runCodeCheck()
        try:
            choice = eval(input('''
下一步:
1.回到菜单栏
2.退出
请选择：'''))
        except:
            print("输入错误")
            choice = eval(input("请输入序号："))
        if choice == 1:
            continue
        if choice == 2:
            break
if __name__ == '__main__':
    run()
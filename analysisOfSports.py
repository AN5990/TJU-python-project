from random import random
# 详细实现
# 第一个函数，介绍性内容，提高用户体验
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")
    print("天气情况会影响选手的能力值")
    print("比赛输赢不仅由选手能力决定，还有一定概率失误")


# 第二个函数
def getInputs():
    global  fitA, fitB, n, faultA, faultB, abiA, abiB
    abiA = eval(input("请输入选手A的能力值(0-1): "))
    faultA = eval(input("请输入选手A失误的概率(0-1): "))
    fitA = input("请输入适合选手A的天气(阴天，晴天，雨天，雪天): ")
    abiB = eval(input("请输入选手B的能力值(0-1): "))
    faultB = eval(input("请输入选手B失误的概率(0-1): "))
    fitB = input("请输入适合选手B的天气(阴天，晴天，雨天，雪天): ")
    n = eval(input("模拟比赛的场次: "))
    
    return abiA, abiB, n, fitA, fitB


# 第三个函数
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))

def gameOver(abiA, abiB):
    return abiA == 15 or abiB == 15


def getProb():
    #基于天气和选手的能力，获得其综合能力
    probW=random()
    if probW<0.25: weather ="阴天"
    if 0.25<=probW<0.5: weather ="晴天"
    if 0.5<=probW<0.75: weather ="雨天"
    if 0.75<=probW<=1: weather ="雪天"
    if weather == fitA: 
        weaA = 0.5
    else: weaA = 0
    if weather == fitB: 
        weaB = 0.5
    else: weaB = 0
    #能力占0.8，天气因素占0.2
    probA = abiA*0.8 + weaA*0.2
    probB = abiB*0.8 + weaB*0.2
    return probA, probB

def simOneGame():  #模拟一场比赛
    scoreA, scoreB = 0, 0
    # 表示选手A先发球
    serving = "abiA"
    probA, probB = getProb() #每次比赛都模拟一次比赛能力
    # 只要当前比赛不结束，选手就要进行相关操作
    while not gameOver(scoreA, scoreB):
        if serving == "abiA":
            # random()生成一个随机变量，如果该变量在A能力范围内，A获得一分
            if random() < probA:
                # random()生成一个随机变量，如果该变量不在A失误范围内，A获得一分
                if random() > faultA:
                    scoreA += 1
                else:
                    serving = "abiB"    
            else:
                serving = "abiB"
        else:
            if random() < probB:
                if random() > faultB:
                    scoreB += 1
                else:
                    serving = "abiA"
            else:
                serving = "abiA"
    return scoreA, scoreB

def simNGames(n):
    # 设定A和B获胜场次的变量winsA和winsB
    winsA, winsB = 0, 0
    # 循环N次
    for i in range(n):
        # 调用 simOneGame()函数来模拟一场比赛
        scoreA, scoreB = simOneGame()
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def analysisOfSports():
    printIntro()
    getInputs()
    winsA, winsB = simNGames(n)
    printSummary(winsA, winsB)

if __name__ == '__main__':

    analysisOfSports()

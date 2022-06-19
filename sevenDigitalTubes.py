import turtle, time

def drawGap():
    turtle.speed(0)  # 设置画笔速度 “fastest”:0  "fast":10   "normal":6  "slow":3  "slowest":1
    # turtle.Turtle().screen.delay(0)    #画笔速度无延迟
    turtle.penup()
    turtle.fd(3)

def drawLine(draw):  # 绘制单段数码管
    global color
    drawGap()
    turtle.speed(0)
    # turtle.Turtle().screen.delay(0)
    turtle.pensize(1)
    turtle.pendown()
    turtle.fillcolor(color) if draw  else turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.left(45)
    turtle.fd(6)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(6)
    turtle.right(90)
    turtle.fd(6)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(6)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.fd(6)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(6)
    turtle.left(45)
    drawGap()
    turtle.right(90)

def drawDigit(digit):  # 根据数字绘制七段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()  # 为绘制后续数字确定位置
    turtle.fd(20)  # 为绘制后续数字确定位置

def drawDate(date):
    global font_in,size
    for i in date:
        if i == "年":
            turtle.write("年", font=(font_in, size, "normal"))
            turtle.fd(40)
        elif i == "月":
            turtle.write("月", font=(font_in, size, "normal"))
            turtle.fd(40)
        elif i == "日":
            turtle.write("日", font=(font_in, size, "normal"))
            turtle.fd(40)
        elif i == "时":
            turtle.write("时", font=(font_in, size, "normal"))
            turtle.fd(40)
        elif i == "分":
            turtle.write("分", font=(font_in, size, "normal"))
            turtle.fd(40)
        elif i == "秒":
            turtle.write("秒", font=(font_in, size, "normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))

def getMenu():
    global choice
    try:
        choice = eval(input('''
请选择实现的功能:
1.数字
2.时间
3.获取系统时间
'''))
    except:
        print("输入错误")
        choice = eval(input("请输入序号："))

def sevenDigitalTubes():
    global color,font_in,size
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition 
    turtle.setup(1600, 1000, 0, 0)
    turtle.penup()
    turtle.fd(-600) 
    if choice == 1:
        color = input("请设置数码管颜色：")
        turtle.pencolor(color)
        try:
            num = eval(input("请输入一个整数："))
        except:
            print("输入错误")
            num = input("请输入一个整数：")
        drawDate(str(num))
    if choice == 2:
        font_in = input("请选择字体：")
        size = input("请设置字体大小：")
        color = input("请设置数码管颜色：")
        turtle.pencolor(color)
        try:
            clock = input("请输入一个时间，如：2022年03月21日：")
        except SyntaxError:
            print("输入错误")
            clock = input("请输入一个时间：")
        drawDate(clock)
    if choice == 3:
        font_in = input("请选择字体：")
        size = input("请设置字体大小：")
        color = input("请设置数码管颜色：")
        turtle.pencolor(color)
        drawDate(time.strftime("%Y年%m月%d日%H时%M分%S秒", time.localtime()))
    turtle.hideturtle()
    turtle.done()

def runSevenDigitalTubes():
    getMenu()
    sevenDigitalTubes()

if __name__ == '__main__':

    runSevenDigitalTubes()
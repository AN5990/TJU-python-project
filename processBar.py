import math
import turtle
def drawLine(len,rad,angle):   #划线的函数
    global summ
    turtle.fd(len)
    turtle.circle(rad,angle)
    summ = (len + (math.fabs(angle)/180)*math.fabs(rad)*3.14) 
    return summ
   
def pen(x,y,color,size,direction,speed):   #设定笔的参数和位置
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.seth(direction)
    turtle.speed(speed)

def processBar(scale,total,length):    #进度条
    for i in range(int(scale/20)+1):
        a = (i+int(length/20))*'*'
        b = '.'*(int(total/20)-(i+int(length/20)))
        c = ((i*20+length)/int(total))*100
        print("\r {:^3.0f}%[{}->{}]".format(c,a,b))
        
def processBar_drawDa():
    print("-------执行开始--------")
    length=0
    turtle.setup(1300,800,0,0)
    pen(-250,0,"blue",25,0,2)
    drawLine(500,0,0)
    processBar(summ,1494,length)
    length=summ
    pen(20,250,"blue",25,-90,2)
    drawLine(0,-1000,35)
    processBar(summ,1494,length)
    length+=summ
    pen(-20,0,"blue",25,-70,2)
    drawLine(0,1000,22)
    processBar(summ,1494,length)
    length+=summ
    print("-------执行结束--------")

if __name__ == '__main__':

    processBar_drawDa()
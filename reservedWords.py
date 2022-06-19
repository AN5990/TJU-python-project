menu = {"False","lambda","else","import","pass","None","break","except",
"in","raise","True","class","finally","is","return","and","continue",
"for","try","as","def","from","nonlocal","while","assert","del","global","not",
"with","elif","if","or","yeild"}
def getText():
    txt = open("reservedWordsTest", 'r').read()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, ' ')  # 将文本中的特殊字 符替换为空格
    return txt

def getWords(myTxt):
    words = myTxt.split()  # 获得分割完成的单词列表
    return words

def getReservedWords(words):
    counts = {}  # 创建空字典，存放词频统计信息
    for word in words:
        if word in menu:   #若单词在menu中则记录，否则记录为零
            counts[word] = counts.get(word, 0) + 1    # 若字典中无当前词语则创建一个键值对，若有则将原有值加1

    items = list(counts.items())  # 将无序的字典类型转换为有序的列表类型
    items.sort(key=lambda x: x[1], reverse=True)  # 按统计值从高到低排序（以第二列排序）
    n = len(items)   #获取列表的长度
    for i in range(n):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))   # 格式化输出词频统计结果

def runReservedWords():
    myTxt = getText()
    words = getWords(myTxt)
    getReservedWords(words)

if __name__ == '__main__':

    runReservedWords()
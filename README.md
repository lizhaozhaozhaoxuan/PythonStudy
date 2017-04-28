# PythonStudy
#本代码是借鉴同学代码之后重新打了一遍。理解了每行代码的含义。觉得该代码比起我之前自己想的便捷了许多。借此学习
#encoding:utf-8
import re
f1 = open('/home/lizhaoxuan/桌面/太空旅客.txt', 'r')
txt = f1.read()
f2 = open('/home/lizhaoxuan/桌面/词典/角色/反派.txt', 'r')
dict = {}
for line in f2.readlines():   #遍历每一行
    key = 0#初始化键值
    value = line.strip()#去掉空格，赋予值
    dict[value]=key#将值关联伟ｋｅｙ的项
    list = re.findall(value,txt)#将值匹配到太空旅客的文档中，赋予到列表里
    key = len(list)#返回列表中的数量
    print value#输出
    print key

运行结果
敌对
1
反派
3
坏人头目
0
终极BOSS
0
老BOSS
0
BOSS
1
大boss
1
坏人
4
双反派
0
凶手
5
对手
3
反面人物
0
boss
3
对手
3
坏蛋
0
反派角色
1
最终boss
1
混蛋
7
压得住
1
气场足
0
瞬间出戏
1
瑕不掩瑜
5
冷高
0
太有范
0
演技太赞
0
演技太捉急
0
没有共鸣
0
熊孩子
1
没有那么帅气利落
0
依然帅
0
帅惨了
0
没有演过特别好看的电影
0
身材好棒
5
这样的反派且行且珍惜
0
让人恨不起来
0
大反派演得超坏
0
男神当了反派依旧帅
0
帅了一脸
0
反派超有型
0
你会永远帅下去
0
反派过于渣化
0
废话太多
0
下手仁慈
0
枪法奇葩
0
死了都是颜值高的
0

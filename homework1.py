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

#基本的数据类型的操作
# r 表示的是 内部默认的字符不转义
print('\\\t\\') #\	\ 输出这样的格式
print(r'\\\t\\') #\\\t\\ 内部的特殊的字符没有被处理

#python 中的空值 使用的是 None 表示的是一个特殊的空值

#python 中通常使用大写来表示常量  其中也是个变量也是可以改变的

PI = 3.141592
print(PI)
PI =23

print(PI)

#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

bm = '中文'.encode('utf-8')
print(bm) # 字符串的格式转化  b'\xe4\xb8\xad\xe6\x96\x87'
print(bm.decode())

print(len('中文')) #输出当前字符串的长度   2

#格式化的数据

sd = "你的名字是:%s 你的年龄是 %d"%("张雪",25)
print(sd)
# %d 数字 %f 浮点 %s字符串 %x 十六进制数据

#list 列表数据类型

classMaster = ['Michenll','Bob','Tracy']

print(classMaster)
print(len(classMaster)) # 输出当前的长度 3

print(classMaster[-1]) #如果开始的是负数 则表示当前的操作是 负数 的方式实现

s = ['python', 'java', ['asp', 'php'], 'scheme']

print(len(s)) #输出当前的长度为4

#Tuple 元组
cas = (1,3)
#没有append insert 等方法 值是不能被改变的 在定义的时候，数据值已经被确认下来
#cas[1] = 4 TypeError: 'tuple' object does not support item assignment

print(cas[0])
print(cas[1])

#输出页面的相关的内容和相关的数据

#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)

bj = [45,65]

sda = (12,34,bj)
sda[2][0] = 'fj'
print(sda)

#tuple 的不变，指的是，指向 不变 指向了一个对象就不能随便的更改 创建一个不变的tuple 就必须保证，其中的每个元素都是不可变的

age = 10
if age >1 and age<5 :
    print('你已经成年了')
elif age >7 and age<9:
    print('你已经上小学了')
elif age>=10 and age <12:
    print("小学快毕业了！")
else:
    print('你要上高中了！')

#当前的文件的条件格式显示 传递相关的参数

for s in [12,43,423,53,53,23]:
    print(s)

# 字典的数据类型
d = {'mitch':65,'Bob':'iouuyo','Tracy':78}
print(d.get('Bob'))

del d['Tracy'] #删除
#
print(d)

#set  和dict类型相似  只是当前 value 










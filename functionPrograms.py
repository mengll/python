#函数的练习
def power(x):
        print(x*x)
power(2)

def power(x,y=1):
    s=1
    while y >0:
        y = y-1
        s= s*x

    print(s)

power(2,3) #8 当前的结构是正确的

power(2) #当函数的参数的个数给定的时候，在调用的时候，如果参数的个数不够，会出错，应该给予一定的默认值，以防止出错

#函数的参数必须指向，不变的对象 可以使用None去指定当前的对象的值

#参数组合
#python中定义函数，可以使用必须参数，默认参数，可变参数，关键字参数，命名关键字参数 参数定义顺序 必选参数，默认参数，可变参数，命名关键字参数 和关键字参数
def f1(a,b,c=10,*args,**kw):
        print('a =',a,'b =',b,'c =',c,'args =',args,'kw = ',kw)
def f2(a,b,c=0,*,d,**kw):
        print('a =',a,'b = ',b,'c = ',c,'d =',d,'kw =',kw)

f1(1,2); #a = 1 b = 2 c = 10 args = () kw =  {}

f1(1,2,3) #a = 1 b = 2 c = 3 args = () kw =  {}

f1(1,2,3,'a','b') #a = 1 b = 2 c = 3 args = ('a', 'b') kw =  {}

f1(1,2,3,'a','b',x=99) #a = 1 b = 2 c = 3 args = ('a', 'b') kw =  {'x': 99}

f1(1,2,3,'a','b','c',z=2,x=2) #f1(1,2,3,'a','b','c',z=2,x=2)

#*args 是可变参数 args接收是一个tuple
#**kw是关键字参数,kw接收的是一个dict

def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)
df = fact(3)
print(df)

#函数式的编程
#列表的高级的生成的方式
L = []
for x in range(1,10):
    L.append(x)

print(L)

#简化的形式
lss = [x for x in range(1,10)]# [1, 2, 3, 4, 5, 6, 7, 8, 9] 把生成的元素放在前面后面跟for循环 就可以把list创建出来
print(lss)
#如果这样的书写的方式 加上了if 判断
lop = [x*x for x in range(1,11) if x %2 ==0]
print(lop) # 输出当前的值 [4, 16, 36, 64, 100]


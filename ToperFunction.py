
#高阶函数
#因为函数也是一个对象，而且函数对象可以被赋值变量，所以通过变量也可以调用该函数

def now():
    print('20161026')
f = now  #将函数的名字赋值给变量


#假设我们现在想增强now方法 在函数调用前后自动打印日志，但是又不希望修改now函数定义 这种在代码运行期间动态增强的功能的方式，称之为装饰器 本质上是高阶函数的

def log(func):
    def wraper(*args,**kw):
        print('call %s()'%func.__name__)
        return func(*args,**kw)
    return wraper

#我们借助python的@语法把decorator 置于函数的定义
@log
def now():
    print('20161024')

now() # call now() 20161024
#在调用now() 函数不仅会运行now()函数本身 还会在运行now() 函数前打印一行日子
#把@log 放到now()  函数的定义出 相当于执行
now = log(now)


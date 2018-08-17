# python
Python学习笔记

##python decode 中的编码问题解决方案
```
line.decode("utf8","ignore")

python 抽象基类
import abc

class Ab(metaclass=abc.ABCMeta):  # 必须写的不然会出错
    @abc.abstractmethod
    def show(cls):
        print(23)


class Fuck(Ab):
    def __init__(self):
        print("初始化")
    def show(cls):
        print("【thisis show】")
```
### 如果 python的参数中没有使用了可变的对象，而在初始化的时候，没有被初始化，后期又被使用了，则使用的是默认的变量地址，多个对象同样的操作是会互相影响



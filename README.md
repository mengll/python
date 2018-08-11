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

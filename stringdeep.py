#字符串的复习和相关的练习
line = 'asdf fjdk;afed,fjek,asdf,foo'
#导入正则模块
import re
rs = re.split(r'[;,\s]\s*',line)
print(rs)
#正则的方式分割当前的字符串  ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
#在获取的时候注意，有没有括号捕获分组，如果使用了捕获分组那么匹配的文本也仅出现在结果集列表中

fileds = re.split(r'(;|,|\s)\s*',line)
print(fileds) #['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = fileds[::2] #使用这样的方式获取，当前对象的值
print(values) #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo'] 如果想重构当前的对象的方式，去实现相关的方法

#字符串以相关的字符串开始，以相关的字符串结尾

filename = "span.txt"
if filename.endswith('.txt') :
    print("you are right! the file type is txt") #判断当前文件以什么格式结尾

#filename.startswith('startName') 文件开始的相关的字符串的

#如果想检查多种匹配可能，只需要将所有的匹配项放到一个元组中去 然后传入startwith and endswitch 的方式去，处理相关的操作的方法

filenames = ['index.php','index.html','show.php','show.html','detail.html','.assess'] #当前文件的列表内容

lsd = [name for name in filenames if name.endswith(('.php','.assess'))]
print(lsd) # ['index.php', 'show.php', '.assess'] 多文件的名的结尾

#使用shell中常使用的通配符(*.py,Dat[0-9]*.csv) 去匹配文本字符串
#解决方案
#fnmatch 提供了两个函数 fnmatch() 和 fnmatchcase() 来实现这样的匹配

#from fnmatch import fnmatch,fnmatchcase

#fnmatch('too.txt','*.txt')
#fnmatch('foo.txt','?oo.txt')
#fnmatch('Dat45.csv','Dat[0-9]*')

#fnmatch() 函数使用底层操作喜用的大小写敏感的规则

#字符串的查找使用的是find的方法
print(line.find('my'))

#r = re.compile('\w+') 生成合适的字符串的 使用group(index) 的方式来获取匹配到的元素

#正则的方式查找替换相关的字符串

txt = "yeah but no bu yeah bu no_yeah"
ts = re.compile('but')

re.sub('but','and',txt,flags=re.IGNORECASE) #正则的方式查找替换，相关的字符的操作 的形式的管理的方式  第四个参数是取消匹配过程中的，大小写的操作

comment = re.compile(r'\b\w+\b')
print(comment.findall(txt))  #匹配当前字符串的

#删除字符串的前后空格

s = " hello worlds "
print(s.strip()) #删除开始，结尾不想要的字符串
#字符串对齐的发那个是

#ljust(20,'=') 字符串的长度为向左对齐 不够的地方使用 =补充
#rjust()
#center(20，*) 中间对齐 两侧使用* 补全 使用format的方式移动 format(text,'>20')

#格式化字符串的的输出
s = '{name} has {n} message.'
sa = s.format(name='zhnagguoyuan',n=32)
print(sa)

name  = "fjhs"
n =43
print(s.format_map(vars())) #通过变量区中找到 从变量对象中查找 相关的数据

#处理html 标签的操作
ssd = "Elements are Writen as <tag>sddasd</tag>"
import html
print(ssd)
sda =html.escape(ssd)
print(html.escape(ssd)) #格式化输出
print(html.escape(ssd,quote=False)) #格式化输出

from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(sda)) #反转显示当前的字符串的操作！

#from xml import sax


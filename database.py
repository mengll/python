#数据类型和算法
#基本的数据类型
#1.1 解压序列赋值给多变量
data = ['na','mei','lu',(2012,12,21)]
_,shares,price,_ = data
print(shares,price) #_ 表示的是占位符的意思

print(sum([1,3,6]))

#创建固定长度的
#deque(maxlen) 构造函数会创建一个固定大小的队列 当先元素键入的对象已满，老
from collections import deque
de = deque()
de.append(2)
de.append(1)
de.append(4 )#执行相关的函数的操作处理
print(de)
print(de.pop()) # 直接的执行是从右侧抛出一个对象
print(de.popleft())#从左侧抛出一个对象
de.append(6)
de.append(7)
de.insert(4,[2,34]) #执行后的结果在队列的最后面添加了相关的哦数据
print(de)

#查找哦啊队列中最大的几个数据 或者最小的几个数据的处理的方法
import heapq
nums = [1,8,2,23,7,-4,18,42,32,37,2]
print(heapq.nlargest(2,nums)) #输出的是当前队列中最大的几个数据
print(heapq.nsmallest(2,nums)) #输出队列中小的几个数据

#整理后堆的数据结构永远是最小的数据 放在最前面
heapq.heapify(nums)
print(nums) # [-4, 2, 1, 23, 7, 2, 18, 42, 32, 37, 8] 堆的数据结构最重要的特性heap[0]永远是最小的元素 并且剩余的元素很容易的通过heap.heappop 的方法得到 该方法获取第一个元素
#实现优先级队列

#字典一个键对应多个值的字典一个键对应多个子的映射这样那个的字典
d = {
    'a':[1,2,4],
    'b':[9,5,6]
}

e = {
    'a':{1,2,3},
    'b':{9,5,6}
}

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['d'].append(2)
d['b'].append(4)
#defaultdict 的一个特性自动初始化每一个key刚开始对应的值，所以只需要添加元素的处理操作
print(d) #defaultdict(<class 'list'>, {'a': [1], 'b': [4], 'd': [2]})

s = defaultdict(set)
s['a'].add(23)
s['a'].add(34)
s['v'].add(54)
print(s) #defaultdict(<class 'set'>, {'a': {34, 23}, 'v': {54}})

#defaultdict 会自动的创建访问的键，创建映射体实体，如果不需要这样的特性，你可以在一个普通的字典上使用 setdefault

e = {}
e.setdefault('a',[]).append(1) #设置当前默认类型
e.setdefault('a',[]).append(2)
e.setdefault('b',[]).append(4)
print(e) #{'b': [4], 'a': [1, 2]}

#字符串的命名切片
lefts = slice(0,3)
rights = slice(-3,11)

nm = "18801273298"

cis = nm[lefts] +'****'+nm[rights]

print(cis) #避免了大量无法理解的硬编码下标使得你的代码更加清晰可读了

#数组中出现次数最多
word_counts = ['look','into','my','eyes','look','my']

from collections import Counter
word_ = Counter(word_counts)
top_three = word_.most_common(3)
print(top_three) #出现词频最多的几个


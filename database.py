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


#正则相关的操作的方式和实力
import re
if __name__ == '__main__':
        res = "wenwendandandeadsa rod"
        s = ''
        re.sub('rod$','bod',res) # 正则替换函数
        print(re.sub('rod$','bod',res)) # wenwendandandeadsa bod 第一个参数是要匹配的正则 第二个参数是要替换内容 第三个参数是要匹配的字符串 第四个参数是要匹配的个数

        #实现正则查找的方法

        print(re.search('wen(?=\w+)',res)) # 实现断言的方式测试 零宽度正

        #将字符串转化成 pattern
        #re.compile()

        #re.compile()
        # 函数，将正则表达式的字符串形式编译为Pattern实例

        pattern  = re.compile('[a-z]+')
        p = pattern.findall('ddsfffff sdddd ')
        print(p)
        # .  表示匹配除了换行符外的任何字符  注：通过设置 re.DOTALL 标志可以使  匹配任何字符（包含换行符）
        # | A | B ，表示匹配正则表达式 A 或者 B
        # ^ 1. （脱字符）匹配输入字符串的开始位置 1. （脱字符）匹配输入字符串的开始位置  也匹配换行符之后的位置
        # http://bbs.fishc.com/thread-57691-1-1.html  教程地址
        #*?, +?, ??   默认情况下 、 和 ?  的匹配模式是贪婪模式（即会尽可能多地匹配符合规则的字符串）；*? 、
        #举个栗子：对于字符串 "FishCCC"，正则表达式 
        
        
        

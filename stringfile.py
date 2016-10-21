
# 每一笔记 python 字符串处理

#unicode 编码系统为表达任意语言的任意字符而设计，它使用的4字节的数字来表达每个字母，符号，或者表示文字 utf-16 16位 = 2字节

#字符串可以使用，单引号，和双引号来表示定义

#例如
if __name__ == '__main__':
    suffixes = {100:['KB','KS','MB','GB','TB'],1024:['KIB','MIB','TIB']}

    def approximate_size():
        #''' Conver is a file size to human-readfile from '''
        for suf in suffixes[100]:
            print(suf)
            #raise ValueError('number is old you must use new word') 抛出一个错误的异常

    approximate_size()

    mll = "wenwen love {na}".format(na="fj")
    mk = [12]
    #传递当前的参数到按照一定的格式显示
    wendna = "wenwen and dandan is the result name :{obj[0]}".format(obj = mk)
    #通过下标的方式 返回当前结果
    print(mll)
    print(wendna) #wenwen and dandan is the result name :12
    #format 使用限定符 语法是{}中带:号）
    #填充与对齐
    # 填充常跟对齐一起使用
    #^ 、 < 、 > 分别是居中、左对齐、右对齐，后面带宽度
    #:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
    print("189{:>8}".format(188)) #向右对齐的操作 189     188
    print("123{:0>6}".format(3819)) #向右移动6位 中间不够的使用0填充  123003819

    #精度 和返回数据的类型

    print("{:.2f}".format(321.236)) #四舍五入 保留两位有效数字 321.24

    #使用金额的方式表示当前的 金额的现实格式
    print("{:,}".format(1238727388)) #1,238,727,388

    #字符串的格式化显示 一般使用的是三个引号去 声明当前的格式  ''' 这里面是可以使用换行等操作的'''
    mlz = "MENGLL"
    print(mlz.lower().count('l')) # 转换成小写 并统计里面 L 字符在其中出现的次数

    #多行的文本的输出的格式
    wd = '''
        to day i want to say you!
        no mater what happend in the futher
        i love you
    '''
    print(wd.splitlines()) #['', '        to day i want to say you!', '        no mater what happend in the futher', '        i love you', '    ']

    #split 是按照特定的字符进行数据的风格处理

    page = "page=1&name=23&limit=12&offset=3"
    print(page.split('&')) #['page=1', 'name=23', 'limit=12', 'offset=3']

    #创建一个字典类型的
    zd = {'age':20,'lv':34}
    print("{obj[age]} had lv num {obj[lv]}".format(obj = zd)) #传入的如果是字典类型的 如何在格式化的字符串的时候输出

    #字符串的分片的处理

    a_string = "zhang fei had died and zhao yun and zhu ge liang"
    print(a_string[6:9]) #输出当前的第6-9 个字符

    print(a_string[3:]) #截取第三个字符到最后的内容

    print(a_string[:6]) #截取到前6位的字符

    #字符串的连接使用的是 +
    f_name = "meng"
    l_name = "ll"
    print(f_name +' '+l_name) #meng ll

    #使用decode('ascii') 进行转码

    str_rep = "niao ge  da zhan erniao"
    print(str_rep.replace('niao','xin'))
    #合并当前的切片
    pian = ['12','32','34','43'] # 类型限制，只能合并字符串的内容
    print(",".join(pian))


import csv
import os
import sys
import zipfile

#加载当前的文件配置
def getPath():
    path = os.path.split (os.path.realpath (__file__))[0]
    return path

#获取当前目录结构下面的内容
def getPathDat(path):
    for parent, dirnames, filenames in os.walk (path):
        for dirname in dirnames:
            getPathDat(os.path.join(path,dirname))
        #遍历当前的文件
        for filename in filenames:  # 输出文件信息
            fileExtends = os.path.splitext(filename)[1]
            if fileExtends == ".py":
                print("This is a Test")

#解压文件
def Unzip(target_dir,target_name):
    zipfiles=zipfile.ZipFile(target_name,'r')
    zipfiles.extractall(os.path.join(target_dir,os.path.splitext(target_name)[0]))
    zipfiles.close()
    print("Unzip finished!")
getPathDat(getPath())
getPath()

if  __name__ == '__main__':
    print("Tshi main")

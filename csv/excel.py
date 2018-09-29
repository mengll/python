# _*_ coding: utf8 _*_
# @email mll@anfan.com
# 武汉掌游科技
import csv
import os
import re
import zipfile
import logging
from datetime import date, datetime

import xlrd
import pandas as pd
from itertools import zip_longest

from dataBase import dataBase


def ListToStr(lista):
    back =""
    for item in lista:
        back += str(item)
    return back
#当前文件
def LogInfo(content,logfile="dt_info.log"):
    logging.basicConfig(filename=logfile,
                        format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %p',
                        level=logging.INFO)
    logging.info(content)
#加载当前的文件配置
def getPath():
    path = os.path.split (os.path.realpath (__file__))[0]
    return path
#解压文件
def Unzip(target_dir,target_name):
    zipfiles=zipfile.ZipFile(target_name,'r')
    print(zipfiles.filename())
    zipfiles.extractall(os.path.join(target_dir,os.path.splitext(target_name)[0]))
    zipfiles.close()

def NewCkIndex(row,wantcell):
    indexer = 0 #保存当前渠道的索引
    try:
        for iv in row:
            if str(iv).strip().strip("`").strip("\t")  == str(wantcell).strip().strip("`").strip("\t") :
                return indexer
            indexer +=1
        return False
    except BaseException as e:
        print("--->>>>",e)

#解析获取当前的索引值
def ParseIndexer(row):
    af_date  = ["帐号"]  #保存订单名声字符集
    af_pname = ["注册时间"]  #保存费用的字符集
    dta = {}
    try:
        for af_dt,af_pn in zip_longest(af_date,af_pname):
            af_dt_index = NewCkIndex(row,str(af_dt).strip().strip("`").strip("\t"))
            if af_dt_index !=False:
                dta['ucid_index'] = af_dt_index

            af_pn_index = NewCkIndex(row, str(af_pn).strip().strip("`").strip("\t"))
            if af_pn_index !=False:
                 dta['create_date_index'] =af_pn_index

        return dta #生成的索引的字符集
    except BaseException as e :
        print(e)

#解析当前的数据对象获取当前的索引
def CkIndex(row,wantcell):
    indexer = [] #保存当前渠道的索引
    for cell in wantcell:
        indexer.append(row.index(cell))
    return indexer #返回当前的索引

#解析当前的excel
def ParseExcel(urla, filename,pg):
    data = xlrd.open_workbook(urla)
    num = len(data.sheets())
    for i in range(0,num,1):
        IsCkIndex = True
        startParse = False
        dat_cell = data.sheets()[i] #获取当前的每一个shell

        #获取第一行的数据获取当前总行数
        ros_num = dat_cell.nrows
        header = ["帐号","ucid","注册时间","idfa"]
        data   = []
        try:
            index_a = {}
            for j in range(ros_num):
                rows = dat_cell.row_values(j)
                if IsCkIndex == True:
                    index_a = ParseIndexer(rows)
                    IsCkIndex = False
                    startParse = True

                if startParse == True:
                    if j >0:
                        ucid = str(rows[index_a['ucid_index']]).split("_")[1]
                        cj = xlrd.xldate.xldate_as_datetime(dat_cell.cell(j, index_a['create_date_index']).value, 0)
                        cja = cj.strftime("%Y%m%d") # 执行的日期

                        run_sql = "select imei,ucid,create_date from ty_user_meta_data where ucid = {ucid} and " \
                                  "create_date = {create_date}".format(ucid = ucid,create_date = cja)
                        d = pg.query(run_sql)
                        imei = d[0][0] if len(d) >0 else ''
                        kl = [rows[index_a['ucid_index']],ucid, cja,imei]
                        print(kl)
                        data.append(kl)
                    pass

        except BaseException as e:
            IsCkIndex = True
            startParse = False
        finally:
            save_csv(os.path.join(getPath(), filename.split(".")[0]),header,data)

def save_csv(save_path,header,data):
    df = pd.DataFrame(data, columns=header)
    df.to_csv(save_path+".csv")

def ParseCsv(dat,filename,pg):
    try:
        with open(dat, newline='', encoding='gb18030', errors='ignore') as f:
            reader = csv.reader(f)
            header = ["帐号", "ucid", "注册时间", "idfa"]
            data = []
            index_a = {}
            IsCkIndex = True
            j = 0
            row_num = 0
            for row in reader:
                if IsCkIndex == True:
                    index_a = ParseIndexer(row)
                    IsCkIndex = False
                    startParse = True
                    row_num = len(row)
                if startParse == True:
                    if j >0 and len(row) == row_num:
                        ucids = str(row[index_a['ucid_index']]).split("_")
                        if len(ucids) < 2:
                            print(row)
                            continue
                        ucid = ucids[1]
                        cj = row[index_a['create_date_index']]
                        cja = getDateFormat(cj)
                        print(cja)
                        #cja = datetime.strptime(cj,"%Y/%m/%d %H:%M").strftime("%Y%m%d")
                        run_sql = "select imei,ucid,create_date from ty_user_meta_data where ucid = {ucid} and " \
                                  "create_date = {create_date}".format(ucid=ucid, create_date=cja)
                        d = pg.query(run_sql)
                        imei = d[0][0] if len(d) > 0 else ''
                        kl = [row[index_a['ucid_index']], ucid, cja, imei]

                        data.append(kl)
                j += 1
    except Exception as e:
        print(e.__str__())
        IsCkIndex = True
        startParse = False
    finally:
        save_csv(os.path.join(getPath(), filename.split(".")[0]), header, data)

# 返回正确的时间格式
def getDateFormat(datetime_str):
    date_format_1 = r"(\d{4})[-/](\d{1,2})[-/](\d{1,2})\s(\d{1,2}):?(\d{1,2}):?(\d{1,2})?"
    dt_c = re.search(date_format_1,datetime_str).groups()
    month = dt_c[1]
    day   = dt_c[2]
    if dt_c is not None:
        if len(dt_c[1]) == 1:
            month ='0'+ dt_c[1]
        if len(dt_c[2]) == 1:
            day = '0'+ dt_c[2]
        return dt_c[0]+month+day

#获取当前目录结构下面的内容
def getPathDat(path,pg):
    for parent, dirnames, filenames in os.walk (path):
        for dirname in dirnames:
            continue
        #遍历当前的文件
        try:
            for filename in filenames:  # 输出文件信息
                farr = os.path.splitext(filename)
                fileExtends = farr[1]
                fname = farr[0]
                fpath = os.path.join(path, filename)
                if fileExtends == ".xlsx":
                    ParseExcel(fpath,filename,pg)
                if fileExtends == ".csv":
                    ParseCsv(fpath,filename,pg)
        except BaseException as e:
            print(e)
        finally:
            print("openfile error")
#函数方法的入口
if  __name__ == '__main__':
    with dataBase() as db:
        ppn = os.path.join(getPath(),"data")
        getPathDat(ppn,db.pg)
    #GetBillDat()
    # print("2016年08月")



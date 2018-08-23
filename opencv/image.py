# _*_ coding: utf8 _*_
# @email mll@anfan.com
# 武汉掌游科技
import os
import re

import imutils
import cv2
from skimage.measure import compare_ssim
import numpy as np
# "images/20170710211223030.png"  "images/20170710211248018.png"
# 对比图片素材具体不同
from main import getPath


def complieImg(imgone,imgtwo):
    imageA = cv2.imread(imgone)
    imageB = cv2.imread(imgtwo)
    print("A",imageA.shape)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM:{}".format(score))

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Modified", imageB)
    # cv2.imwrite("haha2.png",imageB) // 答应图片的差异
    cv2.waitKey(0)  # 设置图片的不同点的

    # 今日头条数据视频抓取帧（0,32,54,76,98,119, 272,294,316）

#  两张图片的相似度
def complieImgScore(imgone,imgtwo):
    imageA = cv2.imread(imgone)
    imageB = cv2.imread(imgtwo)
    a_size = imageA.shape
    b_size = imageB.shape

    if a_size != b_size:
        print("图片尺寸不匹配")
        return
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM:{}".format(score))

def compile_start(filenames,parent,file_one):
    try:
        imageA = cv_imread(file_one)
        a_size = imageA.shape

        for filename in filenames:  # 输出文件信息
            is_type = re.search(r".*(?=jpg|png|jpeg)", filename)
            if is_type is not None:
                fpath = os.path.join(getPath(), parent, filename)
                imageB = cv_imread(fpath)
                b_size = imageB.shape
                if a_size != b_size:
                    print("图片尺寸不匹配")
                    continue
                grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

                (score, diff) = compare_ssim(grayA, grayB, full=True)
                diff = (diff * 255).astype("uint8")
                print("SSIM:{}".format(score))
                # cv2.waitKey(1000)
    except Exception as e:
        print(e)

def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

def getPathDat(path,file_path):
    for parent, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            if os.path.isdir(os.path.join(parent,dirname)):
                getPathDat(os.path.join(parent,dirname),file_path)
        compile_start(filenames,parent,file_path)
# 比较两张图片的具体不同点 （使用demo）配有使用案例
if __name__ == "__main__":
    # file_path = os.path.join(getPath(),'''张赛.jpg''')
    #
    # img = cv_imread(file_path)
    # cv2.imshow("ak",img)
    # cv2.waitKey(0)
    # # print(img.shape)
    getPathDat(os.path.join(getPath(),"images","gjyp"),os.path.join("images","170912cca2048561e44ba58e6856e2b2550629.jpg"))
    #complieImgScore("src/video/12_28_62_12_98.jpg",r'E:\xuexi\image\images\gjyp\20170902\480x320\章赛-20170902-480x320_01.jpg')

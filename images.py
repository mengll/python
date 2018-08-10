# _*_ coding: utf8 _*_
# @email mll@anfan.com
# 武汉掌游科技
import imutils
import cv2
from skimage.measure import compare_ssim

# "images/20170710211223030.png"  "images/20170710211248018.png"
# 对比图片素材具体不同
def complieImg(imgone,imgtwo):
    imageA = cv2.imread(imgone)
    imageB = cv2.imread(imgtwo)
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
    # cv2.imwrite("haha2.png",imageB)
    cv2.waitKey(5000)  # 设置图片的不同点的

# 比较两张图片的具体不同点 （使用demo）配有使用案例
if __name__ == "__main__":
    complieImg("images/69869071051_69869970081_1533715334_0.jpg","images/69869071051_69869970081_1533715334_1.jpg")

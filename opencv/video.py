import hashlib
import os
import cv2

md = {}
# 视频全部解压
def dump_video(path):
    video_path = path
    cap = cv2.VideoCapture(video_path)
    # 原始视频
    with_v = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height_v = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("【视频宽高】",with_v,height_v)
    # Open the input movie file
    input_movie = cv2.VideoCapture(video_path)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    print("【length】",length)

    pre_file = '12_28_62_12_'
    f_index = 0

    while True:
        ret, frame = input_movie.read()
        if not ret:
            break
        frame_resize = cv2.resize(frame, (int(with_v), int(height_v)), interpolation=cv2.INTER_NEAREST)
        # 截取视频的两针图片
        #if f_index in [148, 308]:
        file_path = "./video/" + pre_file + str(f_index) + ".jpg"
        cv2.imencode('.jpg', frame_resize)[1].tofile(file_path)
        m = get_video_md5(file_path)
        md[m] = file_path
        f_index += 1
    input_movie.release()
    cv2.destroyAllWindows()

# 获取视频的首图 图片的名字为视频文件的名字
# @param path string 视频地址
# @param save_path 视频保存地址（上层目录）
# @return file_path file_md5,width,height (视频首图保存的路径，视频的图片额MD5,宽度，高度)
def get_video_img(path,save_path=""):
    video_path = path
    cap = cv2.VideoCapture(video_path)
    # 原始视频
    with_v = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height_v = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Open the input movie file
    input_movie = cv2.VideoCapture(video_path)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    print("【length】",length)

    pre_file = os.path.basename(path)
    save_name = pre_file.split('.')[0]
    ret, frame = input_movie.read()

    if not ret:
        return
    frame_resize = cv2.resize(frame, (int(with_v), int(height_v)), interpolation=cv2.INTER_NEAREST)

    # 截取视频的两针图片
    save_url = os.path.join(save_path,"upload","video_img")
    if not os.path.exists(save_url):
        os.makedirs(save_url)

    file_path = os.path.join(save_url,"%s.jpg"%save_name)
    cv2.imencode('.jpg', frame_resize)[1].tofile(file_path)
    input_movie.release()
    cv2.destroyAllWindows()

    return file_path,get_video_md5(file_path),with_v,height_v

# 获取视频文件的MD5
def get_video_md5(file):
    buffer_size = 1024 * 1024  # 缓冲大小,这里表示1MB
    md5obj = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            content = f.read(buffer_size)  # 每次读取指定字节
            if content:
                md5obj.update(content)
            else:
                break  # 当内容为空时,终止循环

    md5 = md5obj.hexdigest()
    return md5
down_md = []

def md_file(parent,filenames):
    try:
        for filename in filenames:  # 输出文件信息
            file_path = os.path.join(parent,filename)
            down_md.append(get_video_md5(file_path))
    except Exception as e:
        print("【文件加密错误】",e)

def get_path_md(path):
    for parent, dirnames, filenames in os.walk (path):
        for dirname in dirnames:
            if os.path.isdir(os.path.join(parent,dirname)):
                get_path_md(os.path.join(parent,dirname))
            #遍历当前的文件
        md_file(parent,filenames)

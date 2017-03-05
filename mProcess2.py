from multiprocessing import Process
import os

def info():
   # print(os.getegid())
    if hasattr(os,"getppid") :
        print(os.getppid()) #获取子ID 的
    print(os.getpid())
    print("this is info functuoo")

def game():
    print("this is Game function ! as you can see in the futren")
    info()

if __name__ == "__main__":
    op = Process(target=game)
    op.start()
    op.join()

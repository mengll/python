from multiprocessing import Process,Queue
import os

def q(p):
    p.put([32,None,43])

def oprun(o):
    print("this is oprun function!")

if __name__ == "__main__":
    print("exchange message with two process")
    qun= Queue()
    for i in range(3):
        print(i)
    pro = Process(target=q,args=(qun,))
    pro.start()
    pro.run = oprun

    print(qun.get())
    pro.join()
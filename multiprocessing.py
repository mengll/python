import multiprocessing
import time

def consumer(input_q):
     print("-1-")
     while True:
         item = input_q.get()
         #输出当前的内容
         print(item)
         input_q.task_done() #发出信号当前的线程已经完成

def producer(sequence,output_q):
     print("-2-")
     for item in sequence:
         output_q.put(item)

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    const_p = multiprocessing.Process(target=consumer,args=(q,))
    const_p.daemon = True
    const_p.start()

    sequence = [1,2,3,4]
    producer(sequence,q)
    q.join()

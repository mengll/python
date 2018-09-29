# _*_ coding: utf8 _*_
# @email mll@anfan.com
# 武汉掌游科技
import time
from asyncio import get_event_loop
import asyncio
from threading import Thread

async def get_ucid(num):
    # await asyncio.sleep(1)
    return 3 + num

async def fuk(add):
    # await  asyncio.sleep(1)
    return 4 + add

# 携程回调
def back(res):
    print("ucid=>",res.result())
    pass

def thradfunc(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def dowork(x,loop):
    print("携程工作",x)
    await asyncio.sleep(1)
    if x == 'end':
        loop.stop()

if __name__ == "__main__":
    loop = get_event_loop()
    try:
        for i in range(2):
            ucid_task = asyncio.ensure_future(get_ucid(i))
            ucid_task.add_done_callback(back)
            task  = [ucid_task,asyncio.ensure_future(fuk(i))]
            res = loop.run_until_complete(asyncio.wait(task))
            # 创建任务处理
            for v in task:
                print(v.result())

    except Exception as e:
        asyncio.gather(*asyncio.Task.all_tasks()).cancel()   # 取消当前所有任务
        loop.stop()

    finally:
        loop.close()

    try:
        new_loop = asyncio.new_event_loop()
        thread = Thread(target=thradfunc,args=(new_loop,))
        thread.setDaemon(True) # 设置为守护进程，主线程退出，子线程跟着完蛋 所以导致数据执行完不成的情况下退出了
        thread.start()

        # 创建新的携程 (使用新线程调用携程方法)
        asyncio.run_coroutine_threadsafe(dowork(2,new_loop),new_loop) # 如果
        asyncio.run_coroutine_threadsafe(dowork('end', new_loop), new_loop)  # 如果
        thread.join() #  等待线程的完成

    except KeyboardInterrupt as e:
        new_loop.stop()
        asyncio.gather(*asyncio.Task.all_tasks()).cancel()


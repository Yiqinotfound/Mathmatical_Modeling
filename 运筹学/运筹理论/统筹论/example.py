import threading
import time
BoilingWater = 0
Teapot_is_clean = 0
Kettle_is_clean = 0
Tea = 0
def getBoilingWater():
    global BoilingWater
    while Kettle_is_clean==0:
          pass
    time.sleep(10)
    BoilingWater = 1
 
def clearTeapot():
    global Teapot_is_clean
    time.sleep(2)
    Teapot_is_clean = 1

def clearKettle():
   global Kettle_is_clean
   time.sleep(1)
   Kettle_is_clean = 1

def getTea():
   global Tea
   time.sleep(1)
   Tea = 1

def makeTea():
   while Tea==0 or Teapot_is_clean==0 or BoilingWater==0:
       pass
   time.sleep(1)
   print(time.time()-start)
 
start = time.time()  # 获取当前时间，保存在start变量中
threadList = []      # 定义一个线程列表
threadList.append(threading.Thread(target=getBoilingWater)) # 在列表中添加线程对象，targer指定线程要执行的函数
threadList.append(threading.Thread(target=clearTeapot))
threadList.append(threading.Thread(target=clearKettle))
threadList.append(threading.Thread(target=getTea))
threadList.append(threading.Thread(target=makeTea))

for t in threadList:   # 遍历threadList 列表中的所有线程对象，并对每个线程调用start方法，以启动线程，这样，所有的线程就可以并发执行
    t.start()
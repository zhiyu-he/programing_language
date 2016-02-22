# -*- coding:utf-8 -*-

import time
import os
import random
from multiprocessing import Process, Queue

def consumer(q):
    # consumer 通过queue获取消费的数据
    while True:
        data = q.get()
        if data is None:
            print "nothing in the queue"
            time.sleep(1)
            continue
        print "data: %s" % data

def info(title):
    print title
    print 'module name: ', __name__
    if hasattr(os, 'getppid'):
        print 'parent process: ', os.getppid()
    print 'process id: ', os.getpid()

def f(name):
    while True:
        info('function f')
        time.sleep(1)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=consumer, args=(q,))
    p.start()
    # p.join()
    print "can do"
    while True:
        num = random.randint(1, 100)
        q.put(num)
        sleep = random.randint(1, 5)
        time.sleep(sleep)

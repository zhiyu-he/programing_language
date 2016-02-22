# -*- coding:utf-8 -*-

import time
import os
from multiprocessing import Process, Queue

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
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

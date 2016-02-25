# -*- coding:utf-8 -*-

import os
import math

# ref http://stackoverflow.com/questions/12233836/python-find-the-absolute-path-of-an-imported-module

if __name__ == '__main__':
    print os.path.abspath(math.__file__)

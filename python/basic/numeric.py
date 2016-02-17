# coding: utf-8

import sys

# 因为第一位是符号位,
INT_64 = 0x7FFFFFFFFFFFFFFF
INT_32 = 0xFFFFFFFF

def print_sys_maxint():
    num = sys.maxint
    print "sys maxint: %s" % num
    print "sys hex(maxint): %s" % hex(num)

# unsigned int64

if __name__ == '__main__':
    print_sys_maxint()
    print hex(sys.maxint)
    print type(sys.maxint)
    print type(INT_64)
    print "numberic type: %s value: %s" % (type(INT_32), INT_32)

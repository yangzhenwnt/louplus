#!/usr/bin/env python3
import sys
def Hours(minute):
    if minute < 0:
        raise ValueError("Inter num is error")
    else:
        print("{}H , {}M".format(int(minute / 60),minute % 60))

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")

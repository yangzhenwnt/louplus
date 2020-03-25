#!/usr/bin/env python3
#对用户输入的数据进行异常检测
print("请输入数字")
try:
    num = input(">>:");
    print("您输入的数字是: %d" % (int(num)))
except ValueError:
    print("您输入的不是数字")
    

#!/usr/bin/env python3
#将字符串写入文件
str = "课程以浅显易懂的语言，以常见的生活场景为案例，带领大家逐步进入计算机编程世界"

filename = "/tmp/sample.txt"
try:
    fp = open(filename,"w+");
    print("%s 文件打开成功" % filename);
    #写入文件
    size = fp.write(str);
    print("共写入 %d个字节到 %s"  % (size,filename));
except IOerror:
    print("%s 文件写入失败" % filename);
finally:
    #关闭文件
    fp.close()

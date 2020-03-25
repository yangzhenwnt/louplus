#!/usr/bin/env python3

def view_dir(path='.'):
    """
    这个函数打印给定目录中的所有文件和目录
    :args path: 指定目录，默认为当前目录
    """
    name = os.listdir(path)
    names.sort()
    for name in name:
        print(name,end = '')
    print()


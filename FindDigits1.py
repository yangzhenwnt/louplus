#!/usr/bin/env python3
import os
import sys

d = open("/tmp/String.txt")
s = d.readlines()
d.close()
print(s)

for i in s:
    if s.isdigit():
        print(i)

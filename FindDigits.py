#!/usr/bin/env python3
with open("/tmp/String.txt") as s:
    str = s.read()
#print(str)
num = ""
for i in str:
    if i.isdigit():
        num += i
print(num)


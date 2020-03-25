#!/usr/bin/env python3
while True:
    n = int(input("please enter an integer: "))
    if n < 0:
        continue  #这会返回循环的开始
    elif n == 0:
        break
    print("Square is ", n ** 2)
print("Goodbye")

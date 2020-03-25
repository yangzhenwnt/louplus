#!/usr/bin/env python3
s = input("Please enter a string: ")
z = s[::-1] #把输入的字符串进行倒序处理形成新的字符串

if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

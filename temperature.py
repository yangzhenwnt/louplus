#!/usr/bin/env python3
fahrenheit = 0
print("fahrenheit Celsius")
while fahrenheit <= 250:
#C=(F-32)/18 将华氏温度转为摄氏温度
    celsius = (fahrenheit - 32 ) / 1.8
    print("{:10d} {:7.2f}".format(fahrenheit,celsius))
    fahrenheit = fahrenheit + 25


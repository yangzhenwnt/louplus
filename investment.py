#!/usr/bin/env python3
#输入额度
amount = float(input("Enter amount: "))
#输入利率
inrate = float(input("Enter Interest rate: "))
#输入期限
period = int(input("Enter period: "))

value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year,value))
    amount = value
    year = year + 1

